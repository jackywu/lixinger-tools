# Source: https://www.lixinger.com/open/api/doc?api-key=us/index/hot/cp

# 收盘点位API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22us%22,%22dataType%22:%22index%22}])

简要描述:

* 获取收盘点位数据。

请求URL:

* `https://open.lixinger.com/api/us/index/hot/cp`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| stockCodes | Yes | Array | 指数代码数组。stockCodes长度>=1且<=100，格式如下：[".INX"]。 请参考[指数信息API](/open/api/detail?api-key=undefined)获取合法的stockCode。 |

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
| cpc | Number | 涨跌幅 |
| cpc\_fys | Number | 今年以来涨跌幅 |
| cpc\_w1 | Number | 近一周涨跌幅 |
| cpc\_w2 | Number | 近二周涨跌幅 |
| cpc\_m1 | Number | 近一月涨跌幅 |
| cpc\_m3 | Number | 近三月涨跌幅 |
| cpc\_m6 | Number | 近六月涨跌幅 |
| cpc\_y1 | Number | 近一年涨跌幅 |
| cp\_cac\_y2 | Number | 近二年年化涨跌幅 |
| cp\_cac\_y3 | Number | 近三年年化涨跌幅 |
| cp\_cac\_y5 | Number | 近五年年化涨跌幅 |
| cp\_cac\_y10 | Number | 近十年年化涨跌幅 |
| cp\_cac\_fs | Number | 发布以来年化涨跌幅 |

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