import REST.REST_API as CONST
from REST.REST_API import REST_API
import configparser
from Logging import Logger
import math
import schedule
import time


conf = configparser.ConfigParser()
conf.read("conf.ini")
api = REST_API()
# 写日志
log = Logger('all.log',level='debug')
key = conf.get("section", "key")
secret = conf.get("section", "secret")
#参数
mount = int(conf.get("section", 'mount'))
symbol = conf.get("section", 'symbol')
order_sleep = int(conf.get("section", "order_sleep"))
trading_strategy = int(conf.get("section", "trading_strategy")) #1为差价2为平价

api = REST_API()
api.auth(key, secret)#授权

# 程序停止时间设置
def sleep(t):
    time.sleep(t)
#撤销订单
def ordercancle(index,order_id):
    log.logger.info(str(index) + "号：订单号" +str(order_id))
    cmd = api.cancel_order_cmd(index,order_id)
    success, r = api.multi_sign_cmd(cmd)
    if success:
        if index == 2:
            log.logger.info("撤销卖单")
        elif index == 1:
            log.logger.info("撤销买单")
        log.logger.info("撤销缓冲...")
        sleep(5)
    else:
        log.logger.info(r)
#获取订单状态
def orderstatus(order_id):
    success, r = api.get_order(order_id)
    #log.logger.info(r)
    if success:
        status = int(r['result'][0]['result']['status'])
    else:
        log.logger.info(r)
        return 0
    #log.logger.info(status)
    if status == 3:
        return 3
    elif status == 2:
        return 2
    else:
        return 0
#循环判断订单完成
def orderjust(order_id):
    flag=0
    while True:
        r = orderstatus(order_id)
        if r == 3:
            return True
        elif r == 2:
            log.logger.info("订单部分已成交...")
        else:
            log.logger.info("订单正在等待撮合...")
        flag+=1
        sleep(1)
        if flag == order_sleep:
            return False
# 精度控制，直接抹除多余位数，非四舍五入
def digits(num, digit):
    site = pow(10, digit)
    tmp = num * site
    tmp = math.floor(tmp) / site
    return tmp
def pricedecimal(num):
        num = digits(num, 4)
#h获得买一卖一进行价差运算，得到price
def getprice():
    success, ticker = api.get_ticker(symbol)
    if success:
        buy = float(ticker['result']['buy'])
        sell = float(ticker['result']['sell'])
        return buy,sell
    else:
        print("获得买卖价失败！")
        log.logger.info(ticker)
        return 1,0
#获取USDT余额
def getusdt():
    success, usdt = api.get_balance(1)
    if success:
        r = usdt['result'][0]['result']['assets_list'][3]['balance']
        return r
    else:
       log.logger.info(usdt)
       return 0
def handler():
    buyprice, sellprice = getprice()#获取买一卖一价
    if trading_strategy == 2:#平价(有千一价差)
        r = (buyprice+sellprice)/2.0
        r = digits(r,4)
        #print("买一",buyprice,"卖一",sellprice,"平价",r)
        log.logger.info("买一"+str(buyprice)+"卖一"+str(sellprice)+"平价"+str(r))
        buyprice=r
        sellprice=r+0.0001
    elif trading_strategy ==1:#买一卖一
        #print("买一", buyprice, "卖一", sellprice)
        log.logger.info("买一"+str(buyprice)+"卖一"+str(sellprice))
    margin = buyprice - sellprice
    if margin <= 0:
        buymount = digits(mount/buyprice,4)
        sellmount = digits(mount/sellprice,4)
        cm1 = api.create_order_cmd(1, symbol, CONST.SIDE_BUY, CONST.TYPE_LIMIT_PRICE, buyprice, buymount, 0)
        cm2 = api.create_order_cmd(2, symbol, CONST.SIDE_SELL, CONST.TYPE_LIMIT_PRICE, sellprice, sellmount, 0)
        success, r = api.multi_sign_cmd([cm1, cm2])
        log.logger.info("调试信息:")
        log.logger.info(r)
        if success:
            try:
                ordersellid = r['result'][0]['result']
                ordersellindex = r['result'][0]['index']
                orderbuyid =  r['result'][1]['result']
                orderbuyindex = r['result'][1]['index']
                #调试
                #print("sell_price", sellprice, "sell_mount", sellmount,"sell_orderid",ordersellid)
                #log.logger.info("sell_price"+str(sellprice)+"sell_mount"+str(sellmount)+"sell_orderid"+str(ordersellid))
                #print("buy_price", buyprice, "buy_mount", buymount,"buy_orderid",orderbuyid)
                #log.logger.info("buy_price"+str(buyprice) + "buy_mount"+str(buymount)+"buy_orderid"+str(orderbuyid))

            except KeyError:
                pass
            try:
            #判断订单是否完成
                if orderjust(orderbuyid) == False:
                    print(orderbuyid)
                    ordercancle(orderbuyindex,orderbuyid)
                else:
                    log.logger.info("买单已成交")
                if orderjust(ordersellid) == False:
                    print(ordersellid)
                    ordercancle(ordersellindex,ordersellid)
                else:
                    log.logger.info("卖单已成交")
                log.logger.info("结尾日志:")
                log.logger.info(r)
            except UnboundLocalError:
                pass
        else:
            log.logger.info(r)
schedule.every(1).seconds.do(handler)
log.logger.info("使用交易对：")
log.logger.info(symbol)
log.logger.info("对冲USDT消耗数量：")
log.logger.info(mount)
while True:
    #log.logger.info("USDT余额："+getusdt())
    schedule.run_pending()
    time.sleep(2)


















