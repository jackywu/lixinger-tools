# Source: https://www.lixinger.com/open/api/doc?api-key=hk/index

# 指数信息API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22hk%22,%22dataType%22:%22index%22}])

简要描述:

* 获取指数详细信息。

请求URL:

* `https://open.lixinger.com/api/hk/index`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| stockCodes | No | Array | 指数代码数组。默认值为所有指数的股票代码。格式如下：["HSI"]。 请参考[指数信息API](/open/api/detail?api-key=hk/index)获取合法的stockCode。 |

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
| name | String | 指数名称 |
| stockCode | String | 指数代码 |
| areaCode | String | 地区代码 |
| market | String | 市场 |
| fsTableType | String | 财务报表类型  * 非金融 :non\_financial * 银行 :bank * 证券 :security * 保险 :insurance * 房地产投资信托 :reit * 其他金融 :other\_financial * 混合 :hybrid |
| source | String | 指数来源  * 恒生 :hsi |
| currency | String | 货币 |
| series | String | 类型  * 规模 :size * 综合 :composite * 行业 :sector * 风格 :style * 主题 :thematic * 策略 :strategy |
| launchDate | Date | 发布时间 |
| rebalancingFrequency | String | 调样频率  * 年度 :annually * 半年 :semi-annually * 季度 :quarterly * 月度 :monthly * 不定期 :irregularly * 定期 :aperiodically |
| caculationMethod | String | 计算方式  * 派氏加权 :paasche * 分级靠档加权 :grading\_weighted * 股息率加权 :dividend\_grading * 等权 :equal * 自由流通市值加权 :free\_float\_cap * 修正资本化加权 :modified\_cap\_weighted * 流通市值加权 :negotiable\_mc\_weighted * 债券成分券流通金额加权 :circulation\_amount\_of\_constituent\_bonds |

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
|  |

加载...

加载数据失败。[请点击此处重新尝试](#!)

您需要登录才能浏览该数据，下面是图片示例：

您的会员使用时间已经到期了，下面是示例图片：

##### API试用 (剩余访问次数): **0**

* [获取所有指数信息](#!)
* [获取指定指数信息](#!)

执行

**返回数据:**