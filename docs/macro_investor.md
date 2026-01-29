# Source: https://www.lixinger.com/open/api/doc?api-key=macro/investor

# 投资者API[购买](/open/api/price-tier?api-groups=[{%22dataType%22:%22macro%22}])

简要描述:

* 获取投资者数据，如自然人等。

请求URL:

* `https://open.lixinger.com/api/macro/investor`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| startDate | Yes | String: YYYY-MM-DD(北京时间) | 信息起始时间。开始和结束的时间间隔不超过10年 |
| endDate | Yes | String: YYYY-MM-DD(北京时间) | 信息结束时间。 |
| limit | No | Number | 返回最近数据的数量。limit仅在请求数据为date range的情况下生效。 |
| granularity | Yes | String | 数据统计维度当前支持:  * 月度数据: m。 该数据只有在2015年3月后有数据。 * 周数据: w。 该数据只在2020年4月之间有数据。 |
| areaCode | Yes | String | 区域编码，如{areaCode}。当前支持:  * 大陆: cn |
| metricsList | Yes | Array | 指标数组。如['ni']。 * 新增自然人 :nni * 新增非自然人 :n\_non\_ni * 自然人 :ni * A股自然人 :nia * B股自然人 :nib * 非自然人 :non\_ni * A股非自然人 :non\_nia * B股非自然人 :non\_nib |

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

加载...

加载数据失败。[请点击此处重新尝试](#!)

您需要登录才能浏览该数据，下面是图片示例：

您的会员使用时间已经到期了，下面是示例图片：

##### API试用 (剩余访问次数): **0**

执行

**返回数据:**