#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/11/9
"""Test render without flask environments
"""

import jinja2


def render_without_request(template_name, **context):
    """
    用法同 flask.render_template:

    render_without_request('template.html', var1='foo', var2='bar')
    """
    env = jinja2.Environment(
        loader=jinja2.PackageLoader('jinjia2_t',))
    template = env.get_template(template_name)
    return template.render(**context)


print(render_without_request("hello.html", name="liuqw", test="tt"))
