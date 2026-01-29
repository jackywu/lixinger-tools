# Source: https://www.lixinger.com/open/api/doc?api-key=cn/company/hot/mm_ha

# 互联互通API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22cn%22,%22dataType%22:%22company%22}])

简要描述:

* 获取互联互通数据。

说明:

* 计算股本为流通A股

请求URL:

* `https://open.lixinger.com/api/cn/company/hot/mm_ha`

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
| mm\_sh | Number | 陆股通持仓 |
| mm\_sha | Number | 陆股通持仓金额 |
| mm\_sh\_cap\_r | Number | 陆股通持股占流通A股比例 |
| spc | Number | 涨跌幅 |
| mm\_sh\_nba\_q1 | Number | 陆股通过去1个季度净买入金额 |
| mm\_sh\_nba\_q2 | Number | 陆股通过去2个季度净买入金额 |
| mm\_sh\_nba\_q3 | Number | 陆股通过去3个季度净买入金额 |
| mm\_sh\_nba\_q4 | Number | 陆股通过去4个季度净买入金额 |
| mm\_sh\_cap\_rc\_q1 | Number | 陆股通过去1个季度持仓占流通A股比例 |
| mm\_sh\_cap\_rc\_q2 | Number | 陆股通过去2个季度持仓占流通A股比例 |
| mm\_sh\_cap\_rc\_q3 | Number | 陆股通过去3个季度持仓占流通A股比例 |
| mm\_sh\_cap\_rc\_q4 | Number | 陆股通过去4个季度持仓占流通A股比例 |
| mm\_sh\_nbv\_q1 | Number | 陆股通过去1个季度净买入股数 |
| mm\_sh\_nbv\_q2 | Number | 陆股通过去2个季度净买入股数 |
| mm\_sh\_nbv\_q3 | Number | 陆股通过去3个季度净买入股数 |
| mm\_sh\_nbv\_q4 | Number | 陆股通过去4个季度净买入股数 |

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

|
|  |

加载...

加载数据失败。[请点击此处重新尝试](#!)

您需要登录才能浏览该数据，下面是图片示例：

您的会员使用时间已经到期了，下面是示例图片：

##### API试用 (剩余访问次数): **0**

执行

**返回数据:**