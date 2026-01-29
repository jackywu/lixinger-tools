# Source: https://www.lixinger.com/open/api/doc?api-key=hk/company/industries

# 股票所属行业信息API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22hk%22,%22dataType%22:%22company%22}])

简要描述:

* 获取股票所属行业信息。

请求URL:

* `https://open.lixinger.com/api/hk/company/industries`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| stockCode | Yes | String | 股票代码请参考[股票信息API](/open/api/detail?api-key=hk/company)获取合法的stockCode。 |
| date | No | String: YYYY-MM-DD(北京时间) | 信息时间。默认值是当前最新时间。 |

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
|  |

**返回数据说明:** 

| 参数名称 | 数据类型 | 说明 |
| --- | --- | --- |
| name | String | 行业名称 |
| areaCode | String | 地区代码 |
| stockCode | String | 行业代码 |
| source | String | 行业来源  * 申万 :sw * 申万2021版 :sw\_2021 * 国证 :cni |

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
|  |

加载...

加载数据失败。[请点击此处重新尝试](#!)

您需要登录才能浏览该数据，下面是图片示例：

您的会员使用时间已经到期了，下面是示例图片：

##### API试用 (剩余访问次数): **0**

* [获取最新时间股票所属行业信息](#!)
* [获取指定日期股票所属行业信息](#!)

执行

**返回数据:**