# Source: https://www.lixinger.com/open/api/doc?api-key=cn/industry/constituents/sw_2021

# 样本信息API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22cn%22,%22dataType%22:%22industry%22}])

简要描述:

* 获取样本信息。

请求URL:

* `https://open.lixinger.com/api/cn/industry/constituents/sw_2021`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| stockCodes | No | Array | 行业代码数组。stockCodes长度>=1且<=100，格式如下：["490000"]。 请参考[行业信息API](/open/api/detail?api-key=cn/industry)获取合法的stockCode。 |
| date | Yes | String: latest | YYYY-MM-DD(北京时间) | 信息日期。 |

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
|  |

**返回数据说明:** 

| 参数名称 | 数据类型 | 说明 |
| --- | --- | --- |
| stockCode | String | 指数代码 |
| constituents.$.stockCode | String | 样本股票代码 |
| constituents.$.areaCode | String | 地区代码 |
| constituents.$.market | String | 市场 |

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