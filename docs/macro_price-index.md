# Source: https://www.lixinger.com/open/api/doc?api-key=macro/price-index

# 价格指数API[购买](/open/api/price-tier?api-groups=[{%22dataType%22:%22macro%22}])

简要描述:

* 获取价格指数数据，如居民消费价格指数(CPI)等。

请求URL:

* `https://open.lixinger.com/api/macro/price-index`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| startDate | Yes | String: YYYY-MM-DD(北京时间) | 信息起始时间。开始和结束的时间间隔不超过10年 |
| endDate | Yes | String: YYYY-MM-DD(北京时间) | 信息结束时间。 |
| limit | No | Number | 返回最近数据的数量。limit仅在请求数据为date range的情况下生效。 |
| areaCode | Yes | String | 区域编码，如{areaCode}。当前支持:  * 大陆: cn * 美国: us |
| metricsList | Yes | Array | 指标数组，指标格式为**[granularity].[metricsName].[expressionCalculateType]**。如['y.cpi.t'] 指标参数示例:  * 指标名 :metricsName   + granularity(时间粒度):     - expressionCalculateType(数据统计方式):  大陆支持:  * 居民消费价格指数(CPI) :cpi   + y(年):     - t(累积)   + m(月):     - t(累积) * 核心居民消费价格指数(CCPI) :ccpi   + m(月):     - t(累积) * 城市居民消费价格指数 :ucpi   + y(年):     - t(累积)   + m(月):     - t(累积) * 农村居民消费价格指数 :rcpi   + y(年):     - t(累积)   + m(月):     - t(累积) * 居民消费水平 :hci   + y(年):     - t(累积)     - t\_y2y(累积同比) * 农村居民消费水平 :rrci   + y(年):     - t(累积)     - t\_y2y(累积同比) * 城镇居民消费水平 :urci   + y(年):     - t(累积)     - t\_y2y(累积同比) * 工业品出厂价格指数(PPI) :ppi   + y(年):     - t(累积)   + m(月):     - t(累积) * 工业生产者购进价格指数(PPPI) :pppi   + y(年):     - t(累积)   + m(月):     - t(累积) * 制造业采购经理指数 :mi\_pmi   + m(月):     - t(累积) * 非制造业采购经理指数 :n\_mi\_pmi   + m(月):     - t(累积) * 综合采购经理指数 :c\_pmi   + m(月):     - t(累积)  美国支持:  * 美国-所有城市消费者的消费物价指数：美国城市平均所有项目（季调） :cpiaucsl   + y(年):     - t(累积)     - t\_y2y(累积同比)   + q(季度):     - t(累积)     - t\_y2y(累积同比)     - t\_c2c(累积环比)   + m(月):     - t(累积)     - t\_y2y(累积同比)     - t\_c2c(累积环比) * 生产者价格指数按商品分类：最终需求 :ppifis   + m(月):     - t(累积)     - t\_y2y(累积同比)   + q(季度):     - t(累积)     - t\_y2y(累积同比)     - t\_c2c(累积环比)   + y(年):     - t(累积)     - t\_y2y(累积同比)     - t\_c2c(累积环比) * 制造业采购经理指数 :mi\_pmi   + m(月):     - t(累积) |

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