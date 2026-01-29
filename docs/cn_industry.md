# Source: https://www.lixinger.com/open/api/doc?api-key=cn/industry

# 股票信息API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22cn%22,%22dataType%22:%22industry%22}])

简要描述:

* 获取股票详细信息。

请求URL:

* `https://open.lixinger.com/api/cn/industry`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| stockCodes | No | Array | 行业代码数组。默认值为所有行业的股票代码。格式如下：["490000"]。 请参考[行业信息API](/open/api/detail?api-key=cn/industry)获取合法的stockCode。 |
| source | Yes | String | 行业来源，例如：{source}。当前支持:  * 申万: sw * 申万2021版: sw\_2021 * 国证: cni |
| level | No | String | 行业分类级别，例如：'one'。当前支持:  * 一级: one * 二级: two * 三级: three |

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
|  |

**返回数据说明:** 

| 参数名称 | 数据类型 | 说明 |
| --- | --- | --- |
| stockCode | String | 行业代码 |
| name | String | 行业名称 |
| launchDate | Date | 发布时间 |
| areaCode | String | 地区代码 |
| market | String | 市场 |
| fsTableType | String | 财务报表类型  * 非金融 :non\_financial * 银行 :bank * 证券 :security * 保险 :insurance * 房地产投资信托 :reit * 其他金融 :other\_financial * 混合 :hybrid |
| level | String | 行业分类等级 |
| source | String | 行业来源  * 国证 :cni * 申万 :sw * 申万2021版 :sw\_2021 |
| currency | String | 货币 |

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
|  |

加载...

加载数据失败。[请点击此处重新尝试](#!)

您需要登录才能浏览该数据，下面是图片示例：

您的会员使用时间已经到期了，下面是示例图片：

##### API试用 (剩余访问次数): **0**

* [获取指定行业信息](#!)
* [获取指定分类级别的所有行业信息](#!)

执行

**返回数据:**