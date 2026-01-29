# Source: https://www.lixinger.com/open/api/doc?api-key=hk/company/hot/mm_ah

# 互联互通API[购买](/open/api/price-tier?api-groups=[{%22areaCode%22:%22hk%22,%22dataType%22:%22company%22}])

简要描述:

* 获取互联互通数据。

说明:

* 计算股本为总H股

请求URL:

* `https://open.lixinger.com/api/hk/company/hot/mm_ah`

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
| last\_data\_date | Date | 数据时间 |
| mm\_sh | Number | 港股通持仓 |
| mm\_sha | Number | 港股通持仓金额 |
| mm\_sh\_cap\_r | Number | 港股通持仓占H股比例 |
| spc | Number | 涨跌幅 |
| mm\_sh\_nba\_d1 | Number | 港股通过去1个交易日净买入金额 |
| mm\_sh\_nba\_d5 | Number | 港股通过去5个交易日净买入金额 |
| mm\_sh\_nba\_d20 | Number | 港股通过去20个交易日净买入金额 |
| mm\_sh\_nba\_d60 | Number | 港股通过去60个交易日净买入金额 |
| mm\_sh\_nba\_d120 | Number | 港股通过去120个交易日净买入金额 |
| mm\_sh\_nba\_d240 | Number | 港股通过去240个交易日净买入金额 |
| mm\_sh\_cap\_rc\_d1 | Number | 港股通过去1个交易日持仓占H股变化比例 |
| mm\_sh\_cap\_rc\_d5 | Number | 港股通过去5个交易日持仓占H股变化比例 |
| mm\_sh\_cap\_rc\_d20 | Number | 港股通过去20个交易日持仓占H股变化比例 |
| mm\_sh\_cap\_rc\_d60 | Number | 港股通过去60个交易日持仓占H股变化比例 |
| mm\_sh\_cap\_rc\_d120 | Number | 港股通过去120个交易日持仓占H股变化比例 |
| mm\_sh\_cap\_rc\_d240 | Number | 港股通过去240个交易日持仓占H股变化比例 |
| mm\_shc\_v\_r | Number | 港股通过去1个交易日持仓变化占成交量比例 |
| mm\_shc\_v\_r\_d5 | Number | 港股通过去5个交易日持仓变化占成交量比例 |
| mm\_shc\_v\_r\_d20 | Number | 港股通过去20个交易日持仓变化占成交量比例 |
| mm\_shc\_v\_r\_d60 | Number | 港股通过去60个交易日持仓变化占成交量比例 |
| mm\_shc\_v\_r\_d120 | Number | 港股通过去120个交易日持仓变化占成交量比例 |
| mm\_shc\_v\_r\_d240 | Number | 港股通过去240个交易日持仓变化占成交量比例 |
| mm\_sh\_nbv\_d1 | Number | 港股通过去1个交易日净买入股数 |
| mm\_sh\_nbv\_d5 | Number | 港股通过去5个交易日净买入股数 |
| mm\_sh\_nbv\_d20 | Number | 港股通过去20个交易日净买入股数 |
| mm\_sh\_nbv\_d60 | Number | 港股通过去60个交易日净买入股数 |
| mm\_sh\_nbv\_d120 | Number | 港股通过去120个交易日净买入股数 |
| mm\_sh\_nbv\_d240 | Number | 港股通过去240个交易日净买入股数 |
| mm\_sh\_nbp\_d1 | Number | 港股通过去1个交易日净买入收益 |
| mm\_sh\_nbp\_d5 | Number | 港股通过去5个交易日净买入收益 |
| mm\_sh\_nbp\_d20 | Number | 港股通过去20个交易日净买入收益 |
| mm\_sh\_nbp\_d60 | Number | 港股通过去60个交易日净买入收益 |
| mm\_sh\_nbp\_d120 | Number | 港股通过去120个交易日净买入收益 |
| mm\_sh\_nbp\_d240 | Number | 港股通过去240个交易日净买入收益 |
| mm\_sh\_nbpr\_d1 | Number | 港股通过去1个交易日净买入收益率 |
| mm\_sh\_nbpr\_d5 | Number | 港股通过去5个交易日净买入收益率 |
| mm\_sh\_nbpr\_d20 | Number | 港股通过去20个交易日净买入收益率 |
| mm\_sh\_nbpr\_d60 | Number | 港股通过去60个交易日净买入收益率 |
| mm\_sh\_nbpr\_d120 | Number | 港股通过去120个交易日净买入收益率 |
| mm\_sh\_nbpr\_d240 | Number | 港股通过去240个交易日净买入收益率 |

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