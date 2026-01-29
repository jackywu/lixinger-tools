# Source: https://www.lixinger.com/open/api/doc?api-key=us/index/fs/non_financial

# 财报数据API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22us%22,%22dataType%22:%22index%22}])

简要描述:

* 获取财务数据，如营业收入、ROE等。

说明:

* 指标计算请参考[指数财务数据计算](/wiki/stock-collection-fs-calculation)

请求URL:

* `https://open.lixinger.com/api/us/index/fs/non_financial`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| stockCodes | Yes | Array | 指数代码数组。stockCodes长度>=1且<=100，格式如下：[".INX"]。 请参考[指数信息API](/open/api/detail?api-key=undefined)获取合法的stockCode。  需要注意的是，当传入startDate时只能传入一个股票代码。 |
| date | No | String: latest | YYYY-MM-DD(北京时间) | 信息日期。用于获取指定日期数据。 由于每个季度的最后一天为财报日，请确保传入正确的日期，例如：2017-03-31、2017-06-30、2017-09-30、2017-12-31 或 latest。  其中，传入**latest**会得到最近1.1年内的最新财报数据。  需要注意的是，startDate和date至少要传一个。 |
| startDate | No | String: YYYY-MM-DD(北京时间) | 信息起始时间。用于获取一定时间范围内的数据。开始和结束的时间间隔不超过10年 需要注意的是，startDate和date至少要传一个。 |
| endDate | No | String: YYYY-MM-DD(北京时间) | 信息结束时间。用于获取一定时间范围内的数据。默认值是上周一。 需要注意的是，请与startDate一起使用。 |
| limit | No | Number | 返回最近数据的数量。limit仅在请求数据为date range的情况下生效。 |
| metricsList | Yes | Array | 指标数组，指标格式为**[granularity].[tableName].[fieldName].[expressionCalculateType]**。比如，你想获取营业总收入累计原始值以及应收账款当期同比值，对应的metricsList设置为：["q.ps.toi.t", "q.bs.ar.c\_y2y"]。 需要注意的是，当stockCodes长度大于1时最多只能选取48个指标；当stockCodes长度等于1时最多只能获取128 个指标。 当前支持: granularity   * 年 :y * 半年 :hy * 季度 :q   expressionCalculateType   * 资产负债表:   + 年(y):     - 当期 :t     - 当期同比 :t\_y2y     - TTM环比 :ttm\_c2c   + 半年(hy):     - 当期 :t     - 当期原始值 :t\_o     - 当期同比 :t\_y2y     - 当期环比 :t\_c2c     - 半年 :c     - 半年原始值 :c\_o     - 半年同比 :c\_y2y     - 半年环比 :c\_c2c   + 季度(q):     - 当期 :t     - 当期原始值 :t\_o     - 当期同比 :t\_y2y     - 当期环比 :t\_c2c     - 单季 :c     - 单季原始值 :c\_o     - 单季同比 :c\_y2y     - 单季环比 :c\_c2c * 利润表:   + 年(y):     - 累积 :t     - 累积原始值 :t\_o     - 累积同比 :t\_y2y   + 半年(hy):     - 累积 :t     - 累积原始值 :t\_o     - 累积同比 :t\_y2y     - 累积环比 :t\_c2c     - 半年 :c     - 半年原始值 :c\_o     - 半年同比 :c\_y2y     - 半年环比 :c\_c2c     - 半年年比 :c\_2y     - TTM :ttm     - TTM原始值 :ttm\_o     - TTM同比 :ttm\_y2y     - TTM环比 :ttm\_c2c   + 季度(q):     - 累积 :t     - 累积原始值 :t\_o     - 累积同比 :t\_y2y     - 累积环比 :t\_c2c     - 单季 :c     - 单季原始值 :c\_o     - 单季同比 :c\_y2y     - 单季环比 :c\_c2c     - 单季年比 :c\_2y     - TTM :ttm     - TTM原始值 :ttm\_o     - TTM同比 :ttm\_y2y     - TTM环比 :ttm\_c2c * 现金流量表:   + 年(y):     - 累积 :t     - 累积原始值 :t\_o     - 累积同比 :t\_y2y   + 半年(hy):     - 累积 :t     - 累积原始值 :t\_o     - 累积同比 :t\_y2y     - 累积环比 :t\_c2c     - 半年 :c     - 半年原始值 :c\_o     - 半年同比 :c\_y2y     - 半年环比 :c\_c2c     - 半年年比 :c\_2y     - TTM :ttm     - TTM原始值 :ttm\_o     - TTM同比 :ttm\_y2y     - TTM环比 :ttm\_c2c   + 季度(q):     - 累积 :t     - 累积原始值 :t\_o     - 累积同比 :t\_y2y     - 累积环比 :t\_c2c     - 单季 :c     - 单季原始值 :c\_o     - 单季同比 :c\_y2y     - 单季环比 :c\_c2c     - 单季年比 :c\_2y     - TTM :ttm     - TTM原始值 :ttm\_o     - TTM同比 :ttm\_y2y     - TTM环比 :ttm\_c2c   tableName.fieldName     * 资产负债表   + 一、资产总计 : bs.ta   + 流动资产合计 : bs.tca   + 流动资产占比 : bs.tca\_ta\_r   + 货币资金 : bs.cabb   + 货币资金占比 : bs.cabb\_ta\_r   + 可供出售金融资产(流动) : bs.cafsfa   + 应收账款 : bs.ar   + 存货 : bs.i   + 非流动资产合计 : bs.tnca   + 非流动资产占比 : bs.tnca\_ta\_r   + 可供出售金融资产(非流动) : bs.ncafsfa   + 物业、厂房及设备 : bs.ppe   + 商誉及无形资产 : bs.gwaia   + 二、负债合计 : bs.tl   + 资产负债率 : bs.tl\_ta\_r   + 流动负债合计 : bs.tcl   + 流动负债占比 : bs.tcl\_tl\_r   + 应付账款 : bs.ap   + 递延收益 : bs.drev   + 非流动负债合计 : bs.tncl   + 非流动负债占比 : bs.tncl\_tl\_r   + 递延所得税负债 : bs.ditl   + 三、所有者权益合计 : bs.toe   + 股东权益占比 : bs.toe\_ta\_r   + 未分配利润 : bs.rtp   + 其他综合收益 : bs.oci   + 归属于母公司普通股股东权益合计 : bs.tetoshopc   + 四、股本、股东以及估值   + 市值 : bs.mc   + 总股本 : bs.tsc  * 利润表   + 一、营业总收入 : ps.toi   + 营业收入 : ps.oi   + 营业成本 : ps.oc   + 毛利率(GM) : ps.gp\_m   + 销售及行政开支 : ps.sgnae   + 研发费用 : ps.rade   + 研发费用率 : ps.rade\_r   + 利息费用 : ps.ieife   + 二、利润总额 : ps.tp   + 所得税费用 : ps.ite   + 有效税率 : ps.ite\_tp\_r   + 研发费占利润总额比值 : ps.rade\_tp\_r   + 三、净利润 : ps.np   + 净利润率 : ps.np\_s\_r   + 归属于母公司股东及其他权益持有者的净利润 : ps.npatshaoehopc   + 归属于母公司普通股股东的净利润 : ps.npatoshopc   + 少数股东损益 : ps.npatmsh   + 五、分红及涨跌幅   + 分红金额 : ps.da  * 现金流量表   + 一、经营活动产生的现金流量净额 : cfs.ncffoa   + 业务收购支付的相关现金 : cfs.ncpicwba   + 二、投资活动产生的现金流量净额 : cfs.ncffia   + 三、筹资活动产生的现金流量净额 : cfs.ncfffa   + 支付股息支付的现金 : cfs.cpfd   + 四、现金及现金等价物的净增加额 : cfs.niicace   + 汇率变动对现金及现金等价物的影响 : cfs.iocacedtfier   + 五、附注   + 股份酬金支出 : cfs.sbce   + 折旧及摊销 : cfs.daa  * 财务指标   + 一、每股指标   + 总股本 : m.tsc (expressionCalculateType参考资产负债表)   + 归属于母公司普通股股东的每股收益 : m.npatoshopc\_ps (expressionCalculateType参考利润表)   + 归属于母公司普通股股东的每股股东权益 : m.tetoshopc\_ps (expressionCalculateType参考资产负债表)   + 每股未分配利润 : m.rp\_ps (expressionCalculateType参考资产负债表)   + 每股分红 : m.da\_ps (expressionCalculateType参考利润表)   + 每股经营活动产生的现金流量净额 : m.ncffoa\_ps (expressionCalculateType参考现金流量表)   + 二、盈利能力   + 归属于母公司普通股股东的ROE : m.roe\_atoshaopc (expressionCalculateType参考利润表)   + 净资产收益率(ROE) : m.roe (expressionCalculateType参考利润表)   + 杠杆倍数 : m.l (expressionCalculateType参考资产负债表)   + 总资产收益率(ROA) : m.roa (expressionCalculateType参考利润表)   + 总资产周转率 : m.ta\_to (expressionCalculateType参考利润表)   + 净利润率 : m.np\_s\_r (expressionCalculateType参考利润表)   + 毛利率(GM) : m.gp\_m (expressionCalculateType参考利润表)   + 三、营运能力(周转率)   + 存货周转率 : m.i\_tor (expressionCalculateType参考利润表)   + 应收账款周转率 : m.ar\_tor (expressionCalculateType参考利润表)   + 应付账款周转率 : m.ap\_tor (expressionCalculateType参考利润表)   + 不动产、厂房及设备周转率 : m.ppe\_tor (expressionCalculateType参考利润表)   + 四、营运能力(周转天数)   + 存货周转天数 : m.i\_ds (expressionCalculateType参考利润表)   + 应收账款周转天数 : m.ar\_ds (expressionCalculateType参考利润表)   + 应付账款周转天数 : m.ap\_ds (expressionCalculateType参考利润表)   + 不动产、厂房及设备周转天数 : m.ppe\_ds (expressionCalculateType参考利润表)   + 流动资产周转天数 : m.tca\_ds (expressionCalculateType参考利润表)   + 股东权益周转天数 : m.toe\_ds (expressionCalculateType参考利润表)   + 五、偿债及资本结构   + 资产负债率 : m.tl\_ta\_r (expressionCalculateType参考资产负债表)   + 货币资金占流动负债比率 : m.cabb\_tcl\_r (expressionCalculateType参考资产负债表)   + 流动比率 : m.c\_r (expressionCalculateType参考资产负债表)   + 不动产、厂房及设备占总资产比率 : m.ppe\_ta\_r (expressionCalculateType参考资产负债表)   + 六、现金流量   + 经投融产生的现金流量净额 : m.ncffoaiafa (expressionCalculateType参考现金流量表)   + 经营活动产生的现金流量净额对净利润的比率 : m.ncffoa\_np\_r (expressionCalculateType参考利润表) |

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

|
|  |

加载...

加载数据失败。[请点击此处重新尝试](#!)

您需要登录才能浏览该数据，下面是图片示例：

您的会员使用时间已经到期了，下面是示例图片：

##### API试用 (剩余访问次数): **0**

* [通过日期获取](#!)
* [通过时间范围获取](#!)

执行

**返回数据:**