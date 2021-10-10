#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""url_builder -- URL Builder for 法人番号API

"""
from urllib import parse as urlparse


class URLBuilder(object):
    """URLBuilder

    URLBuilder is a object.
    Responsibility: Build Request URL for api.houjin-bangou.nta.go.jp
    """
    BASE_URL = "https://api.houjin-bangou.nta.go.jp"

    VERSION = "4"

    def __init__(self, a_request_type, a_data_type):
        """

        @Arguments:
        - `a_request_type`: num, diff, name.
            num: search for Company Code 法人番号検索
            diff: search by period
            name: search by name 法人名
        - `a_data_type`: response data type.
        """
        self._request_type = str(a_request_type)
        self.parameters = {
            'type': str(a_data_type),
        }

    def get_request_type(self, ):
        r"""Return request type string.

        get_request_type()

        @Return:
           request type string.

        @Error:
        """
        return self._request_type

    def set_request_type(self, a_request_type):
        r"""Set request type string.

        set_request_type(a_request_type)

        @Arguments:
        - `a_request_type`: num, diff, name.
            num: search for Company Code 法人番号検索
            diff: search by period
            name: search by name 法人名

        @Return:
           this instance.
        @Error:
        """
        self._request_type = a_request_type
        return self._request_type

    def get_data_type(self, ):
        r"""Get response data type.

        get_data_type()

        @Return:
           response data type.
        @Error:
        """
        return self.parameters.get("type", None)

    def set_data_type(self, a_data_type):
        r"""Set response data type.

        set_data_type(a_data_type)

        @Arguments:
        - `a_data_type`: response data type.

        @Return:
           this instance.
        @Error:
        """
        self.parameters["type"] = str(a_data_type)
        return self

    def get_parameter(self, a_name):
        r"""Get parameter's value.

        get_parameter(a_name)

        @Arguments:
        - `a_name`: name of parameter.

        @Return:
           value of parameter's name.
        @Error:
        """
        return self.parameters.get(a_name, None)

    def set_parameter(self, a_name, a_value):
        r"""Set request parameter.

        set_parameter(a_name, a_value)

        @Arguments:
        - `a_name`: parameter's name
        - `a_value`: parameter's value

        @Return:
           this instance.
        @Error:
        """
        self.parameters[str(a_name)] = a_value
        return self

    def remove_parameter(self, a_name):
        """Remove parameter by name.

        remove_parameter(a_name)

        @Arguments:
        - `a_name`: parameter name

        @Return:
          this instance
        @Error:
        """
        if a_name in self.parameters:
            del self.parameters[a_name]
        return self

    def clear_parameters(self, ):
        """Clear parameters.

        clear_parameters()

        @Return:
           this instance
        @Error:
        """
        self.paramaters.clear()
        return self

    def has_parameter(self, a_name):
        """Check exists parameter.

        has_parameter(a_name)

        @Arguments:
        - `a_name`: parameter name

        @Return:
           true if exists parameter name.
        @Error:
        """
        return a_name in self.parameters

    def build(self, ):
        """Return request url.

        build()

        @Return:
           request url string.
        @Error:
        """
        url = self.BASE_URL
        params = {}
        for name in self.parameters:
            if isinstance(self.parameters[name], (tuple, list)):
                params[name] = ','.join(self.parameters[name])
                continue
            params[name] = self.parameters[name]
        url = url + '/' + self.VERSION
        url = url + '/' + self._request_type
        url = url + '?'
        url = url + urlparse.urlencode(params)
        return url

    def __str__(self):
        return self.build()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# url_builder.py ends here
