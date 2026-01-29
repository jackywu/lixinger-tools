# Source: https://www.lixinger.com/open/api/doc?api-key=cn/industry/margin-trading-and-securities-lending/sw_2021

# 融资融券API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22cn%22,%22dataType%22:%22industry%22}])

简要描述:

* 获取融资融券数据。

请求URL:

* `https://open.lixinger.com/api/cn/industry/margin-trading-and-securities-lending/sw_2021`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| stockCode | Yes | String | 请参考[行业信息API](/open/api/detail?api-key=cn/industry)获取合法的stockCode。 |
| startDate | Yes | String: YYYY-MM-DD(北京时间) | 信息起始时间。用于获取一定时间范围内的数据。开始和结束的时间间隔不超过10年 |
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
|  |

**返回数据说明:** 

| 参数名称 | 数据类型 | 说明 |
| --- | --- | --- |
| date | Date | 数据时间 |
| financingBalance | Number | 融资余额 |
| securitiesBalance | Number | 融券余额 |
| financingBalanceToMarketCap | Number | 融资余额占流通市值比例 |
| securitiesBalanceToMarketCap | Number | 融券余额占流通市值比例 |

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
|  |

加载...

加载数据失败。[请点击此处重新尝试](#!)

您需要登录才能浏览该数据，下面是图片示例：

您的会员使用时间已经到期了，下面是示例图片：

##### API试用 (剩余访问次数): **0**

执行

**返回数据:**