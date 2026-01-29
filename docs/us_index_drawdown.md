# Source: https://www.lixinger.com/open/api/doc?api-key=us/index/drawdown

# 指数回撤API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22us%22,%22dataType%22:%22index%22}])

简要描述:

* 获取指数回撤数据。

请求URL:

* `https://open.lixinger.com/api/us/index/drawdown`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| stockCode | Yes | String | 请参考[指数信息API](/open/api/detail?api-key=undefined)获取合法的stockCode。 |
| startDate | Yes | String: YYYY-MM-DD(北京时间) | 信息起始时间。用于获取一定时间范围内的数据。开始和结束的时间间隔不超过10年 |
| endDate | No | String: YYYY-MM-DD(北京时间) | 信息结束时间。用于获取一定时间范围内的数据。默认值是上周一。 |
| granularity | Yes | String | 回撤周期，例如：“y”。当前支持:  * 月: m * 季度: q * 半年: hy * 1年: y1 * 3年: y3 * 5年: y5 * 10年: y10 * 上市以来: fs |

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
|  |

**返回数据说明:** 

| 参数名称 | 数据类型 | 说明 |
| --- | --- | --- |
| date | Date | 数据时间 |
| value | Number | 回撤 |

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
|  |

加载...

加载数据失败。[请点击此处重新尝试](#!)

您需要登录才能浏览该数据，下面是图片示例：

您的会员使用时间已经到期了，下面是示例图片：

##### API试用 (剩余访问次数): **0**

执行

**返回数据:**