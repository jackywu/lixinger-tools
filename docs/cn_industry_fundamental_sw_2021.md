# Source: https://www.lixinger.com/open/api/doc?api-key=cn/industry/fundamental/sw_2021

# 基本面数据API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22cn%22,%22dataType%22:%22industry%22}])

简要描述:

* 获取基本面数据，如PE、PB等。

说明:

* 指标计算请参考[行业估值计算](/wiki/stock-collection-value-calculation)

请求URL:

* `https://open.lixinger.com/api/cn/industry/fundamental/sw_2021`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| stockCodes | Yes | Array | 行业代码数组。stockCodes长度>=1且<=100，格式如下：["490000"]。 请参考[行业信息API](/open/api/detail?api-key=cn/industry)获取合法的stockCode。  需要注意的是，当传入startDate时只能传入一个股票代码。 |
| date | No | String: YYYY-MM-DD(北京时间) | 指定日期。 需要注意的是，startDate和date至少要传一个。 |
| startDate | No | String: YYYY-MM-DD(北京时间) | 信息起始时间。用于获取一定时间范围内的数据。开始和结束的时间间隔不超过10年 需要注意的是，startDate和date至少要传一个。 |
| endDate | No | String: YYYY-MM-DD(北京时间) | 信息结束时间。用于获取一定时间范围内的数据。默认值是上周一。 需要注意的是，请与startDate一起使用。 |
| limit | No | Number | 返回最近数据的数量。limit仅在请求数据为date range的情况下生效。 |
| metricsList | Yes | Array | 指标列表。例如：['mc', 'pe\_ttm.ew', 'pe\_ttm.y10.ew.cvpos’]。 **需要注意的是**，共有三种形式的指标格式：  **[metricsName].[granularity].[metricsType].[statisticsDataType]**: 支持指标有 pe\_ttm, pb, ps\_ttm, dyr(股息率)  **[metricsName].[metricsType]**: 支持指标有 dyr(股息率), pe\_ttm, pb, ps\_ttm  **[metricsName]** : 被剩余的指标支持，如 , mc(市值), tv(成交量), ta(成交金额) 当前支持: metricsName   * PE-TTM :pe\_ttm * PB :pb * PS-TTM :ps\_ttm * 股息率 :dyr * 成交金额 :ta * 换手率 :to\_r * 市值 :mc * A股市值 :mc\_om * 流通市值 :cmc * 自由流通市值 :ecmc * 融资买入金额 :fpa * 融资偿还金额 :fra * 融资净买入金额 :fnpa * 融资余额 :fb * 融券卖出金额 :ssa * 融券偿还金额 :sra * 融券净卖出金额 :snsa * 融券余额 :sb * 陆股通持仓金额 :ha\_shm * 陆股通净买入金额 :mm\_nba * 发布时间 :launchDate   granularity   * 上市以来 :fs * 20年 :y20 * 10年 :y10 * 5年 :y5 * 3年 :y3 * 1年 :y1   metricsType   * 市值加权 :mcw * 等权 :ew * 正数等权 :ewpvo * 平均值 :avg * 中位数 :median   statisticsDataType   * 当前值 :cv * 分位点% :cvpos * 最小值 :minv * 最大值 :maxv * 最大正值 :maxpv * 50%分位点值 :q5v * 80%分位点值 :q8v * 20%分位点值 :q2v * 平均值 :avgv |

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