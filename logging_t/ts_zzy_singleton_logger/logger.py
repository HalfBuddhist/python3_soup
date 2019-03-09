# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: Zhiya Zang <zangzhiya@chuangxin.com>
# Date:   2019-01-18

import socket
import multiprocessing
import logging
from logging import handlers
from logging import LoggerAdapter

from base.singleton import Singleton


_extra_dict = {
    "IP": socket.gethostbyname(socket.getfqdn(socket.gethostname())),
    "HOST": socket.getfqdn(socket.gethostname()),
    "KEYWORD": ""
}

# use the default date format, '%Y-%m-%d %H:%M:%S', '%s,%03d'
_formatter = logging.Formatter(
    "%(IP)s -- [%(asctime)s] [%(name)s] [%(filename)s(%(lineno)d)] "
    "[%(levelname)s] #%(KEYWORD)s# %(message)s")

# add the "DEBUG" element for debug.
_levels_to_record = [
    {
        "name": "INFO",
        "value": logging.INFO
    },
    {
        "name": "WARNING",
        "value": logging.WARNING
    },
    {
        "name": "ERROR",
        "value": logging.ERROR
    }
]


class LoggerHelper(metaclass=Singleton):

    def __init__(self):
        self._queue = multiprocessing.Queue()

    def setup(self, helper_name, log_dir):
        self._init_consume_logger(helper_name, log_dir)

    def get_logger(self, logger_name):
        queue_handler = handlers.QueueHandler(self._queue)
        queue_handler.setFormatter(_formatter)

        logger = logging.getLogger(logger_name)
        logger.handlers.clear()
        logger.addHandler(queue_handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False  # don't propagate to the root logger.

        return LoggerAdapter(logger, _extra_dict)

    def _init_consume_logger(self, helper_name, log_dir):
        file_logger = logging.getLogger(helper_name)

        for level in _levels_to_record:
            file_path = "{}/{}.log.{}".format(
                log_dir, helper_name, level["name"])
            handler = handlers.TimedRotatingFileHandler(
                file_path, backupCount=180, encoding="utf-8", when="midnight")
            handler.suffix = "%Y-%m-%d"
            handler.setLevel(logging.ERROR)
            file_logger.addHandler(handler)

        log_queue_listener = handlers.QueueListener(
            self._queue, *file_logger.handlers, respect_handler_level=True)
        log_queue_listener.start()
