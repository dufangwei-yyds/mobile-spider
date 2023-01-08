# -*- coding: utf-8 -*-
# @Time    : 2022/12/20 19:55
# @Author  : bruce
# @Email   : d920130d2@163.com
# @File    : mitmdump_test.py
# @Software: PyCharm

from mitmproxy import ctx


def request(flow):
    # print(flow.request.headers)
    ctx.log.info(str(flow.request.headers))
    ctx.log.warn(str(flow.request.host))
    ctx.log.error(str(flow.request.url))
    ctx.log.warn(str(flow.request.method))
    ctx.log.info(str(flow.request.path))


def response(flow):
    ctx.log.error(str(flow.response.status_code))
    ctx.log.error(str(flow.response.text))
