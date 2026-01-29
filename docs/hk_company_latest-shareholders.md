# Source: https://www.lixinger.com/open/api/doc?api-key=hk/company/latest-shareholders

# 最新股东API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22hk%22,%22dataType%22:%22company%22}])

简要描述:

* 获取最新股东数据。

请求URL:

* `https://open.lixinger.com/api/hk/company/latest-shareholders`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| stockCode | Yes | String | 股票代码请参考[股票信息API](/open/api/detail?api-key=hk/company)获取合法的stockCode。 |

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
| date | Date | 最后申报有关通知之日期 |
| name | String | 姓名 |
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
|  |

加载...

加载数据失败。[请点击此处重新尝试](#!)

您需要登录才能浏览该数据，下面是图片示例：

您的会员使用时间已经到期了，下面是示例图片：

##### API试用 (剩余访问次数): **0**

执行

**返回数据:**