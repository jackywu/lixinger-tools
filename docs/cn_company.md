# Source: https://www.lixinger.com/open/api/doc?api-key=cn/company

# 股票信息API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22cn%22,%22dataType%22:%22company%22}])

简要描述:

* 获取股票详细信息。

请求URL:

* `https://open.lixinger.com/api/cn/company`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| stockCodes | No | Array | 股票代码数组。默认值为所有股票代码。格式如下：["300750","600519","600157"]。 请参考[股票信息API](/open/api/detail?api-key=cn/company)获取合法的stockCode。 |
| fsTableType | No | String | 财报类型，比如，'bank'。当前支持:  * 非金融: non\_financial * 银行: bank * 保险: insurance * 证券: security * 其他金融: other\_financial |
| mutualMarkets | No | Array | 互联互通类型，比如：'[ha]'。当前支持:陆股通: ha |
| includeDelisted | No | Boolean | 是否包含退市股。 默认值是false。 |
| pageIndex | Yes | Number | 页面索引。 默认值是0。 |

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

**返回数据说明:** 

| 参数名称 | 数据类型 | 说明 |
| --- | --- | --- |
| total | Number | 公司总数 |
| name | String | 公司名称 |
| stockCode | String | 股票代码 |
| areaCode | String | 地区代码 |
| market | String | 市场 |
| exchange | String | 交易所 |
| fsTableType | String | 财报类型 |
| mutualMarkets | String | 互联互通 |
| mutualMarketFlag | Boolean | 是否是互联互通标的 |
| marginTradingAndSecuritiesLendingFlag | Boolean | 是否是融资融券标的 |
| ipoDate | Date | 上市时间 |
| delistedDate | Date | 退市时间 |

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
|  |

加载...

加载数据失败。[请点击此处重新尝试](#!)

您需要登录才能浏览该数据，下面是图片示例：

您的会员使用时间已经到期了，下面是示例图片：

##### API试用 (剩余访问次数): **0**

* [获取所有股票信息](#!)
* [获取指定财报类型的所有股票信息](#!)
* [获取指定股票信息](#!)
* [获取陆股通股票数据。](#!)

执行

**返回数据:**