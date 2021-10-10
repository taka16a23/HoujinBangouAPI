#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""api_client -- api client for 法人番号API

"""
import requests

from url_builder import URLBuilder
from api_response import Response


class APIClient(object):
    """APIClient

    APIClient is a object.
    Responsibility:
    """
    class REQUEST_TYPE:
        NUMBER = 'num'
        DIFF = 'diff'
        NAME = 'name'

    class DATA_TYPE:
        CSV_SHIFT_JIS = "01"
        CSV_UNICODE = "02"
        XML_UNICODE = "12"

    def __init__(self, a_application_id, a_request_type, a_data_type):
        """

        @Arguments:
        - `a_application_id`: access key for 法人番号API
        - `a_request_type`: num, diff, name.
            num: search for Company Code 法人番号検索
            diff: search by period
            name: search by name 法人名
        - `a_data_type`: response data type
        """
        self.application_id = str(a_application_id)
        self.url_builder = URLBuilder(a_request_type, a_data_type)
        self.url_builder.set_parameter('id', self.application_id)

    def get_application_id(self, ):
        r"""Get application id.

        get_application_id()

        @Return:
           application id string
        @Error:
        """
        return self.application_id

    def set_application_id(self, a_application_id):
        r"""Set application id.

        set_application_id(a_application_id)

        @Arguments:
        - `a_application_id`: application id for api

        @Return:
           this instance
        @Error:
        """
        self.application_id = str(a_application_id)
        self.url_builder.set_parameter('id', self.application_id)
        return self

    def get_data_type(self, ):
        r"""Get data type.

        get_data_type()

        @Return:

        @Error:
        """
        return self.url_builder.get_data_type()

    def set_data_type(self, a_data_type):
        r"""Set data type.

        set_data_type(a_data_type)

        @Arguments:
        - `a_data_type`: data type string

        @Return:
           this instance
        @Error:
        """
        self.url_builder.set_data_type(a_data_type)
        return self

    def get_parameter(self, a_name):
        r"""Get paramter value by name.

        get_parameter(a_name)

        @Arguments:
        - `a_name`: parameter name

        @Return:
           paramter value as string.
           also return None if not exists.
        @Error:
        """
        return self.url_builder.get_parameter(a_name)

    def set_parameter(self, a_name, a_value):
        r"""Set parameter value.

        set_parameter(a_name, a_value)

        @Arguments:
        - `a_name`: parameter's name
        - `a_value`: parameter's value

        @Return:
           this instance
        @Error:
        """
        self.url_builder.set_parameter(a_name, a_value)
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
        self.url_builder.remove_parameter(a_name)
        return self

    def clear_parameters(self, ):
        """Clear parameters.

        clear_parameters()

        @Return:
           this instance
        @Error:
        """
        self.url_builder.clear_parameters()
        self.url_builder.set_parameter('id', self.application_id)
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
        return self.url_builder.has_parameter(a_name)

    def request(self, ):
        """Execute request to API.

        request()

        @Return:
           response

        @Error:
        """
        url = self.url_builder.build()
        return Response(requests.get(url))

    def __str__(self):
        return self.url_builder.build()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# api_client.py ends here
