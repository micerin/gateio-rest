#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Provide the GateIO class to abstract web interaction
'''

from HttpUtil import getSign, httpGet, httpPost
import json
from collections import OrderedDict

class GateIO:
    def __init__(self, url, apiKey, secretKey):
        self.__url = url
        self.__apiKey = apiKey
        self.__secretKey = secretKey

    ## General methods that query the exchange

    #所有交易对
    def pairs(self):
        URL = "/api2/1/pairs"
        params=''
        return httpGet(self.__url, URL, params)

    #市场订单参数
    def marketinfo(self):
        URL = "/api2/1/marketinfo"
        params=''
        return httpGet(self.__url, URL, params)

    #交易市场详细行情
    def marketlist(self):
        URL = "/api2/1/marketlist"
        params=''
        return httpGet(self.__url, URL, params)

    #所有交易行情
    def tickers(self):
        URL = "/api2/1/tickers"
        params=''
        return httpGet(self.__url, URL, params)

    # 所有交易对市场深度
    def orderBooks(self):
        URL = "/api2/1/orderBooks"
        param=''
        return httpGet(self.__url, URL, param)


    #单项交易行情
    def ticker(self, param):
        URL = "/api2/1/ticker"
        return httpGet(self.__url, URL, param)
        # data = json.loads( httpGet(self.__url, URL, param), object_pairs_hook=UserString)
        # return json.dumps(data, indent=2)
        # response = httpGet(self.__url, URL, param)
        #data = response.json()
        # data = json.load(response)
        # return data# json.dump(data)

    # 单项交易对市场深度
    def orderBook(self, param):
        URL = "/api2/1/orderBook"
        return httpGet(self.__url, URL, param)

    # 历史成交记录
    def tradeHistory(self, param):
        URL = "/api2/1/tradeHistory"
        return httpGet(self.__url, URL, param)

    ## Methods that make use of the users keys

    #获取帐号资金余额
    def balances(self):
        URL = "/api2/1/private/balances"
        param = {}
        data = json.loads( httpPost(self.__url, URL, param, self.__apiKey, self.__secretKey), object_pairs_hook=OrderedDict)
        return json.dumps(data, indent=2)

    def balancesFormatted(self):
        URL = "/api2/1/private/balances"
        param = {}
        data = json.loads( httpPost(self.__url, URL, param, self.__apiKey, self.__secretKey), object_pairs_hook=OrderedDict)

        print('Account Balance State')
        print(json.dumps(data, indent=2))
        # for(i in range(len(data['available']))):
        #     token = data['available'][i]
        #     print ("%s amount:%s" % (token.namupper(), data['order']['orderNumber'], data['order']['status'], data['order']['type'], data['order']['rate'], data['order']['amount']))
        return 0

    # 获取充值地址
    def depositAddres(self,param):
        URL = "/api2/1/private/depositAddress"
        params = {'currency':param}
        return httpPost(self.__url, URL, params, self.__apiKey, self.__secretKey)

    # 获取充值提现历史
    def depositsWithdrawals(self, start,end):
        URL = "/api2/1/private/depositsWithdrawals"
        params = {'start': start,'end':end}
        return httpPost(self.__url, URL, params, self.__apiKey, self.__secretKey)

    # 买入
    def buy(self, currencyPair,rate, amount):
        URL = "/api2/1/private/buy"
        params = {'currencyPair': currencyPair,'rate':rate, 'amount':amount}
        data = json.loads( httpPost(self.__url, URL, params, self.__apiKey, self.__secretKey), object_pairs_hook=OrderedDict)
        return json.dumps(data, indent=2)

    # 卖出
    def sell(self, currencyPair, rate, amount):
        URL = "/api2/1/private/sell"
        params = {'currencyPair': currencyPair, 'rate': rate, 'amount': amount}
        data = json.loads( httpPost(self.__url, URL, params, self.__apiKey, self.__secretKey), object_pairs_hook=OrderedDict)
        return json.dumps(data, indent=2)

    # 取消订单
    def cancelOrder(self, orderNumber, currencyPair):
        URL = "/api2/1/private/cancelOrder"
        params = {'orderNumber': orderNumber, 'currencyPair': currencyPair}
        data = json.loads( httpPost(self.__url, URL, params, self.__apiKey, self.__secretKey), object_pairs_hook=OrderedDict)
        return json.dumps(data, indent=2)

    # 取消所有订单
    # type下单类型(0:卖出,1:买入,-1:不限制)
    def cancelAllOrders(self, type, currencyPair):
        URL = "/api2/1/private/cancelAllOrders"
        params = {'type': type, 'currencyPair': currencyPair}
        data = json.loads( httpPost(self.__url, URL, params, self.__apiKey, self.__secretKey), object_pairs_hook=OrderedDict)
        return json.dumps(data, indent=2)

    # def cancelAllOrdersFormatted(self, type, currencyPair):
    #     URL = "/api2/1/private/cancelAllOrders"
    #     params = {'type': type, 'currencyPair': currencyPair}
    #     data = json.loads(httpPost(self.__url, URL, params, self.__apiKey, self.__secretKey), object_pairs_hook=OrderedDict)
    #     return json.dumps(data, indent=2)

    # 获取下单状态
    def getOrder(self, orderNumber, currencyPair):
        URL = "/api2/1/private/getOrder"
        params = {'orderNumber': orderNumber, 'currencyPair': currencyPair}
        data = json.loads( httpPost(self.__url, URL, params, self.__apiKey, self.__secretKey), object_pairs_hook=OrderedDict)
        return json.dumps(data, indent=2)        
    
    def getOrderFormatted(self, orderNumber, currencyPair):
        URL = "/api2/1/private/getOrder"
        params = {'orderNumber': orderNumber, 'currencyPair': currencyPair}
        data = json.loads(httpPost(self.__url, URL, params, self.__apiKey, self.__secretKey), object_pairs_hook=OrderedDict)
        print ("%s order:%s status:%s type:%s rate:%s amount:%s" % (currencyPair.upper(), data['order']['orderNumber'], data['order']['status'], data['order']['type'], data['order']['rate'], data['order']['amount']))
        return 0

    # 获取我的当前挂单列表
    def openOrders(self):
        URL = "/api2/1/private/openOrders"
        params = {}
        data = json.loads(httpPost(self.__url, URL, params, self.__apiKey, self.__secretKey), object_pairs_hook=OrderedDict)
        return json.dumps(data, indent=2)

    def openOrdersFormatted(self):
        URL = "/api2/1/private/openOrders"
        params = {}
        data = json.loads( httpPost(self.__url, URL, params, self.__apiKey, self.__secretKey), object_pairs_hook=OrderedDict)
        print('Open Orders:')
        for i in range(len(data['orders'])):
            order = data['orders'][i]
            print("%s %s status:%s type:%s rate:%s amount:%s" % (order['currencyPair'].upper(), order['orderNumber'], order['status'], order['type'], order['rate'], order['amount']))
        return 0

    # 获取我的24小时内成交记录
    def myTradeHistory(self, currencyPair, orderNumber):
        URL = "/api2/1/private/tradeHistory"
        params = {'currencyPair': currencyPair, 'orderNumber': orderNumber}
        data = json.loads(httpPost(self.__url, URL, params, self.__apiKey, self.__secretKey), object_pairs_hook=OrderedDict)
        return json.dumps(data, indent=2)

    # 提现
    def withdraw(self, currency, amount, address):
        URL = "/api2/1/private/withdraw"
        params = {'currency': currency, 'amount': amount,'address':address}
        return httpPost(self.__url, URL, params, self.__apiKey, self.__secretKey)
