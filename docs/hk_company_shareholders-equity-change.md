# Source: https://www.lixinger.com/open/api/doc?api-key=hk/company/shareholders-equity-change

# 股东权益变动API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22hk%22,%22dataType%22:%22company%22}])

简要描述:

* 获取股东权益变动数据。

请求URL:

* `https://open.lixinger.com/api/hk/company/shareholders-equity-change`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| stockCode | No | String | 请参考[股票信息API](/open/api/detail?api-key=hk/company)获取合法的stockCode。stockCode仅在请求数据为date range的情况下生效。 |
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
|  |

**返回数据说明:** 

| 参数名称 | 数据类型 | 说明 |
| --- | --- | --- |
| date | Date | 日期 |
| name | String | 姓名 |
| numOfSharesInvolvedList | Array | 持有权益的股份数量 子字段:  * 数额: value: (Number) * 股份类型: sharesType: (String) |
| numOfSharesInterestedList | Array | 持有权益的股份数目 子字段:  * 数额: value: (Number) * 股份类型: sharesType: (String) |
| percentageOfIssuedVotingShares | Array | 占已发行的有投票权股份百分比 子字段:  * 数额: value: (Number) * 股份类型: sharesType: (String) |

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

* [通过日期获取](#!)
* [通过时间范围获取](#!)

执行

**返回数据:**