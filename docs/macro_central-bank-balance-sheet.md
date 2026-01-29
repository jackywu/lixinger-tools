# Source: https://www.lixinger.com/open/api/doc?api-key=macro/central-bank-balance-sheet

# 央行资产负债表API[购买](/open/api/price-tier?api-groups=[{%22dataType%22:%22macro%22}])

简要描述:

* 获取央行资产负债表数据，如总资产等。

请求URL:

* `https://open.lixinger.com/api/macro/central-bank-balance-sheet`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| startDate | Yes | String: YYYY-MM-DD(北京时间) | 信息起始时间。开始和结束的时间间隔不超过10年 |
| endDate | Yes | String: YYYY-MM-DD(北京时间) | 信息结束时间。 |
| limit | No | Number | 返回最近数据的数量。limit仅在请求数据为date range的情况下生效。 |
| areaCode | Yes | String | 区域编码，如{areaCode}。当前支持:  * 大陆: cn |
| metricsList | Yes | Array | 指标数组。如['t\_a']。 * 总资产 :t\_a   + y(年):     - t(累积)   + m(月):     - t(累积) * 国外资产 :f\_a   + y(年):     - t(累积)   + m(月):     - t(累积) * 对政府债权 :c\_o\_g   + y(年):     - t(累积)   + m(月):     - t(累积) * 对其他存款性公司债权 :c\_o\_odc   + y(年):     - t(累积)   + m(月):     - t(累积) * 对其他金融性公司债权 :c\_o\_ofc   + y(年):     - t(累积)   + m(月):     - t(累积) * 对非金融性公司债权 :c\_o\_onfc   + y(年):     - t(累积)   + m(月):     - t(累积) * 其他资产 :o\_a   + y(年):     - t(累积)   + m(月):     - t(累积) * 储备货币 :r\_m   + y(年):     - t(累积)   + m(月):     - t(累积) * 不计入储备货币的金融性公司存款 :d\_o\_fc\_ef\_rm   + y(年):     - t(累积)   + m(月):     - t(累积) * 发行债券 :b\_i   + y(年):     - t(累积)   + m(月):     - t(累积) * 国外负债 :f\_l   + y(年):     - t(累积)   + m(月):     - t(累积) * 政府存款 :d\_o\_g   + y(年):     - t(累积)   + m(月):     - t(累积) * 自有资金 :o\_c   + y(年):     - t(累积)   + m(月):     - t(累积) * 其他负债 :o\_lia   + y(年):     - t(累积)   + m(月):     - t(累积) |

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

加载...

加载数据失败。[请点击此处重新尝试](#!)

您需要登录才能浏览该数据，下面是图片示例：

您的会员使用时间已经到期了，下面是示例图片：

##### API试用 (剩余访问次数): **0**

执行

**返回数据:**