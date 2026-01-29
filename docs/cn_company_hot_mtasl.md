# Source: https://www.lixinger.com/open/api/doc?api-key=cn/company/hot/mtasl

# 融资融券API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22cn%22,%22dataType%22:%22company%22}])

简要描述:

* 获取融资融券数据。

说明:

* 计算股本为流通A股

请求URL:

* `https://open.lixinger.com/api/cn/company/hot/mtasl`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| stockCodes | Yes | Array | 股票代码数组。stockCodes长度>=1且<=100，格式如下：["300750","600519","600157"]。 请参考[股票信息API](/open/api/detail?api-key=cn/company)获取合法的stockCode。 |

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |

|
|  |

|
|  |
|
|  |
|

|
|  |

**返回数据说明:** 

| 参数名称 | 数据类型 | 说明 |
| --- | --- | --- |
| stockCode | String | 股票代码 |
| last\_data\_date | Date | 数据时间 |
| spc | Number | 涨跌幅 |
| mtaslb\_fb | Number | 融资余额 |
| mtaslb\_sb | Number | 融券余额 |
| mtaslb | Number | 融资融券余额 |
| mtaslb\_mc\_r | Number | 融资融券余额占流通A股市值比例 |
| mtaslb\_fbc | Number | 新增融资余额 |
| mtaslb\_smc | Number | 新增融券余量 |
| npa\_o\_f\_d1 | Number | 过去1个交易日融资净买入金额 |
| npa\_o\_f\_d5 | Number | 过去5个交易日融资净买入金额 |
| npa\_o\_f\_d20 | Number | 过去20个交易日融资净买入金额 |
| npa\_o\_f\_d60 | Number | 过去60个交易日融资净买入金额 |
| npa\_o\_f\_d120 | Number | 过去120个交易日融资净买入金额 |
| npa\_o\_f\_d240 | Number | 过去240个交易日融资净买入金额 |
| fb\_mc\_rc\_d1 | Number | 过去1个交易日融资余额占流通市值变化比例 |
| fb\_mc\_rc\_d5 | Number | 过去5个交易日融资余额占流通市值变化比例 |
| fb\_mc\_rc\_d20 | Number | 过去20个交易日融资余额占流通市值变化比例 |
| fb\_mc\_rc\_d60 | Number | 过去60个交易日融资余额占流通市值变化比例 |
| fb\_mc\_rc\_d120 | Number | 过去120个交易日融资余额占流通市值变化比例 |
| fb\_mc\_rc\_d240 | Number | 过去240个交易日融资余额占流通市值变化比例 |

| 参数名称 | 数据类型 | 说明 |
| --- | --- | --- |

|
|  |

|
|  |
|
|  |
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|

|
|  |

加载...

加载数据失败。[请点击此处重新尝试](#!)

您需要登录才能浏览该数据，下面是图片示例：

您的会员使用时间已经到期了，下面是示例图片：

##### API试用 (剩余访问次数): **0**

执行

**返回数据:**