# Source: https://www.lixinger.com/open/api/doc?api-key=macro/national-debt

# 国债API[购买](/open/api/price-tier?api-groups=[{%22dataType%22:%22macro%22}])

简要描述:

* 获取国债数据，如十年期收益率等。

请求URL:

* `https://open.lixinger.com/api/macro/national-debt`

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
| metricsList | Yes | Array | 指标数组。如['tcm\_y10']。 大陆支持:  * 三月期收益率 :tcm\_m3 * 六月期收益率 :tcm\_m6 * 一年期收益率 :tcm\_y1 * 二年期收益率 :tcm\_y2 * 三年期收益率 :tcm\_y3 * 五年期收益率 :tcm\_y5 * 七年期收益率 :tcm\_y7 * 十年期收益率 :tcm\_y10 * 二十年期收益率 :tcm\_y20 * 三十年期收益率 :tcm\_y30  美国支持:  * 三月期收益率 :tcm\_m3 * 六月期收益率 :tcm\_m6 * 一年期收益率 :tcm\_y1 * 二年期收益率 :tcm\_y2 * 三年期收益率 :tcm\_y3 * 五年期收益率 :tcm\_y5 * 七年期收益率 :tcm\_y7 * 十年期收益率 :tcm\_y10 * 二十年期收益率 :tcm\_y20 * 三十年期收益率 :tcm\_y30 |

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