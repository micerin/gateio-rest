#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
# https://gate.io/api2

'''
Provide user specific data and interact with gate.io
'''

from gateAPI import GateIO
import sys  

# Usage
def printUsage():
    print('default without parameter, show all state and orders')
    print('*.py orders     -- show all open order')
    print('*.py state     -- show current balance')
    print('*.py buy [currencyPair] [rate] [amount] ')
    print('*.py sell [currencyPair] [rate] [amount] ')
    print('*.py cancel [orderNum] [currencyPair] ')
    print('*.py cancelall [type] [currencyPair]  type for order(0:sell 1:buy -1:noLimit) ')
    print('*.py tick     -- latest ticker for interested tokens ')
    print('*.py tick [currencyPair]     -- latest ticker for interested tokens ')
    print('*.py status [orderNum] [currencyPair]     -- get order status ')
    print('*.py history [currencyPair] [orderNum]     -- get 24 hour trade status ')

## 填写 apiKey APISECRET
apiKey = ''
secretKey = ''
## address
btcAddress = 'your btc address'

## Provide constants
API_QUERY_URL = 'data.gate.io'
API_TRADE_URL = 'api.gate.io'

## Create a gate class instance
gate_query = GateIO(API_QUERY_URL, apiKey, secretKey)
gate_trade = GateIO(API_TRADE_URL, apiKey, secretKey)

if(len(sys.argv)  == 1):
    # Ticker on interested coins
    print('------------Ticker on coins------------')
    print(gate_query.ticker('btc_usdt'))
    print(gate_query.ticker('xrp_usdt'))
    print(gate_query.ticker('eth_usdt'))
    print(gate_query.ticker('doge_usdt'))
    print(gate_query.ticker('ltc_usdt'))
    print(gate_query.ticker('etc_usdt'))
    print(gate_query.ticker('iota_usdt'))
    print(gate_query.ticker('eos_usdt'))
    print(gate_query.ticker('neo_usdt'))
    print('------------Ticker on coins End------------')
    print('')
    print('')
        
    #  All Private
    # # Get account fund balances
    print('----------Fund Balance------------')
    print(gate_trade.balances())
    print('----------Fund Balance End------------')
    print('')
    print('')
        
    #  active orders
    print('------------Open Orders------------')
    print(gate_query.openOrders())
    print('------------Open Orders End------------')
    print('')
    print('')

else:
    if(sys.argv[1] == 'orders'):
       print(gate_query.openOrders())
       #gate_query.openOrdersFormatted()
    elif (sys.argv[1] == "state"):
        print(gate_trade.balances())
    elif(sys.argv[1] == "buy"):
        print(gate_trade.buy(sys.argv[2], sys.argv[3],sys.argv[4]))
    elif(sys.argv[1] == "sell"):
        print(gate_trade.sell(sys.argv[2], sys.argv[3],sys.argv[4]))
    elif(sys.argv[1] == "cancel"):
        print(gate_trade.cancelOrder(sys.argv[2], sys.argv[3]))
    elif(sys.argv[1] == "cancelall"):
        print(gate_trade.cancelAllOrders(sys.argv[2], sys.argv[3]))
    elif(sys.argv[1] == "status"):
       print(gate_trade.getOrder(sys.argv[2], sys.argv[3]))
       #gate_trade.getOrderFormatted(sys.argv[2], sys.argv[3])
    elif(sys.argv[1] == "history"):
        print(gate_trade.myTradeHistory(sys.argv[2], sys.argv[3]))
    elif(sys.argv[1] == "tick" and len(sys.argv) > 2):
        print(sys.argv[2])
        print(gate_query.ticker(sys.argv[2]))
    elif(sys.argv[1] == "tick"):
        print('btc_usdt')
        print(gate_query.ticker('btc_usdt'))
        print('')
        print('xrp_usdt')
        print(gate_query.ticker('xrp_usdt'))
        print('')
        print('eth_usdt')
        print(gate_query.ticker('eth_usdt'))
        print('')
        print('doge_usdt')
        print(gate_query.ticker('doge_usdt'))
        print('')
        print('ltc_usdt')
        print(gate_query.ticker('ltc_usdt'))
        print('')
        print('etc_usdt')
        print(gate_query.ticker('etc_usdt'))
        print('')
        print('iota_usdt')
        print(gate_query.ticker('iota_usdt'))
        print('')
        print('eos_usdt')
        print(gate_query.ticker('eos_usdt'))
        print('')
        print('neo_usdt')
        print(gate_query.ticker('neo_usdt'))
    elif(sys.argv[1] == 'help' or sys.argv[1] == '?' or sys.argv[1] == '/?'):
        printUsage()
    else:
        printUsage()

# Place order buy
# print(gate_trade.buy('etc_btc', '0.001', '123'))

# Place order sell
# print(gate_trade.sell('etc_btc', '0.001', '123'))

# Cancel order
# print(gate_trade.cancelOrder('267040896', 'etc_btc'))

# Cancel all orders
# type下单类型(0:卖出,1:买入,-1:不限制)
#print(gate_trade.cancelAllOrders('1', 'doge_usdt'))
#print(gate_trade.cancelAllOrders('1', 'xrp_usdt'))

# Get order status
# print(gate_trade.getOrder('267040896', 'eth_btc'))

# Get my last 24h trades
#print(gate_trade.mytradeHistory('eth_usdt', ''))

#all currencypair for reference
#['btc_usdt', 'bch_usdt', 'eth_usdt', 'etc_usdt', 'qtum_usdt', 'ltc_usdt', 'dash_usdt', 'zec_usdt', 'btm_usdt', 'eos_usdt', 'req_usdt', 'snt_usdt', 'omg_usdt', 'pay_usdt', 'cvc_usdt', 'zrx_usdt', 'tnt_usdt', 'xmr_usdt', 'xrp_usdt', 'doge_usdt', 'bat_usdt', 'pst_usdt', 'btg_usdt', 'dpy_usdt', 'lrc_usdt', 'storj_usdt', 'rdn_usdt', 'stx_usdt', 'knc_usdt', 'link_usdt', 'cdt_usdt', 'ae_usdt', 'ae_eth', 'ae_btc', 'cdt_eth', 'rdn_eth', 'stx_eth', 'knc_eth', 'link_eth', 'req_eth', 'rcn_eth', 'trx_eth', 'arn_eth', 'kick_eth', 'bnt_eth', 'ven_eth', 'mco_eth', 'fun_eth', 'data_eth', 'rlc_eth', 'zsc_eth', 'wings_eth', 'ctr_eth', 'mda_eth', 'rcn_usdt', 'trx_usdt', 'kick_usdt', 'ven_usdt', 'mco_usdt', 'fun_usdt', 'data_usdt', 'zsc_usdt', 'ctr_usdt', 'mda_usdt', 'xtz_usdt', 'gnt_usdt', 'gnt_eth', 'gem_usdt', 'gem_eth', 'rfr_usdt', 'rfr_eth', 'dadi_usdt', 'dadi_eth', 'abt_usdt', 'abt_eth', 'ledu_usdt', 'ledu_btc', 'ledu_eth', 'ost_usdt', 'ost_eth', 'xlm_usdt', 'xlm_eth', 'xlm_btc', 'mobi_usdt', 'mobi_eth', 'mobi_btc', 'ocn_usdt', 'ocn_eth', 'ocn_btc', 'zpt_usdt', 'zpt_eth', 'zpt_btc', 'cofi_usdt', 'cofi_eth', 'jnt_usdt', 'jnt_eth', 'jnt_btc', 'blz_usdt', 'blz_eth', 'gxs_usdt', 'gxs_btc', 'mtn_usdt', 'mtn_eth', 'ruff_usdt', 'ruff_eth', 'ruff_btc', 'tnc_usdt', 'tnc_eth', 'tnc_btc', 'zil_usdt', 'zil_eth', 'tio_usdt', 'tio_eth', 'bto_usdt', 'bto_eth', 'theta_usdt', 'theta_eth', 'ddd_usdt', 'ddd_eth', 'ddd_btc', 'mkr_usdt', 'mkr_eth', 'dai_usdt', 'smt_usdt', 'smt_eth', 'mdt_usdt', 'mdt_eth', 'mdt_btc', 'mana_usdt', 'mana_eth', 'lun_usdt', 'lun_eth', 'salt_usdt', 'salt_eth', 'fuel_usdt', 'fuel_eth', 'elf_usdt', 'elf_eth', 'drgn_usdt', 'drgn_eth', 'gtc_usdt', 'gtc_eth', 'gtc_btc', 'qlc_usdt', 'qlc_btc', 'qlc_eth', 'dbc_usdt', 'dbc_btc', 'dbc_eth', 'bnty_usdt', 'bnty_eth', 'lend_usdt', 'lend_eth', 'icx_usdt', 'icx_eth', 'btf_usdt', 'btf_btc', 'ada_usdt', 'ada_btc', 'lsk_usdt', 'lsk_btc', 'waves_usdt', 'waves_btc', 'bifi_usdt', 'bifi_btc', 'mds_eth', 'mds_usdt', 'dgd_usdt', 'dgd_eth', 'qash_usdt', 'qash_eth', 'qash_btc', 'powr_usdt', 'powr_eth', 'powr_btc', 'fil_usdt', 'bcd_usdt', 'bcd_btc', 'sbtc_usdt', 'sbtc_btc', 'god_usdt', 'god_btc', 'bcx_usdt', 'bcx_btc', 'hsr_usdt', 'hsr_btc', 'hsr_eth', 'qsp_usdt', 'qsp_eth', 'ink_btc', 'ink_usdt', 'ink_eth', 'ink_qtum', 'med_qtum', 'med_eth', 'med_usdt', 'bot_qtum', 'bot_usdt', 'bot_eth', 'qbt_qtum', 'qbt_eth', 'qbt_usdt', 'tsl_qtum', 'tsl_usdt', 'gnx_usdt', 'gnx_eth', 'neo_usdt', 'gas_usdt', 'neo_btc', 'gas_btc', 'iota_usdt', 'iota_btc', 'nas_usdt', 'nas_eth', 'nas_btc', 'eth_btc', 'etc_btc', 'etc_eth', 'zec_btc', 'dash_btc', 'ltc_btc', 'bch_btc', 'btg_btc', 'qtum_btc', 'qtum_eth', 'xrp_btc', 'doge_btc', 'xmr_btc', 'zrx_btc', 'zrx_eth', 'dnt_eth', 'dpy_eth', 'oax_eth', 'rep_eth', 'lrc_eth', 'lrc_btc', 'pst_eth', 'bcdn_eth', 'bcdn_usdt', 'tnt_eth', 'snt_eth', 'snt_btc', 'btm_eth', 'btm_btc', 'llt_eth', 'llt_usdt', 'snet_eth', 'snet_usdt', 'llt_snet', 'omg_eth', 'omg_btc', 'pay_eth', 'pay_btc', 'bat_eth', 'bat_btc', 'cvc_eth', 'storj_eth', 'storj_btc', 'eos_eth', 'eos_btc', 'bts_usdt', 'bts_btc', 'tips_eth', 'cs_eth', 'man_eth', 'rem_eth', 'lym_eth', 'instar_eth', 'ont_eth', 'ont_usdt', 'bft_eth', 'bft_usdt', 'iht_eth', 'iht_usdt', 'senc_eth', 'senc_usdt', 'tomo_eth', 'elec_eth', 'ship_eth', 'tfd_eth', 'hav_eth', 'hur_eth', 'lst_eth']