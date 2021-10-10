#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""houjinname_api_client -- search by campany name for 法人番号API

"""
from datetime import datetime

from api_client import APIClient
from address import ADDRESS
from corporate_type import CORPORATE_TYPE


class HoujinNameAPIClient(APIClient):
    """HoujinNameAPIClient

    HoujinNameAPIClient is a APIClient.
    Responsibility:
    """
    class MODE:
        PREFIX = "1"  # 前方一致
        PARTIAL = "2" # 部分一致

    class TARGET:
        FUZZY = "1"   # あいまい検索
        EXACT = "2"   # 完全一致
        ENGLISH = "3" # 英語表記 （英語表記登録情報検索）

    ADDRESS = ADDRESS

    CORPORATE_TYPE = CORPORATE_TYPE

    class CHANGE:
        DISABLE = "0"
        ENABLE = "1"

    class CLOSE:
        NOT_CLOSED = "0"
        CLOSED = "1"

    def __init__(self, a_application_id, a_data_type, a_name):
        """

        @Arguments:
        - `a_application_id`:
        - `a_data_type`:
        - `a_name`:

        取得の対象とする法人名を URL エンコード
        （UTF-8）した値をセットします。
        （注１）複数の法人名はセットできません。
        （注２）法人種別及び名称に使用されている文字（漢
        字、ひらがな、カタカナ、アルファベット、数字等）
        はすべて URL エンコード（UTF-8）する必要があります
        が、後述する「商号又は名称検索対象」で「１」又は
        「２」を選択した場合は全角文字、「商号又は名称検索
        対象」で「３」を選択した場合は半角文字を URL エン
        コード（UTF-8）してください。
        （注３）「商号又は名称検索方式」で「１」を設定する
        場合は、法人種別を除いた上で法人名を URL エンコー
        ド（UTF-8）してください。
        （例）「株式会社法人ばんごうＮＵＭ１」の場合
        %E6%A0%AA%E5%BC%8F%E4%BC%9A%E7%A4%BE%E6%B3%
        95%E4%BA%BA%E3%81%B0%E3%82%93%E3%81%94%E3%8
        1%86%EF%BC%AE%EF%BC%B5%EF%BC%AD%EF%BC%91
        """
        super(HoujinNameAPIClient, self).__init__(
            a_application_id, APIClient.REQUEST_TYPE.NAME, a_data_type)
        self.set_parameter('name', a_name)

    def get_name(self, ):
        r"""Get name value.

        get_name()

        @Return:
           name value
        @Error:
        """
        return self.get_parameter('name')

    def set_name(self, a_name):
        r"""Set name value.

        set_name(a_name)

        @Arguments:
        - `a_name`: name of Corporation

        @Return:
           name value
        @Error:
        """
        self.set_parameter('name', a_name)
        return self

    def get_mode(self, ):
        r"""Get mode value.

        get_mode()

        @Return:
           mode value
        @Error:
        """
        return self.get_parameter('mode')

    def set_mode(self, a_mode):
        r"""Set mode value.

        set_mode(a_mode)

        @Arguments:
        - `a_mode`: mode value

        @Return:
           this instance
        @Error:

        検索方式を指定できます。
        指定しない場合は、｢１｣（前方一致検索）で処理します。
        """
        self.set_parameter('mode', a_mode)
        return self

    def get_target(self, ):
        r"""Get target value.

        get_target()

        @Return:
           target value
        @Error:
        """
        return self.get_parameter('target')

    def set_target(self, a_target):
        r"""Set target value.

        set_target(a_target)

        @Arguments:
        - `a_target`: target value

        @Return:
           this instance
        @Error:

        検索対象を指定できます。
        指定しない場合は、｢１｣（JIS 第一・第二水準）（あいまい検索）で処理します。
        """
        self.set_parameter('target', a_target)
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

        法人種別を指定できます。
        カンマ区切りで複数の法人種別を指定できますが、最大４種類までです。
        何も指定しない場合は、全ての法人種別が含まれたデータが応答します。
        """
        self.set_parameter('kind', a_kind)
        return self

    def get_change(self, ):
        r"""Get change value.

        get_change()

        @Return:
           change value
           None if not exists

        @Error:
        """
        return self.get_parameter('change')

    def set_change(self, a_change):
        r"""Set change value.

        set_change(a_change)

        @Arguments:
        - `a_change`: change value

        @Return:
           this instance

        @Error:

        法人名や所在地の変更があった法人等について過去の情報を含めて検索するかどうかを指定できます。
        指定しない場合は、「０」（変更履歴を含めない）で処理します。
        """
        self.set_parameter('change', a_change)
        return self

    def get_closed(self, ):
        """Get closed value.

        get_closed()

        @Return:
           closed value
           None if not exists

        @Error:
        """
        return self.get_parameter('close')

    def enable_closed(self, ):
        """Set closed value.

        enable_closed()

        @Return:
           this instance

        @Error:

        登記記録の閉鎖等があった法人等の情報を取得するかどうかを指定できます。
        指定しない場合は、「１」（登記記録の閉鎖等を含める）で処理します。
        """
        self.set_parameter('close', HoujinNameAPIClient.CLOSE.CLOSED)
        return self

    def disable_closed(self, ):
        """Set disable closed.

        disable_closed()

        @Return:
           this instance
        @Error:

        登記記録の閉鎖等があった法人等の情報を取得するかどうかを指定できます。
        指定しない場合は、「１」（登記記録の閉鎖等を含める）で処理します。
        """
        self.set_parameter('close', HoujinNameAPIClient.CLOSE.NOT_CLOSED)
        return self

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
# houjinname_api_client.py ends here
