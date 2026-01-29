# Source: https://www.lixinger.com/open/api/doc?api-key=macro/domestic-debt-securities

# 国内各类债券API[购买](/open/api/price-tier?api-groups=[{%22dataType%22:%22macro%22}])

简要描述:

* 获取国内各类债券数据，如政府债券发行金额等。

请求URL:

* `https://open.lixinger.com/api/macro/domestic-debt-securities`

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
| metricsList | Yes | Array | 指标数组，指标格式为**[granularity].[metricsName].[expressionCalculateType]**。如['y.gs\_i.t'] 指标参数示例:  * 指标名 :metricsName   + granularity(时间粒度):     - expressionCalculateType(数据统计方式):  大陆支持:  * 政府债券发行金额 :gs\_i   + y(年):     - t(累积)   + m(月):     - c(当期) * 金融债券发行金额 :fb\_i   + y(年):     - t(累积)   + m(月):     - c(当期) * 公司信用类债券发行金额 :cdb\_i   + y(年):     - t(累积)   + m(月):     - c(当期) * 国际机构债券发行金额 :iib\_i   + y(年):     - t(累积)   + m(月):     - c(当期) * 政府债券累积余额 :gs\_o   + y(年):     - t(累积)   + m(月):     - t(累积) * 金融债券累积余额 :fb\_o   + y(年):     - t(累积)   + m(月):     - t(累积) * 公司信用类债券累积余额 :cdb\_o   + y(年):     - t(累积)   + m(月):     - t(累积) * 国际机构债券累积余额 :iib\_o   + y(年):     - t(累积)   + m(月):     - t(累积) |

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