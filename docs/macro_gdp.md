# Source: https://www.lixinger.com/open/api/doc?api-key=macro/gdp

# Gdp API[购买](/open/api/price-tier?api-groups=[{%22dataType%22:%22macro%22}])

简要描述:

* 获取GDP数据，如GDP等。

请求URL:

* `https://open.lixinger.com/api/macro/gdp`

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
| metricsList | Yes | Array | 指标数组，指标格式为**[granularity].[metricsName].[expressionCalculateType]**。如['y.gdp.t'] 指标参数示例:  * 指标名 :metricsName   + granularity(时间粒度):     - expressionCalculateType(数据统计方式):  大陆支持:  * GDP :gdp   + y(年):     - t(累积)     - t\_y2y(累积同比)   + q(季度):     - t(累积)     - t\_y2y(累积同比)     - c(当期)     - c\_c2c(当期环比) * 不变价GDP :gdp\_cp   + y(年):     - t(累积)     - c(当期) * 人均GDP :per\_gdp   + y(年):     - t(累积)     - t\_y2y(累积同比) * 第一产业GDP :pi\_gdp   + y(年):     - t(累积)     - t\_y2y(累积同比)   + q(季度):     - t(累积)     - t\_y2y(累积同比)     - c(当期)     - c\_c2c(当期环比) * 第二产业GDP :si\_gdp   + y(年):     - t(累积)     - t\_y2y(累积同比)   + q(季度):     - t(累积)     - t\_y2y(累积同比)     - c(当期)     - c\_c2c(当期环比) * 第三产业GDP :ti\_gdp   + y(年):     - t(累积)     - t\_y2y(累积同比)   + q(季度):     - t(累积)     - t\_y2y(累积同比)     - c(当期)     - c\_c2c(当期环比) * 第一产业对GDP贡献率 :pi\_gdp\_c\_r   + y(年):     - t(累积)   + q(季度):     - t(累积)     - c(当期) * 第二产业对GDP贡献率 :si\_gdp\_c\_r   + y(年):     - t(累积)   + q(季度):     - t(累积)     - c(当期) * 第三产业对GDP贡献率 :ti\_gdp\_c\_r   + y(年):     - t(累积)   + q(季度):     - t(累积)     - c(当期) * GNI :gni   + y(年):     - t(累积)     - t\_y2y(累积同比)  美国支持:  * GDP :gdp   + y(年):     - t(累积)     - t\_y2y(累积同比)   + q(季度):     - t(累积)     - t\_c2c(累积环比)     - t\_y2y(累积同比) |

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