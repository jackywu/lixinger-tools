# Source: https://www.lixinger.com/open/api/doc?api-key=macro/population

# 人口API[购买](/open/api/price-tier?api-groups=[{%22dataType%22:%22macro%22}])

简要描述:

* 获取人口数据，如总人口等。

请求URL:

* `https://open.lixinger.com/api/macro/population`

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
| metricsList | Yes | Array | 指标数组，指标格式为**[granularity].[metricsName].[expressionCalculateType]**。如['y.tp.t'] 指标参数示例:  * 指标名 :metricsName   + granularity(时间粒度):     - expressionCalculateType(数据统计方式):  大陆支持:  * 总人口 :tp   + y(年):     - t(累积) * 男性总人口 :tmp   + y(年):     - t(累积) * 女性总人口 :tfp   + y(年):     - t(累积) * 人口增长率 :pb\_r   + y(年):     - t(累积) * 人口死亡率 :pm\_r   + y(年):     - t(累积) * 人口自然增长率 :png\_r   + y(年):     - t(累积) * 0至14岁总人口 :tp\_a\_0\_14   + y(年):     - t(累积) * 15至64岁总人口 :tp\_a\_15\_64   + y(年):     - t(累积) * 65岁以上总人口 :tp\_a\_65   + y(年):     - t(累积) * 少儿抚养比 :cr\_r   + y(年):     - t(累积) * 老年抚养比 :or\_r   + y(年):     - t(累积) |

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