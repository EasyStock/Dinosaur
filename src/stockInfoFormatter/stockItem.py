#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   stockItem.py
@Time    :   2020/12/07 20:58:17
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''
from stockInfoFormatter.stockKeyDef import keyConverterToLong, stock_OpenPrice,\
            stock_ClosePrice,stock_HighPrice,stock_LowerPrice,stock_Volumn,stock_Turnover,stock_OtherInfo
from stockInfoFormatter import stockItemObj
import json

STOCK_ITEM_KEYS = [
    stock_OpenPrice,
    stock_ClosePrice,
    stock_HighPrice,
    stock_LowerPrice,
    stock_Volumn,
    stock_Turnover,
    stock_OtherInfo
]

class StockItem(stockItemObj.StockItemObj):
    def __init__(self):
        super(StockItem, self).__init__()
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
            if longKey not in STOCK_ITEM_KEYS:
                continue
            self.stockItems[longKey] = jsonObj[key]