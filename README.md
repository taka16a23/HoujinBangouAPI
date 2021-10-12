# HoujinBangouAPI
国税庁法人番号APIクライアント

## 概要
[法人番号システム Web-API｜国税庁法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/webapi/)
にて提供されているAPIのクライアントです。

利用には上記サイトで発行していただいたアプリケーションIDが必要です。

バージョンは4のみ対応となります。

## 利用方法
法人番号検索
```python
  import HoujinBangouAPI
  # 取得したアプリケーションID
  application_id = 'xxxxxxxxxxxxx' 
  # 取得データタイプを指定 ここでは xml unicode
  data_type = HoujinBangouAPI.HoujinBangouAPIClient.DATA_TYPE.XML_UNICODE
  # インスタンス作成
  client = HoujinBangouAPI.HoujinBangouAPIClient(application_id, data_type)
  # 検索対象の法人番号を指定
  client.add_number('8040001999013') 
  # 問い合わせ
  ret = client.request()
  # 取得結果を表示
  print(ret.raw.text)
```

期間検索
```python
  import HoujinBangouAPI
  # 取得したアプリケーションID
  application_id = 'xxxxxxxxxxxxx' 
  # 取得データタイプを指定 ここでは xml unicode
  data_type = HoujinBangouAPI.DiffHoujinAPIClient.DATA_TYPE.XML_UNICODE
  # 開始日
  from_date = '2021-10-10'
  to_date = '2021-10-11'
  # インスタンス作成
  client = HoujinBangouAPI.DiffHoujinAPIClient(application_id, data_type, from_date, to_date)
  # 問い合わせ
  ret = client.request()
  # 取得結果を表示
  print(ret.raw.text)
```

法人名検索
```python
  import HoujinBangouAPI
  # 取得したアプリケーションID
  application_id = 'xxxxxxxxxxxxx' 
  # 取得データタイプを指定 ここでは xml unicode
  data_type = HoujinBangouAPI.HoujinNameAPIClient.DATA_TYPE.XML_UNICODE
  # 検索法人名 必須
  name = "国税庁"
  # インスタンス作成
  client = HoujinBangouAPI.HoujinNameAPIClient(application_id, data_type, name)
  # 問い合わせ
  ret = client.request()
  # 取得結果を表示
  print(ret.raw.text)
```

## ライセンス
MIT
