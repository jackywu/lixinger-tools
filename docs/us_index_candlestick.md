# Source: https://www.lixinger.com/open/api/doc?api-key=us/index/candlestick

# K线数据API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22us%22,%22dataType%22:%22index%22}])

简要描述:

* 获取K线数据。

说明:

* 中证指数全收益率2016年以前没有数据。

请求URL:

* `https://open.lixinger.com/api/us/index/candlestick`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| stockCode | Yes | String | 请参考[指数信息API](/open/api/detail?api-key=undefined)获取合法的stockCode。stockCode仅在请求数据为date range的情况下生效。 |
| type | Yes | String | 收盘点位类型，例如，“normal”。当前支持:  * 正常点位: normal  * 全收益率点位: total\_return |
| date | No | String: YYYY-MM-DD(北京时间) | 信息日期。用于获取指定日期数据。 |
| startDate | No | String: YYYY-MM-DD(北京时间) | 信息起始时间。用于获取一定时间范围内的数据。开始和结束的时间间隔不超过10年 |
| endDate | No | String: YYYY-MM-DD(北京时间) | 信息结束时间。用于获取一定时间范围内的数据。默认值是上周一。 |
| limit | No | Number | 返回最近数据的数量。 |

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
|
|
|
|

|
|  |

**返回数据说明:** 

| 参数名称 | 数据类型 | 说明 |
| --- | --- | --- |
| date | Date | 数据时间 |
| open | Number | 开盘价 |
| close | Number | 收盘价 |
| high | Number | 最高价 |
| low | Number | 最低价 |
| volume | Number | 成交量 |
| amount | Number | 金额 |
| change | Number | 涨跌幅 |

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
|  |

加载...

加载数据失败。[请点击此处重新尝试](#!)

您需要登录才能浏览该数据，下面是图片示例：

您的会员使用时间已经到期了，下面是示例图片：

##### API试用 (剩余访问次数): **0**

执行

**返回数据:**