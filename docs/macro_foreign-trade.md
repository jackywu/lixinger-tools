# Source: https://www.lixinger.com/open/api/doc?api-key=macro/foreign-trade

# 对外贸易API[购买](/open/api/price-tier?api-groups=[{%22dataType%22:%22macro%22}])

简要描述:

* 获取对外贸易数据，如进出口总额(人民币)等。

请求URL:

* `https://open.lixinger.com/api/macro/foreign-trade`

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
| metricsList | Yes | Array | 指标数组，指标格式为**[granularity].[metricsName].[expressionCalculateType]**。如['y.tiae\_rmb.t'] 指标参数示例:  * 指标名 :metricsName   + granularity(时间粒度):     - expressionCalculateType(数据统计方式):  大陆支持:  * 进出口总额(人民币) :tiae\_rmb   + y(年):     - t(累积) * 进口差额(人民币) :iaeb\_rmb   + y(年):     - t(累积) * 出口总额(人民币) :te\_rmb   + y(年):     - t(累积) * 进口总额(人民币) :ti\_rmb   + y(年):     - t(累积) * 进出口总额(美元) :tiae\_usd   + y(年):     - t(累积)   + m(月):     - t(累积)     - t\_y2y(累积同比)     - c(当期)     - c\_c2c(当期环比) * 进口差额(美元) :iaeb\_usd   + y(年):     - t(累积)   + m(月):     - t(累积)     - c(当期) * 出口总额(美元) :te\_usd   + y(年):     - t(累积)   + m(月):     - t(累积)     - t\_y2y(累积同比)     - c(当期)     - c\_c2c(当期环比) * 进口总额(美元) :ti\_usd   + y(年):     - t(累积)   + m(月):     - t(累积)     - t\_y2y(累积同比)     - c(当期)     - c\_c2c(当期环比) |

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