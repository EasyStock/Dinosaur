#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   columnsName.py
@Time    :   2020/12/27 10:35:49
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''

KW_DATE = 'date'
KW_SID = 'sid'
KW_OPEN = 'open'
KW_CLOSE = 'close'
KW_LOW = 'low'
KW_HIGH = 'high'
KW_PRE_CLOSE = 'pre_close'
KW_VOLUME = 'vol'
KW_TURN_OVER = 'turnover'
KW_MA5 = 'ma5'
KW_MA10 = 'ma10'
KW_MA20 = 'ma20'
KW_MA30 = 'ma30'
KW_MA60 = 'ma60'
KW_MA120 = 'ma120'
KW_MA240 = 'ma240'
KW_MACD = 'macd'
KW_BOLL_U = 'bollu'
KW_BOLL_M = 'bollm'
KW_BOLL_L = 'bolll'
KW_RSI6 = 'rsi6'
KW_RSI12 = 'rsi12'
KW_RSI24 = 'rsi24'
KW_MARKET = 'market'
KW_OTHER_INFO = 'otherInfo'

KW_FILTER_COLUMNS_BASIC1 = [KW_SID,KW_DATE,KW_CLOSE]
KW_FILTER_COLUMNS_BASIC2 = [KW_SID,KW_DATE,KW_OPEN,KW_CLOSE,KW_HIGH,KW_LOW,KW_VOLUME,KW_TURN_OVER]
KW_FILTER_COLUMNS_MAS = [KW_MA5,KW_MA10,KW_MA20,KW_MA30,KW_MA60,KW_MA120,KW_MA240]
KW_INDEXES = [KW_MA5,KW_MA10,KW_MA20,KW_MA30,KW_MA60,KW_MA120,KW_MA240,KW_MACD,KW_BOLL_U,KW_BOLL_M,KW_BOLL_L,KW_RSI6,KW_RSI12,KW_RSI24]
