# Source: https://www.lixinger.com/open/api/doc?api-key=macro/bop

# 国际收支平衡API[购买](/open/api/price-tier?api-groups=[{%22dataType%22:%22macro%22}])

简要描述:

* 获取国际收支平衡数据，如资本账户差额等。

请求URL:

* `https://open.lixinger.com/api/macro/bop`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| startDate | Yes | String: YYYY-MM-DD(北京时间) | 信息起始时间。开始和结束的时间间隔不超过10年 |
| endDate | Yes | String: YYYY-MM-DD(北京时间) | 信息结束时间。 |
| limit | No | Number | 返回最近数据的数量。limit仅在请求数据为date range的情况下生效。 |
| areaCode | Yes | String | 区域编码，如{areaCode}。当前支持:  * 大陆: cn |
| metricsList | Yes | Array | 指标数组，指标格式为**[granularity].[metricsName].[expressionCalculateType]**。如['y.bop\_ca.t'] 指标参数示例:  * 指标名 :metricsName   + granularity(时间粒度):     - expressionCalculateType(数据统计方式):  大陆支持:  * 经常账户差额 :bop\_cura   + y(年):     - t(累积)   + q(季度):     - c(当期) * 货物于服务差额 :bop\_gas   + y(年):     - t(累积)   + q(季度):     - c(当期) * 货物差额 :bop\_g   + y(年):     - t(累积)   + q(季度):     - c(当期) * 服务差额 :bop\_s   + y(年):     - t(累积)   + q(季度):     - c(当期) * 初次收入差额 :bop\_firi   + y(年):     - t(累积)   + q(季度):     - c(当期) * 二次收入差额 :bop\_seci   + y(年):     - t(累积)   + q(季度):     - c(当期) * 资本与金融账户差额 :bop\_cafa   + y(年):     - t(累积)   + q(季度):     - c(当期) * 资本账户差额 :bop\_ca   + y(年):     - t(累积)   + q(季度):     - c(当期) * 金融账户差额 :bop\_fa   + y(年):     - t(累积)   + q(季度):     - c(当期) * 非储备性质金融账户差额 :bop\_nsfa   + y(年):     - t(累积)   + q(季度):     - c(当期) * 直接投资差额 :bop\_di   + y(年):     - t(累积)   + q(季度):     - c(当期) * 证券投资差额 :bop\_si   + y(年):     - t(累积)   + q(季度):     - c(当期) * 金融衍生工具差额 :bop\_nsfa\_fd   + y(年):     - t(累积)   + q(季度):     - c(当期) * 其他投资差额 :bop\_nsfa\_oi   + y(年):     - t(累积)   + q(季度):     - c(当期) * 储备资产差额 :bop\_ra   + y(年):     - t(累积)   + q(季度):     - c(当期) * 净误差与遗漏差额 :bop\_eao   + y(年):     - t(累积)   + q(季度):     - c(当期) |

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

加载...

加载数据失败。[请点击此处重新尝试](#!)

您需要登录才能浏览该数据，下面是图片示例：

您的会员使用时间已经到期了，下面是示例图片：

##### API试用 (剩余访问次数): **0**

执行

**返回数据:**