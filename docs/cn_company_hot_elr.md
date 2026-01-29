# Source: https://www.lixinger.com/open/api/doc?api-key=cn/company/hot/elr

# 限售解禁API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22cn%22,%22dataType%22:%22company%22}])

简要描述:

* 获取限售解禁数据。

请求URL:

* `https://open.lixinger.com/api/cn/company/hot/elr`

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
| last\_data\_date | Date | 最近一期预计解除限售时间 |
| srl\_last | Number | 最近预计解除限售股数 |
| srl\_cap\_r\_last | Number | 最近预计解除限售股数占总股本比例 |
| elr\_s\_y1 | Number | 未来一年预计解除限售股数 |
| elr\_s\_cap\_r\_y1 | Number | 未来一年预计解除限售股数占总股本比例 |
| elr\_mc\_y1 | Number | 未来一年预计解除限售市值 |

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
|  |

加载...

加载数据失败。[请点击此处重新尝试](#!)

您需要登录才能浏览该数据，下面是图片示例：

您的会员使用时间已经到期了，下面是示例图片：

##### API试用 (剩余访问次数): **0**

执行

**返回数据:**