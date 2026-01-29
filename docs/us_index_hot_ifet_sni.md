# Source: https://www.lixinger.com/open/api/doc?api-key=us/index/hot/ifet_sni

# 场内基金认购净流入API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22us%22,%22dataType%22:%22index%22}])

简要描述:

* 获取场内基金认购净流入数据。

请求URL:

* `https://open.lixinger.com/api/us/index/hot/ifet_sni`

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
| ifet\_as | Number | 场内基金资产规模 |
| ifet\_sni\_ytd | Number | 过去1天场内基金认购净流入 |
| ifet\_sni\_w1 | Number | 过去1周场内基金认购净流入 |
| ifet\_sni\_w2 | Number | 过去2周场内基金认购净流入 |
| ifet\_ssni\_m1 | Number | 过去1个月场内基金认购净流入 |
| ifet\_sni\_m3 | Number | 过去3个月场内基金认购净流入 |
| ifet\_sni\_m6 | Number | 过去6个月场内基金认购净流入 |
| ifet\_sni\_y1 | Number | 过去1年场内基金认购净流入 |
| ifet\_sni\_y2 | Number | 过去2年场内基金认购净流入 |
| ifet\_sni\_fys | Number | 今年以来场内基金认购净流入 |

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
|  |

加载...

加载数据失败。[请点击此处重新尝试](#!)

您需要登录才能浏览该数据，下面是图片示例：

您的会员使用时间已经到期了，下面是示例图片：

##### API试用 (剩余访问次数): **0**

执行

**返回数据:**