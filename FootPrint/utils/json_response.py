# -*- coding: utf-8 -*-

"""
@author: 猿小天
@contact: QQ:1638245306
@Created on: 2021/6/2 002 14:43
@Remark: 自定义的JsonResonpse文件
"""
import decimal

from rest_framework.response import Response

# http://blog.ironhead.ninja/2015/04/30/decimal-in-django-json-encoder.html
# https://juejin.cn/post/6844903510543171592

import simplejson

def default_json_encoder(o) :
    if isinstance(o,  decimal.Decimal):
        fs = str(o.quantize(decimal.Decimal('0.00')))
        # if fs.endswith('.00'):
        fs =fs.replace('.00','')
        return fs
    return o
    # if isinstance(o, datetime.datetime):
    #     r = o.isoformat()
    #     if o.microsecond:
    #         r = r[:23] + r[26:]
    #     if r.endswith('+00:00'):
    #         r = r[:-6] + 'Z'
    #     return r
    # elif isinstance(o, datetime.date):
    #     return o.isoformat()
    # elif isinstance(o, datetime.time):
    #     if is_aware(o):
    #         raise ValueError("JSON can't represent timezone-aware times.") raise ValueError("JSON can't represent timezone-aware times.")
    #     r = o.isoformat()
    #     if o.microsecond:
    #         r = r[:12]
    #     return r
    # else:
    #     raise TypeError(repr(o) + ' is not JSON serializable')


class SuccessResponse(Response):
    """
    标准响应成功的返回, SuccessResponse(data)或者SuccessResponse(data=data)
    (1)默认code返回2000, 不支持指定其他返回码
    """

    def __init__(self, data=None, msg='success', status=None, template_name=None, headers=None, exception=False,
                 content_type=None,page=1,limit=1,total=1):
        # if isinstance(data, dict):
        #     data = simplejson.dumps(data, default=default_json_encoder)
        std_data = {
            "code": 2000,
            "data": {
                "page": page,
                "limit": limit,
                "total": total,
                "data": data
            },
            "msg": msg
        }
        super().__init__(std_data, status, template_name, headers, exception, content_type)


class DetailResponse(Response):
    """
    不包含分页信息的接口返回,主要用于单条数据查询
    (1)默认code返回2000, 不支持指定其他返回码
    """

    def __init__(self, data=None, msg='success', status=None, template_name=None, headers=None, exception=False,
                 content_type=None,):
        # if isinstance(data, dict):
        #     data = simplejson.dumps(data, default=default_json_encoder)
        std_data = {
            "code": 2000,
            "data": data,
            "msg": msg
        }
        super().__init__(std_data, status, template_name, headers, exception, content_type)


class ErrorResponse(Response):
    """
    标准响应错误的返回,ErrorResponse(msg='xxx')
    (1)默认错误码返回400, 也可以指定其他返回码:ErrorResponse(code=xxx)
    """

    def __init__(self, data=None, msg='error', code=400, status=None, template_name=None, headers=None,
                 exception=False, content_type=None):
        std_data = {
            "code": code,
            "data": data,
            "msg": msg
        }
        super().__init__(std_data, status, template_name, headers, exception, content_type)


