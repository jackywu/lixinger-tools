# Source: https://www.lixinger.com/open/api/doc?api-key=macro/rmb-deposits

# 人民币存款[购买](/open/api/price-tier?api-groups=[{%22dataType%22:%22macro%22}])

简要描述:

* 获取人民币贷款数据，如人民币存款等。

请求URL:

* `https://open.lixinger.com/api/macro/rmb-deposits`

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
| metricsList | Yes | Array | 指标数组。如['rmb\_d']。 * 人民币存款 :rmb\_d   + y(年):     - t(累积)   + m(月):     - t(累积) * 境内存款 :rmb\_d\_d   + y(年):     - t(累积)   + m(月):     - t(累积) * 境外存款 :rmb\_o\_d   + y(年):     - t(累积)   + m(月):     - t(累积) * 住户存款 :rmb\_h\_d   + y(年):     - t(累积)   + m(月):     - t(累积) * 非金融企业存款 :rmb\_nfe\_d   + y(年):     - t(累积)   + m(月):     - t(累积) * 机关团体存款 :rmb\_gdo\_d   + y(年):     - t(累积)   + m(月):     - t(累积) * 财政性存款 :rmb\_f\_d   + y(年):     - t(累积)   + m(月):     - t(累积) * 非银行业金融机构存款 :rmb\_nbfi\_d   + y(年):     - t(累积)   + m(月):     - t(累积) * 住户活期存款 :rmb\_h\_d\_d   + y(年):     - t(累积)   + m(月):     - t(累积) * 住户定期及其他存款 :rmb\_h\_to\_d   + y(年):     - t(累积)   + m(月):     - t(累积) * 非金融企业活期存款 :rmb\_nfe\_d\_d   + y(年):     - t(累积)   + m(月):     - t(累积) * 非金融企业定期及其他存款 :rmb\_nfe\_to\_d   + y(年):     - t(累积)   + m(月):     - t(累积) |

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