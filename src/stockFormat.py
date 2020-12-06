#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   stockFormat.py
@Time    :   2020/10/31 20:26:15
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''

from stockKeyDef import *
import collections
import pandas as pd
import json

STOCK_BASE_ITEM_FORMAT = [stock_ID,stock_Name]

STOCK_ITEM_KEY = [
    stock_OpenPrice,
    stock_ClosePrice,
    stock_ClosePrice_Yesterday,
    stock_HighPrice,
    stock_LowerPrice,
    stock_Volumn,
    stock_Turnover,

    stock_MA5,
    stock_MA10,
    stock_MA20,
    stock_MA30,
    stock_MA60,
    stock_MA120,
    stock_MA240,
    stock_OtherInfo
]

class StockBaseInfo(object):
    def __init__(self):
        self.stock_ID = None
        self.stock_Name = None

    def __str__(self):
        msg ='%s : %s \n%s : %s'%(stock_ID, self.stock_ID, stock_Name,self.stock_Name)
        return msg

    def columns(self):
        return (stock_ID, stock_Name)
    
    def value(self):
        ret = collections.OrderedDict()
        ret[stock_ID] = self.stock_ID
        ret[stock_Name] = self.stock_Name

class StockItem(object):
    def __init__(self):
        self.items = collections.OrderedDict()
        self._initWithFormatter_()

    def _initWithFormatter_(self):
        for key in STOCK_ITEM_KEY:
            self.items[key] = None
        
    def columns(self):
        return STOCK_ITEM_KEY

    def initWithList(self,v):
        index = 0
        for key in STOCK_ITEM_KEY:
            self.items[key] = v[index]
            index = index + 1
    
    def __str__(self):
        series = pd.Series(self.items)
        return str(series)

    def toJson(self):
        ret = collections.OrderedDict()
        for key in self.items:
            keyInshort = keyConverterToShort(key)
            #keyInshort = keyConverterToLong(key)
            ret[keyInshort] = self.items[key]
        return json.dumps(ret,ensure_ascii=False)

    def value(self):
        return self.items

class StockDailyItem(object):
    def __init__(self):
        self.stock_date = None
        self.stock_Item = StockItem()
        self.stock_ID = None
    
    def toJson(self):
        tmp = collections.OrderedDict()
        tmp[stock_ID] = self.stock_ID
        tmp[stock_Date] = self.stock_date
        tmp.update(self.stock_Item.value())
        ret = collections.OrderedDict()
        for key in tmp:
            keyInshort = keyConverterToShort(key)
            #keyInshort = keyConverterToLong(key)
            ret[keyInshort] = tmp[key]
        return json.dumps(ret,ensure_ascii=False)


if __name__ == "__main__":
    print(StockBaseInfo())
    print('------')
    print(StockItem())
    print(StockItem().toJson())

    print(StockDailyItem().toJson())

