# Source: https://www.lixinger.com/open/api/doc?api-key=hk/company/profile

# 公司概况API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22hk%22,%22dataType%22:%22company%22}])

简要描述:

* 获取公司概况数据

请求URL:

* `https://open.lixinger.com/api/hk/company/profile`

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
| listingDate | Date | 上市日期 |
| chairman | String | 董事长 |
| classAdescription | String | A股 |
| classBdescription | String | B股 |
| capitalStructureClassA | Number | A股股本结构 |
| capitalStructureClassB | Number | B股股本结构 |
| fiscalYearEnd | Date | 财政年度结算日期 |
| summary | String | 公司概况 |
| listingCategory | String | 上市类型 |
| registrar | String | 过户处 |
| website | String | 公司网址 |
| registeredAddress | String | 注册地址 |
| officeAddress | String | 办公地址 |

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
|  |

加载...

加载数据失败。[请点击此处重新尝试](#!)

您需要登录才能浏览该数据，下面是图片示例：

您的会员使用时间已经到期了，下面是示例图片：

##### API试用 (剩余访问次数): **0**

执行

**返回数据:**