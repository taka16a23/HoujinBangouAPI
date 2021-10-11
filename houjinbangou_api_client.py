#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""houjinbangou_api_client -- search number client for 法人番号API

"""
from .api_client import APIClient


class HoujinBangouAPIClient(APIClient):
    """HoujinBangouAPIClient

    HoujinBangouAPIClient is a APIClient.
    Responsibility:
    """
    class HISTORY:
        DISABLE = "0"
        ENABLE = "1"

    def __init__(self, a_application_id, a_data_type, a_sHistory=None):
        """

        @Arguments:
        - `a_application_id`: access key for 法人番号API. 13 length
        - `a_data_type`: response data type
        - `a_sHistory`: includ history on response data
        """
        super(HoujinBangouAPIClient, self).__init__(
            a_application_id, APIClient.REQUEST_TYPE.NUMBER, a_data_type)
        history = a_sHistory
        if history is None:
            history = HoujinBangouAPIClient.HISTORY.DISABLE
        self.url_builder.set_parameter('history', history)

    def add_number(self, a_number):
        """Add search campany number.

        add_number(a_number)

        @Arguments:
        - `a_number`: campany number as string

        @Return:
           this instance
        @Error:
        """
        if not isinstance(self.url_builder.get_parameter('number'), (tuple, list)):
            self.url_builder.set_parameter('number', [])
        self.url_builder.parameters['number'].append(str(a_number))
        return self

    def extend_numbers(self, a_iterable):
        """Extend campany numbers.

        extend_numbers(a_iterable)

        @Arguments:
        - `a_iterable`: tuple or list of numbers

        @Return:
          this instance.
        @Error:
        """
        if not isinstance(self.url_builder.get_parameter('number'), (tuple, list)):
            self.url_builder.set_parameter('number', [])
        self.url_builder.parameters['number'].extend(a_iterable)
        return self

    def remove_number(self, a_number):
        """Remove campany number.

        remove_number(a_number)

        @Arguments:
        - `a_number`: campany number as string

        @Return:
           this instance
        @Error:
        """
        if not isinstance(self.url_builder.get_parameter('number'), (tuple, list)):
            self.url_builder.set_parameter('number', [])
        if a_number in self.url_builder.parameter['number']:
            self.url_builder.parameter['number'].remove(a_number)
        return self

    def clear_number(self, ):
        """Clear campany number.

        clear_number()

        @Return:
           this instance
        @Error:
        """
        self.set_parameter('number', [])
        return self

    def has_number(self, a_number):
        """Exists campany number.

        has_number(a_number)

        @Arguments:
        - `a_number`: campany number

        @Return:
           true if exists campany numbers.
        @Error:
        """
        if not self.get_parameter('number'):
            return False
        return a_number in self.get_parameter('number')

    def is_enabled_history(self, ):
        """Check enabled history.

        is_enabled_history()

        @Return:
           true if history enable.
        @Error:
        """
        return HoujinBangouAPIClient.HISTORY.ENABLE == self.get_parameter('history')

    def disable_history(self, ):
        """Set disable history.

        disable_history()

        @Return:
           this instance
        @Error:
        """
        self.set_parameter('history', HoujinBangouAPIClient.HISTORY.DISABLE)
        return self

    def enable_history(self, ):
        """Set enable history.

        enable_history()

        @Return:
           this instance
        @Error:
        """
        self.set_parameter('history', HoujinBangouAPIClient.HISTORY.ENABLE)
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# houjinbangou_api_client.py ends here
