#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   stockFormat.py
@Time    :   2020/10/31 20:26:15
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''

import json
from stockInfoFormatter import stockItemObj
from stockInfoFormatter.stockKeyDef import keyConverterToLong, stock_ID,stock_Name

STOCK_BASIC_ITEM_INFO_KEYS = [stock_ID,stock_Name]

class StockBasicInfo(stockItemObj.StockItemObj):
    def __init__(self):
        super(StockBasicInfo, self).__init__()
        self.stockItems[stock_ID] = ''
        self.stockItems[stock_Name] = ''
    
    def initWithJson(self,jsonStr):
        jsonObj = json.loads(jsonStr,encoding='utf-8')
        for key in jsonObj:
            longKey = keyConverterToLong(key)
            if longKey not in STOCK_BASIC_ITEM_INFO_KEYS:
                continue
            self.stockItems[longKey] = jsonObj[key]