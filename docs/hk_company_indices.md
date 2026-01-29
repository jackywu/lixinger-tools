# Source: https://www.lixinger.com/open/api/doc?api-key=hk/company/indices

# 股票所属指数信息API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22hk%22,%22dataType%22:%22company%22}])

简要描述:

* 获取股票所属指数信息。

请求URL:

* `https://open.lixinger.com/api/hk/company/indices`

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
| name | String | 指数名称 |
| areaCode | String | 地区代码 |
| stockCode | String | 指数代码 |
| source | String | 指数来源  * 中证 :csi * 国证 :cni * 恒生 :hsi * 美指 :usi * 理杏仁 :lxri |

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

* [获取最新时间股票所属指数信息](#!)
* [获取指定日期股票所属指数信息](#!)

执行

**返回数据:**