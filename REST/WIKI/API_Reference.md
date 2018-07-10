## 市场行情(不需要apikey)
### 网络测试
* GET https://api.coinpark.cc/v1/public?cmd=ping
```
返回结果：
{
    "result": {},
    "cmd":"ping"
}
```

### 查询交易对    def get_symbols(self):
* GET https://api.coinpark.cc/v1/mdata?cmd=pairList
* POST https://api.coinpark.cc/v1/mdata
```
请求参数：
cmd: "api/pairList"
body: {
}

返回结果：
{
    "result":[
        {"id":1,"pair":"BIX_BTC"},
        {"id":2,"pair":"CP_BTC"},
        ...
    ],
    "cmd":"api/pairList"
}
```
### 查询k线    def get_kline(self, symbol, period, size=1000):
* GET https://api.coinpark.cc/v1/mdata?cmd=kline&pair=BIX_BTC&period=1min&size=10
* POST https://api.coinpark.cc/v1/mdata
```
请求参数：
cmd: "api/kline"
body: {
    pair,       //交易对，如BIX_BTC
    period,     //k线周期，取值 ['1min', '3min', '5min', '15min', '30min', '1hour', '2hour', '4hour', '6hour', '12hour', 'day', 'week']
    size,       //要几条，1-1000，不传返回1000
}

返回结果：
{
    "result":[
        {
            "time":1512660420000,
            "open":"0.00586568",
            "high":"0.00586568",
            "low":"0.00586568",
            "close":"0.00586568",
            "vol":"0"
        },
        {
            "time":1512660480000,
            "open":"0.00586568",
            "high":"0.00586568",
            "low":"0.00586568",
            "close":"0.00586568",
            "vol":"10"
        }
    ],
    "cmd":"api/kline"
}
```
### 查询全币种市场行情    def get_allmakret(self):
* GET https://api.coinpark.cc/v1/mdata?cmd=marketAll
* POST https://api.coinpark.cc/v1/mdata
```
请求参数：
cmd: "api/marketAll"
body: {
}

返回结果：
{
    "result":[
        {
            "id":4,
            "coin_symbol":"BIX",
            "currency_symbol":"BTC",
            "last":"0.00002704",
            "high":"0.00003480",
            "low":"0.00001951",
            "change":"+0.00000715",
            "percent":"+35.95%",
            "vol24H":"641954",
            "amount":"16.55",
            "last_cny":"1.84",
            "high_cny":"2.37",
            "low_cny":"1.33",
            "last_usd":"0.27",
            "high_usd":"0.35",
            "low_usd":"0.19"
        },
        {
            "id":5,
            "coin_symbol":"ETH",
            "currency_symbol":"BTC",
            "last":"0.04341296",
            "high":"0.04884176",
            "low":"0.04321405",
            "change":"-0.00047878",
            "percent":"-1.09%",
            "vol24H":"86",
            "amount":"3.77",
            "last_cny":"2950.87",
            "high_cny":"3319.88",
            "low_cny":"2937.35",
            "last_usd":"432.60",
            "high_usd":"486.70",
            "low_usd":"430.62"
        }
    ],
    "cmd":"api/marketAll"
}
```
### 查询单币种市场行情    def get_market(self, symbol):
* GET https://api.coinpark.cc/v1/mdata?cmd=market&pair=BIX_BTC
* POST https://api.coinpark.cc/v1/mdata
```
请求参数：
cmd: "api/market"
body: {
    pair,       //交易对，如BIX_BTC
}

返回结果：
{
    "result":{
        "id":4,
        "coin_symbol":"BIX",            //交易币种
        "currency_symbol":"BTC",        //定价币种
        "last":"0.00002704",            //最新价
        "high":"0.00003480",
        "low":"0.00001951",
        "change":"+0.00000715",         //24h涨跌
        "percent":"+35.95%",            //24h涨跌幅
        "vol24H":"641954",              //24h成交量
        "amount":"16.55",               //24h成交额
        "last_cny":"1.84",              //最新价折算cny
        "high_cny":"2.37",
        "low_cny":"1.33",
        "last_usd":"0.27",              //最新价折算usd
        "high_usd":"0.35",
        "low_usd":"0.19"
    },
    "cmd":"api/market"
}
```
### 查询市场深度    def get_depth(self, symbol, size=200):
* GET https://api.coinpark.cc/v1/mdata?cmd=depth&pair=BIX_BTC&size=10
* POST https://api.coinpark.cc/v1/mdata
```
请求参数：
cmd: "api/depth"
body: {
    pair,       //交易对，如BIX_BTC
    size,       //要几条，1-200，不传返回200
}

返回结果：
{
    "result":{
        "pair":"LTC_BTC",
        "update_time":1510983122681,
        "asks":[                            //卖方深度

        ],
        "bids":[                            //买方深度
            {
                "price":"0.008596",         //挂单价格
                "volume":"18.54306495"      //挂单数量
            },
            {
                "price":"0.00859289",
                "volume":"40.13567123"
            }
        ]
    },
    "cmd":"api/depth"
}
```
### 查询成交记录    def get_deals(self, symbol, size=200):
* GET https://api.coinpark.cc/v1/mdata?cmd=deals&pair=BIX_BTC&size=10
* POST https://api.coinpark.cc/v1/mdata
```
请求参数：
cmd: "api/deals"
body: {
    pair,       //交易对，如BIX_BTC
    size,       //要几条，1-200，不传返回200
}

返回结果：
{
    "result":[
        {
            "pair":"LTC_BTC",
            "price":"0.008601",                 //成交价格
            "amount":"24.12584739",             //成交数量
            "time":"1512721748000",             //成交时间
            "side":2                            //交易方向，1-买，2-卖
        },
        {
            "pair":"LTC_BTC",
            "price":"0.008611",                 //成交价格
            "amount":"24.23584739",             //成交数量
            "time":"1512721748000",             //成交时间
            "side":2                            //交易方向，1-买，2-卖
        }
    ],
    "cmd":"api/deals"
}
```
### 查询市场ticker    def get_ticker(self, symbol):
* GET https://api.coinpark.cc/v1/mdata?cmd=ticker&pair=BIX_BTC
* POST https://api.coinpark.cc/v1/mdata
```
请求参数：
cmd: "api/ticker"
body: {
    pair,       //交易对，如BIX_BTC
}

返回结果：
{
    "result":{
        "buy":"0.00582132",         //最新买一价
        "high":"0.00778847",        //24h最高价
        "last":"0.00582156",        //最新成交价
        "low":"0.00540611",         //24h最低价
        "sell":"0.00582152",        //最新卖一价
        "timestamp":1510983122665,  //时间戳
        "vol":"70.50811953"         //24h成交量
        "last_cny":"621.53",        //最新成交价，cny计价
        "last_usd":"93.93"          //最新成交价，usd计价
    },
    "cmd":"api/ticker"
}
```
## 用户资产信息(需要apikey)
### 普通账户资产    def get_balance(self, select=1):
POST https://api.coinpark.cc/v1/transfer
```
请求参数：
cmd: "transfer/assets"
body: {
    select       //可选，1-请求所有币种资产明细，不传-各币种总资产合计
}

返回结果：
{
    "result":{
        "total_btc":"107.71371658",             //各币种资产总和，btc计价
        "total_cny":"5587362.53",               //各币种资产总和，cny计价
        "total_usd":"4000.30",                  //各币种资产总和，usd计价
        "assets_list":[                         //币种资产明细，没有返回 []
            {
                "coin_symbol":"BTC",
                "balance":"102.31666784",       //可用
                "freeze":"0.01800000",          //冻结
                "BTCValue":"1100.35043000",     //btc估值
                "CNYValue":"59448654.69",       //cny估值
                "USDValue":"8945419.86",        //usd估值
            },
            {
                "coin_symbol":"ETH",
                "balance":"100.00000000",
                "freeze":"0.00000000",
                "BTCValue":"1100.35043000",     //btc估值
                "CNYValue":"59448654.69",       //cny估值
                "USDValue":"8945419.86",        //usd估值
            },
            {
                "coin_symbol":"LTC",
                "balance":"125.34853787",
                "freeze":"0.00000000",
                "BTCValue":"1100.35043000",     //btc估值
                "CNYValue":"59448654.69",       //cny估值
                "USDValue":"8945419.86",        //usd估值
            },
            {
                "coin_symbol":"BIX",
                "balance":"712.79411732",
                "freeze":"0.00000000",
                "BTCValue":"1100.35043000",     //btc估值
                "CNYValue":"59448654.69",       //cny估值
                "USDValue":"8945419.86",        //usd估值
            }
        ]
    },
    "cmd":"transfer/assets"
}
```
### 提现信息    def get_withdrawInfo(self, withdraw_id):
POST https://api.coinpark.cc/v1/transfer
```
请求参数：
cmd: "transfer/withdrawInfo",
body: {
    id,  // 提现 id
}

返回结果：
{
    "result":{
      	"id":228,
	"createdAt": 1512756997000,
	"coin_symbol":"LTC",                        // 币种
	"to_address":"xxxxxxxxxxxxxxxxxxxxxxxxxx",  // 提现地址
	"status":3,                                 // 状态,  -2：审核不通过；-1: 用户撤销；0:待审核; 1:审核通过（待发币）;  2: 发币中； 3：发币完成'
	"amount":"1.00000000",                      // 数量
	"fee":0.1                                   // 手续费
    },
    "cmd":"transfer/withdrawInfo"
}
```

## 交易(需要apikey)
### 下单    def create_order_cmd(self, index, symbol, order_side, order_type, price, amount, money, pay_bix=0, account_type=0):
POST https://api.coinpark.cc/v1/orderpending
```
请求参数：
cmd: "orderpending/trade",
index: 12345,       //随机数，int类型，批量时唯一标识某个cmd
body: {
    pair,           //交易对, BIX_BTC, BIX_ETH, ...
    account_type,   //账户类型，0-普通账户，1-信用账户
    order_type,     //交易类型，1-市价单，2-限价单
    order_side,     //交易方向，1-买，2-卖
    pay_bix,        //是否bix抵扣手续费，0-不抵扣，1-抵扣
    price,          //委托价格
    amount,         //委托数量
    money,          //委托金额(order_type=1时需要)
}

返回结果：
{
    "result": 34,     //返回委托单id
    "index": 12345,   //用户自定义随机数
    "cmd":"orderpending/trade"
}
```
### 撤单    def cancel_order_cmd(self, index, order_id):
POST https://api.coinpark.cc/v1/orderpending
```
请求参数：
cmd: "orderpending/cancelTrade"
index: 12345,       //随机数，int类型，批量时唯一标识某个cmd
body: {
    orders_id,  //委托单id
}

返回结果：
{
    "result":"撤销中",
    "index": 12345,   //用户自定义随机数
    "cmd":"orderpending/cancelTrade"
}
```
### 当前委托#def get_order_pending_list(self, page, size, pair=None, account_type=None, coin_symbol=None,currency_symbol=None, order_side=None):

POST https://api.coinpark.cc/v1/orderpending
```
请求参数：
cmd: "orderpending/orderPendingList"
body: {
    [pair],           //交易对,兼容参数
    [account_type],   //账户类型，0-普通账户，1-信用账户
    page,             //第几页，从1开始
    size              //要几条
    [coin_symbol]     //交易币种
    [currency_symbol] //定价币种
    [order_side]      //交易方向，1-买，2-卖
}

返回结果：
{
    "result":{
        "count":1,
        "page":1,
        "items":[
            {
                "id":159,
                "createdAt": 1512756997000,
                "account_type":0,                       //账户类型 0-普通账户，1-信用账户
                "coin_symbol":"LTC",                    //交易币种
                "currency_symbol":"BTC",                //定价币种
                "order_side":2,                         //交易方向，1-买，2-卖
                "order_type":2,                         //订单类型，1-市价单，2-限价单
                "price":"0.00900000",                   //委托价格，市价单是0
                "amount":"1.00000000",                  //委托数量，市价买单是0
                "money":"0.00900000",                   //委托金额，市价卖单是0
                "deal_amount":"0.00000000",             //已成交数量
                "deal_percent":"0.00%",                 //成交百分比
                "unexecuted":"0.00000000",              //未成交数量
                "status":1                              //状态，1-待成交，2-部分成交，3-完全成交，4-部分撤销，5-完全撤销，6-待撤销
            }
        ]
    },
    "cmd":"orderpending/orderPendingList"
}
```

### 历史委托#def get_pending_history_list(self, page, size, pair=None, account_type=None, coin_symbol=None,currency_symbol=None, order_side=None, hide_cancel=None):
POST https://api.coinpark.cc/v1/orderpending
```
请求参数：
cmd: "orderpending/pendingHistoryList"
body: {
    [pair],           //交易对,兼容参数
    [account_type],   //账户类型，0-普通账户，1-信用账户
    page,             //第几页，从1开始
    size              //要几条
    [coin_symbol]     //交易币种
    [currency_symbol] //定价币种
    [order_side]      //交易方向，1-买，2-卖
    [hide_cancel]     //隐藏已撤销订单，0-不隐藏，1-隐藏
}

返回结果：
{
    "result":{
        "count":1,
        "page":1,
        "items":[
            {
                "id":159,
                "createdAt": 1512756997000,
                "account_type":0,                       //账户类型 0-普通账户，1-信用账户
                "coin_symbol":"LTC",                    //交易币种
                "currency_symbol":"BTC",                //定价币种
                "order_side":2,                         //交易方向，1-买，2-卖
                "order_type":2,                         //订单类型，1-市价单，2-限价单
                "price":"0.00900000",                   //委托价格，市价单是0
                "amount":"1.00000000",                  //委托数量，市价买单是0
                "money":"0.00900000",                   //委托金额，市价卖单是0
                "deal_price":"0.00900000",              //成交均价
                "deal_amount":"1.00000000",             //已成交数量
                "deal_money":"0.00900000",              //已成交金额
                "deal_percent":"100%",                  //成交百分比
                "status":3                              //状态，1-待成交，2-部分成交，3-完全成交，4-部分撤销，5-完全撤销，6-待撤销
            }
        ]
    },
    "cmd":"orderpending/pendingHistoryList"
}
```

### 委托单详情    def get_order(self, order_id):
POST https://api.coinpark.cc/v1/orderpending
```
请求参数：
cmd: "orderpending/order"
body: {
    id,           //委托单id
}

返回结果：
{
    "result":{
        "id":159,
         "createdAt": 1512756997000,
         "account_type":0,                       //账户类型 0-普通账户，1-信用账户
         "pair":"LTC_BTC",                       //交易对
         "coin_symbol":"LTC",                    //交易币种
         "currency_symbol":"BTC",                //定价币种
         "order_side":2,                         //交易方向，1-买，2-卖
         "order_type":2,                         //订单类型，1-市价单，2-限价单
         "price":"0.00900000",                   //委托价格，市价单是0
         "amount":"1.00000000",                  //委托数量，市价买单是0
         "money":"0.00900000",                   //委托金额，市价卖单是0
         "deal_amount":"0.00000000",             //已成交数量
         "deal_percent":"0.00%",                 //成交百分比
         "unexecuted":"0.00000000",              //未成交数量
         "status":1                              //状态，1-待成交，2-部分成交，3-完全成交，4-部分撤销，5-完全撤销，6-待撤销
    },
    "cmd":"orderpending/order"
}
```

### 成交明细    def get_order_history_list(self, page, size, pair=None, account_type=None, coin_symbol=None, currency_symbol=None,order_side=None):
POST https://api.coinpark.cc/v1/orderpending
```
请求参数：
cmd: "orderpending/orderHistoryList"
body: {
    [pair],           //交易对,兼容参数
    [account_type],   //账户类型，0-普通账户，1-信用账户
    page,             //第几页，从1开始
    size              //要几条
    [coin_symbol]     //交易币种
    [currency_symbol] //定价币种
    [order_side]      //交易方向，1-买，2-卖
}

返回结果：
{
    "result":{
        "count":1,              //记录总数
        "page":1,               //当前第几页
        "items":[               //记录明细
            {
                "id":228,
                "createdAt": 1512756997000,
                "account_type":0,                           //账户类型 0-普通账户，1-信用账户
                "coin_symbol":"LTC",                        //交易币种
                "currency_symbol":"BTC",                    //定价币种
                "order_side":2,                             //交易方向，1-买，2-卖
                "order_type":2,                             //订单类型，1-市价单，2-限价单
                "price":"0.00886500",                       //成交价格
                "amount":"1.00000000",                      //成交量
                "money":"0.00886500",                       //成交额，单位是定价币种
                "fee":0                                     //手续费
            }
        ]
    },
    "cmd":"orderpending/orderHistoryList"
}
```