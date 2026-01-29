# Source: https://www.lixinger.com/open/api/doc?api-key=hk/company/hot/director_equity_change

# 董事权益变动API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22hk%22,%22dataType%22:%22company%22}])

简要描述:

* 获取董事权益变动数据。

请求URL:

* `https://open.lixinger.com/api/hk/company/hot/director_equity_change`

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
| dec\_a\_last | Number | 最新董事权益变动金额 |
| dec\_cap\_rc\_last | Number | 最新董事权益变动占H股比例 |
| dec\_a\_m1 | Number | 过去1个月累计董事权益变动金额 |
| dec\_a\_m3 | Number | 过去3个月累计董事权益变动金额 |
| dec\_a\_m6 | Number | 过去6个月累计董事权益变动金额 |
| dec\_a\_y1 | Number | 过去1年累计董事权益变动金额 |
| dec\_a\_y2 | Number | 过去2年累计董事权益变动金额 |
| dec\_a\_y3 | Number | 过去3年累计董事权益变动金额 |
| dec\_cap\_rc\_m1 | Number | 过去1个月累计董事权益变动占H股 |
| dec\_cap\_rc\_m3 | Number | 过去3个月累计董事权益变动占H股 |
| dec\_cap\_rc\_m6 | Number | 过去6个月累计董事权益变动占H股 |
| dec\_cap\_rc\_y1 | Number | 过去1年累计董事权益变动占H股 |
| dec\_cap\_rc\_y2 | Number | 过去2年累计董事权益变动占H股 |
| dec\_cap\_rc\_y3 | Number | 过去3年累计董事权益变动占H股 |

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
|  |

加载...

加载数据失败。[请点击此处重新尝试](#!)

您需要登录才能浏览该数据，下面是图片示例：

您的会员使用时间已经到期了，下面是示例图片：

##### API试用 (剩余访问次数): **0**

执行

**返回数据:**