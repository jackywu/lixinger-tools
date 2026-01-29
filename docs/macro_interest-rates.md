# Source: https://www.lixinger.com/open/api/doc?api-key=macro/interest-rates

# 利率API[购买](/open/api/price-tier?api-groups=[{%22dataType%22:%22macro%22}])

简要描述:

* 获取利率数据，如活期存款等。

请求URL:

* `https://open.lixinger.com/api/macro/interest-rates`

请求方式:

* POST

参数:

| 参数名称 | 必选 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| token | Yes | String | [我的Token](/open/api/token)页有用户专属且唯一的Token。 |
| startDate | Yes | String: YYYY-MM-DD(北京时间) | 信息起始时间。开始和结束的时间间隔不超过10年 |
| endDate | Yes | String: YYYY-MM-DD(北京时间) | 信息结束时间。 |
| limit | No | Number | 返回最近数据的数量。limit仅在请求数据为date range的情况下生效。 |
| areaCode | Yes | String | 区域编码，如{areaCode}。当前支持:  * 大陆: cn * 香港: hk * 美国: us |
| metricsList | Yes | Array | 指标数组。如['rmb\_bdirofi\_d']。 大陆支持:  * 活期存款 :rmb\_bdirofi\_d * 定期存款（三个月） :rmb\_bdirofi\_m3 * 定期存款（半年） :rmb\_bdirofi\_hy * 定期存款（一年） :rmb\_bdirofi\_y1 * 定期存款（两年） :rmb\_bdirofi\_y2 * 定期存款（三年） :rmb\_bdirofi\_y3 * 定期存款（五年） :rmb\_bdirofi\_y5 * 贷款：六个月以内（含六个月） :rmb\_blrofi\_wm6 * 贷款：一年以内（含一年） :rmb\_blrofi\_wy1 * 贷款：六个月至一年（含一年） :rmb\_blrofi\_m6ty1 * 贷款：一至三年（含三年） :rmb\_blrofi\_y1ty3 * 贷款：三至五年（含五年） :rmb\_blrofi\_y3ty5 * 贷款：一至五年（含五年） :rmb\_blrofi\_y1ty5 * 贷款：五年以上 :rmb\_blrofi\_mty5 * 一年期LRP :lpr\_y1 * 五年及以上LPR :lpr\_y5 * 三个月期MLF利率 :mlf\_m3\_r * 六个月期MLF利率 :mlf\_m6\_r * 一年期MLF利率 :mlf\_y1\_r * 1个周Shibor :shibor\_w1 * 2个周Shibor :shibor\_w2 * 1个月Shibor :shibor\_m1 * 3个月Shibor :shibor\_m3 * 6个月Shibor :shibor\_m6 * 9个月Shibor :shibor\_m9 * 1年Shibor :shibor\_y1 * 隔夜Shibor :shibor\_on * 中债商业银行同业存单(AAA)隔夜收益率 :cdnaaa\_d1 * 中债商业银行同业存单(AAA)1周收益率 :cdnaaa\_w1 * 中债商业银行同业存单(AAA)1个月收益率 :cdnaaa\_m1 * 中债商业银行同业存单(AAA)6个月收益率 :cdnaaa\_m6 * 中债商业银行同业存单(AAA)1年收益率 :cdnaaa\_y1 * 隔夜回购定盘利率(FR001) :fr\_d1 * 七天回购定盘利率(FR007) :fr\_d7 * 十四天回购定盘利率(FR014) :fr\_d14 * 银银间隔夜回购定盘利率(FDR001) :fdr\_d1 * 银银间七天回购定盘利率(FDR007) :fdr\_d7 * 银银间十四天回购定盘利率(FDR014) :fdr\_d14  美国支持:  * 联邦基金（有效） :eff * 金融商业票据：1个月 :fcp\_m1 * 金融商业票据：2个月 :fcp\_m2 * 金融商业票据：3个月 :fcp\_m3 * 非金融商业票据：1个月 :nfcp\_m1 * 非金融商业票据：2个月 :nfcp\_m2 * 非金融商业票据：3个月 :nfcp\_m3 * 银行优惠贷款 :bpl * 贴现窗主要信贷 :dwpc * 国库券（二级市场）：4周 :smtb\_w4 * 国库券（二级市场）：3个月 :smtb\_m3 * 国库券（二级市场）：6个月 :smtb\_m6 * 国库券（二级市场）：1年 :smtb\_y1 * 通货膨胀指数：5年 :ii\_y5 * 通货膨胀指数：7年 :ii\_y7 * 通货膨胀指数：10年 :ii\_y10 * 通货膨胀指数：20年 :ii\_y20 * 通货膨胀指数：30年 :ii\_y30 * 通货膨胀指数长期平均值 :ltavg  香港支持:  * 1周Hibor :hibor\_w1 * 2周Hibor :hibor\_w2 * 1个月Hibor :hibor\_m1 * 3个月Hibor :hibor\_m3 * 6个月Hibor :hibor\_m6 * 9个月Hibor :hibor\_m9 * 1年Hibor :hibor\_y1 * 隔夜Hibor :hibor\_on |

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