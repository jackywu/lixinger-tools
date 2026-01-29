# Source: https://www.lixinger.com/open/api/doc?api-key=hk/company/hot/ss_ha

# 跨市场比价HAAPI[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22hk%22,%22dataType%22:%22company%22}])

简要描述:

* 获取跨市场比价HA数据。

请求URL:

* `https://open.lixinger.com/api/hk/company/hot/ss_ha`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| stockCodes | Yes | Array | 股票代码数组。stockCodes长度>=1且<=100，格式如下：["00700"]。 请参考[股票信息API](/open/api/detail?api-key=hk/company)获取合法的stockCode。 |

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
| last\_data\_date | Date | 数据时间 |
| ss\_cdr | Number | 最新折价率 |
| ss\_dra\_w1 | Number | 过去一个周折价率均值 |
| ss\_dra\_m1 | Number | 过去一个月折价率均值 |
| ss\_dra\_m3 | Number | 过去三个月折价率均值 |
| ss\_dra\_m6 | Number | 过去六个月折价率均值 |
| ss\_dra\_y1 | Number | 过去一年折价率均值 |
| ss\_dra\_y2 | Number | 过去两年折价率均值 |
| ss\_dra\_y3 | Number | 过去三年折价率均值 |

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
|  |

加载...

加载数据失败。[请点击此处重新尝试](#!)

您需要登录才能浏览该数据，下面是图片示例：

您的会员使用时间已经到期了，下面是示例图片：

##### API试用 (剩余访问次数): **0**

执行

**返回数据:**