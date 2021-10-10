#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""diff_houjin_api_client -- search by period for 法人番号API

市町村コードは「JIS X 0402」参照

"""
from datetime import datetime

from api_client import APIClient
from address import ADDRESS
from corporate_type import CORPORATE_TYPE


class DiffHoujinAPIClient(APIClient):
    """DiffHoujinAPIClient

    DiffHoujinAPIClient is a APIClient.
    Responsibility:
    """

    ADDRESS = ADDRESS

    CORPORATE_TYPE = CORPORATE_TYPE

    def __init__(self, a_application_id, a_data_type, a_from, a_to):
        """

        @Arguments:
        - `a_application_id`: access key for 法人番号API. 13 length
        - `a_data_type`: response data type
        - `a_from`: '2000-01-01' format or datetime.datetime
        - `a_to`: '2000-01-01' format or datetime.datetime
        """
        super(DiffHoujinAPIClient, self).__init__(
            a_application_id, APIClient.REQUEST_TYPE.DIFF, a_data_type)
        if isinstance(a_from, (str, )):
            self.set_parameter('from', a_from)
        if isinstance(a_from, (datetime, )):
            self.set_parameter('from', a_from.strftime('%Y-%m-%d'))
        if isinstance(a_to, (str, )):
            self.set_parameter('to', a_to)
        if isinstance(a_to, (datetime, )):
            self.set_parameter('to', a_to.strftime('%Y-%m-%d'))

    def get_from(self, ):
        r"""Get from date string.

        get_from()

        @Return:
           date string like '2000-01-01'
        @Error:
        """
        return self.get_parameter.get('from')

    def set_from(self, a_from):
        r"""Set from date.

        set_from(a_from)

        @Arguments:
        - `a_from`: '2000-01-01' format or datetime.datetime

        @Return:
           this instance
        @Error:

        """
        if isinstance(a_from, (string, )):
            self.set_parameter('from', a_from)
        if isinstance(a_from, (datetime, )):
            self.set_parameter('from', a_from.strftime('%Y-%m-%d'))
        return self

    def get_to(self, ):
        r"""Get to date string

        get_to()

        @Return:
           date string like '2000-01-01'
        @Error:
        """
        return self.get_parameter('to')

    def set_to(self, a_to):
        r"""Set to date.

        set_to(a_to)

        @Arguments:
        - `a_to`: '2000-01-01' format or datetime.datetime

        @Return:
           this instance
        @Error:

        最大日数は 50 日
        """
        if isinstance(a_to, (basestring, )):
            self.set_parameter('to', a_to)
        if isinstance(a_to, (datetime, )):
            self.set_parameter('to', a_to.strftime('%Y-%m-%d'))
        return self

    def get_address(self, ):
        r"""Get address code.

        get_address()

        @Return:
           address code string
           None if not exists.
        @Error:
        """
        return self.get_parameter('address')

    def set_address(self, a_address):
        r"""Set address code.

        set_address(a_address)

        @Arguments:
        - `a_address`: address code

        @Return:
           this instance
        @Error:

        国内所在地の都道府県コード又は都道府県コードと
        市区町村コードを組み合わせたコードのいずれかを指定できます。
        市区町村コードのみではエラー(エラーコード 051)となります。

        都道府県コード[２桁]（JIS X 0401）をセットします。
        国外所在地を指定する場合は「99」をセットします。
        都道府県コード[２桁]（JIS X 0401）＋市区町村コード[３桁]（JIS X 0402）
        都道府県コード及び市区町村コードの詳細については、
        以下の URL※（日本産業標準調査会/データベース検索）を参照のこと。
        https://www.jisc.go.jp/
        """
        self.set_parameter('address',  a_address)
        return self

    def get_kind(self, ):
        r"""Get corporate type code.

        get_kind()

        @Return:
           corporate type code.
           None if not exists.
        @Error:
        """
        return self.get_parameter('kind')

    def set_kind(self, a_kind):
        r"""Set corporate type code.

        set_kind(a_kind)

        @Arguments:
        - `a_kind`: corporate type code

        @Return:
           this instance
        @Error:
        """
        self.set_parameter('kind', a_kind)
        return self

    def get_divide(self, ):
        r"""Get divide code.

        get_divide()

        @Return:
           divide code
           None if not exists
        @Error:
        """
        return self.get_parameter('divide')

    def set_divide(self, a_divide):
        r"""Set divide code.

        set_divide(a_divide)

        @Arguments:
        - `a_divide`: divide code

        @Return:
          this instance
        @Error:
        """
        self.set_parameter('divide', a_divide)
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# diff_houjin_api_client.py ends here
