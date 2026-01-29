# Source: https://www.lixinger.com/open/api/doc?api-key=cn/industry/hot/mm_ha/sw_2021

# 互联互通API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22cn%22,%22dataType%22:%22industry%22}])

简要描述:

* 获取互联互通数据。

请求URL:

* `https://open.lixinger.com/api/cn/industry/hot/mm_ha/sw_2021`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| stockCodes | Yes | Array | 行业代码数组。stockCodes长度>=1且<=100，格式如下：["490000"]。 请参考[行业信息API](/open/api/detail?api-key=cn/industry)获取合法的stockCode。 |

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
| mm\_sha | Number | 陆股通持仓金额 |
| mm\_sha\_mc\_r | Number | 陆股通持仓金额占市值比例 |
| mm\_sh\_nba\_q1 | Number | 陆股通过去1个季度净买入金额 |
| mm\_sh\_nba\_q2 | Number | 陆股通过去2个季度净买入金额 |
| mm\_sh\_nba\_q3 | Number | 陆股通过去3个季度净买入金额 |
| mm\_sh\_nba\_q4 | Number | 陆股通过去4个季度净买入金额 |
| mm\_sha\_mc\_rc\_q1 | Number | 陆股通过去1个季度持股金额占市值变化比例 |
| mm\_sha\_mc\_rc\_q2 | Number | 陆股通过去2个季度持股金额占市值变化比例 |
| mm\_sha\_mc\_rc\_q3 | Number | 陆股通过去3个季度持股金额占市值变化比例 |
| mm\_sha\_mc\_rc\_q4 | Number | 陆股通过去4个季度持股金额占市值变化比例 |

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

执行

**返回数据:**