#!/usr/bin/env python
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqingwei <liuqingwei@chuangxin.com>
# Date:   2018/7/9
# coding=utf-8
"""Worker to do the object function give the paramets.
Commands:
python -m scripts.hyperopt-mongo-worker --mongo=localhost:27017/ts_hyperopt --poll-interval=0.1
"""

import sys
sys.path.append('')
import logging
import time
import hyperopt.mongoexp
from ts_run_parallel import fn_obj


logging.basicConfig(stream=sys.stderr, level=logging.INFO)
sys.exit(hyperopt.mongoexp.main_worker())
