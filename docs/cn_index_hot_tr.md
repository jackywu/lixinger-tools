# Source: https://www.lixinger.com/open/api/doc?api-key=cn/index/hot/tr

# 换手率API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22cn%22,%22dataType%22:%22index%22}])

简要描述:

* 获取换手率数据。

请求URL:

* `https://open.lixinger.com/api/cn/index/hot/tr`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| stockCodes | Yes | Array | 指数代码数组。stockCodes长度>=1且<=100，格式如下：["000016"]。 请参考[指数信息API](/open/api/detail?api-key=cn/index)获取合法的stockCode。 |

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
| cpc | Number | 涨跌幅 |
| ta | Number | 成交金额 |
| tr\_d1 | Number | 过去1个交易日换手率 |
| tr\_d5 | Number | 过去5个交易日换手率 |
| tr\_d10 | Number | 过去10个交易日换手率 |
| tr\_d20 | Number | 过去20个交易日换手率 |
| tr\_d60 | Number | 过去60个交易日换手率 |
| tr\_d120 | Number | 过去120个交易日换手率 |
| tr\_d240 | Number | 过去240个交易日换手率 |

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
|  |

加载...

加载数据失败。[请点击此处重新尝试](#!)

您需要登录才能浏览该数据，下面是图片示例：

您的会员使用时间已经到期了，下面是示例图片：

##### API试用 (剩余访问次数): **0**

执行

**返回数据:**