#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   stockDailyItem.py
@Time    :   2020/12/07 20:57:24
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''



from stockInfoFormatter import stockItemObj
from stockInfoFormatter.stockKeyDef import stock_ID,stock_OpenPrice,stock_ClosePrice,\
    stock_HighPrice,stock_LowerPrice,stock_Volumn,stock_Turnover,stock_OtherInfo,keyConverterToLong
import json

STOCK_DAILY_ITEM_KEYS = [
    stock_ID,
    stock_OpenPrice,
    stock_ClosePrice,
    stock_HighPrice,
    stock_LowerPrice,
    stock_Volumn,
    stock_Turnover,
    stock_OtherInfo
]

class StockDailyItem(stockItemObj.StockItemObj):
    def __init__(self):
        super(StockDailyItem, self).__init__()
        self.stockItems[stock_ID] = 0.0
        self.stockItems[stock_OpenPrice] = 0.0
        self.stockItems[stock_ClosePrice] = 0.0
        self.stockItems[stock_HighPrice] = 0.0
        self.stockItems[stock_LowerPrice] = 0.0
        self.stockItems[stock_Volumn] = 0.0
        self.stockItems[stock_Turnover] = 0.0
        self.stockItems[stock_OtherInfo] = ''
    
    def initWithJson(self,jsonStr):
        jsonObj = json.loads(jsonStr,encoding='utf-8')
        for key in jsonObj:
            longKey = keyConverterToLong(key)
            if longKey not in STOCK_DAILY_ITEM_KEYS:
                continue
            self.stockItems[longKey] = jsonObj[key]