# Source: https://www.lixinger.com/open/api/doc?api-key=cn/company/hot/shnc

# 股东人数变化API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22cn%22,%22dataType%22:%22company%22}])

简要描述:

* 获取股东人数变化数据。

请求URL:

* `https://open.lixinger.com/api/cn/company/hot/shnc`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| stockCodes | Yes | Array | 股票代码数组。stockCodes长度>=1且<=100，格式如下：["300750","600519","600157"]。 请参考[股票信息API](/open/api/detail?api-key=cn/company)获取合法的stockCode。 |

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
|  |

**返回数据说明:** 

| 参数名称 | 数据类型 | 说明 |
| --- | --- | --- |
| stockCode | String | 股票代码 |
| shnc\_rld | Date | 最新数据时间 |
| shnc\_rln | Number | 最新股东人数 |
| shnc\_d10 | Number | 10天股东人数变化 |
| shnc\_d20 | Number | 20天股东人数变化 |
| shnc\_d30 | Number | 30天股东人数变化 |
| shnc\_d60 | Number | 60天股东人数变化 |
| shnc\_d90 | Number | 90天股东人数变化 |
| shnc\_qld | Date | 最新季度数据时间 |
| shnc\_qln | Number | 最新季度股东人数 |
| shnc\_q1 | Number | 1个季度股东人数变化 |
| shnc\_q2 | Number | 2个季度股东人数变化 |
| shnc\_q3 | Number | 3个季度股东人数变化 |
| shnc\_y1 | Number | 1年股东人数变化 |
| shnc\_y2 | Number | 2年股东人数变化 |

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
|
|
|
|
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