# Source: https://www.lixinger.com/open/api/doc?api-key=macro/rmb-loans

# 人民币贷款[购买](/open/api/price-tier?api-groups=[{%22dataType%22:%22macro%22}])

简要描述:

* 获取人民币贷款数据，如人民币贷款等。

请求URL:

* `https://open.lixinger.com/api/macro/rmb-loans`

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
| metricsList | Yes | Array | 指标数组。如['rmb\_l']。 * 人民币贷款 :rmb\_l   + y(年):     - t(累积)   + m(月):     - t(累积) * 境内贷款 :rmb\_d\_l   + y(年):     - t(累积)   + m(月):     - t(累积) * 海外贷款 :rmb\_o\_l   + y(年):     - t(累积)   + m(月):     - t(累积) * 住户贷款 :rmb\_h\_l   + y(年):     - t(累积)   + m(月):     - t(累积) * 住户短期贷款 :rmb\_h\_s\_l   + y(年):     - t(累积)   + m(月):     - t(累积) * 住户中长期贷款 :rmb\_h\_ml\_l   + y(年):     - t(累积)   + m(月):     - t(累积) * 企（事）业单位贷款 :rmb\_nfeg\_l   + y(年):     - t(累积)   + m(月):     - t(累积) * 企（事）业单位短期贷款 :rmb\_nfeg\_s\_l   + y(年):     - t(累积)   + m(月):     - t(累积) * 企（事）业单位中长期贷款 :rmb\_nfeg\_ml\_l   + y(年):     - t(累积)   + m(月):     - t(累积) * 企（事）业单位票据融资 :rmb\_nfeg\_p\_f   + y(年):     - t(累积)   + m(月):     - t(累积) * 企（事）业单位融资租赁 :rmb\_nfeg\_f\_l   + y(年):     - t(累积)   + m(月):     - t(累积) * 企（事）业单位各项垫款 :rmb\_nfeg\_ta\_l   + y(年):     - t(累积)   + m(月):     - t(累积) * 非银行业金融机构贷款 :rmb\_nbfo\_l   + y(年):     - t(累积)   + m(月):     - t(累积) |

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