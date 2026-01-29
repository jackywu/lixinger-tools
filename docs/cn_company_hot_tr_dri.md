# Source: https://www.lixinger.com/open/api/doc?api-key=cn/company/hot/tr_dri

# 分红再投入收益率API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22cn%22,%22dataType%22:%22company%22}])

简要描述:

* 获取分红再投入收益率数据。

说明:

* [**理杏仁采用分红再投入策略计算投资收益率**](/wiki/cagr-profit)

请求URL:

* `https://open.lixinger.com/api/cn/company/hot/tr_dri`

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
| last\_data\_date | Date | 数据时间 |
| p\_r | Number | 指定时间段投资收益率 |
| cagr\_p\_r\_fys | Number | 今年以来投资收益率 |
| cagr\_p\_r\_d7 | Number | 近7日投资收益率 |
| cagr\_p\_r\_d14 | Number | 近14日投资收益率 |
| cagr\_p\_r\_d30 | Number | 近30日投资收益率 |
| cagr\_p\_r\_d60 | Number | 近60日投资收益率 |
| cagr\_p\_r\_d90 | Number | 近90日投资收益率 |
| cagr\_p\_r\_y1 | Number | 近一年投资收益率 |
| cagr\_p\_r\_y3 | Number | 近三年年化投资收益率 |
| cagr\_p\_r\_y5 | Number | 近五年年化投资收益率 |
| cagr\_p\_r\_y10 | Number | 近十年年化投资收益率 |
| cagr\_p\_r\_y20 | Number | 近二十年年化投资收益率 |
| cagr\_p\_r\_fs | Number | 上市至今年化投资收益率 |
| p\_r\_fs | Number | 上市以来总投资收益率 |
| period\_date | Date | 投资收益率计算起始日期 |

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