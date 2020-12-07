#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   testStockInfo.py
@Time    :   2020/12/07 22:11:09
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''

from stockInfoFormatter.stockHistoryItem import StockHistoryItem
from stockInfoFormatter.stockDailyItem import StockDailyItem
from stockInfoFormatter.stockItem import StockItem
from stockInfoFormatter.stockBasicInfo import StockBasicInfo
from stockInfoFormatter.stockItemObj import StockItemObj

def testStockItemObj():
    print(StockItemObj())
    print(StockItemObj().toJson_longKey())
    print(StockItemObj().toJson_shortKey())
    print(StockItemObj().toList())
    print(StockItemObj().toDict())
    print(StockItemObj().value())
    print(StockItemObj().columns())


def testStockBasicInfo():
    print(StockBasicInfo())
    print(StockBasicInfo().toJson_longKey())
    print(StockBasicInfo().toJson_shortKey())
    print(StockBasicInfo().toList())
    print(StockBasicInfo().toDict())
    print(StockBasicInfo().value())
    print(StockBasicInfo().columns())
    jsonStr = '''{"股票简称": "11111","股票代码": "22222","最高价": "3333"}'''
    a = StockBasicInfo()
    a.initWithJson(jsonStr)
    print(a)

def testStockItem():
    print(StockItem())
    print(StockItem().toJson_longKey())
    print(StockItem().toJson_shortKey())
    print(StockItem().toList())
    print(StockItem().toDict())
    print(StockItem().value())
    print(StockItem().columns())
    jsonStr = '''{"收盘价": 1.0, "开盘价": 2.0, "最高价": 0.0, "最低价": 0.0, "成交量(股)": 0.0, "成交额(元)": 0.0, "其他信息": ""}'''
    a = StockItem()
    a.initWithJson(jsonStr)
    print(a)

def testStockDailyItem():
    print(StockDailyItem())
    print(StockDailyItem().toJson_longKey())
    print(StockDailyItem().toJson_shortKey())
    print(StockDailyItem().toList())
    print(StockDailyItem().toDict())
    print(StockDailyItem().value())
    print(StockDailyItem().columns())
    jsonStr = '''{"日期": 0.0,"股票代码": 0.0, "开盘价": 0.0, "收盘价": 0.0, "最高价": 0.0, "最低价": 0.0, "成交量(股)": 0.0, "成交额(元)": 0.0, "其他信息": ""}'''
    a = StockDailyItem()
    a.initWithJson(jsonStr)
    print(a)

def testStockHistoryItem():
    print(StockHistoryItem())
    print(StockHistoryItem().toJson_longKey())
    print(StockHistoryItem().toJson_shortKey())
    print(StockHistoryItem().toList())
    print(StockHistoryItem().toDict())
    print(StockHistoryItem().value())
    print(StockHistoryItem().columns())
    jsonStr = '''{"日期": 0.0,"股票代码": 0.0, "开盘价": 0.0, "收盘价": 0.0, "最高价": 0.0, "最低价": 0.0, "成交量(股)": 0.0, "成交额(元)": 0.0, "其他信息": ""}'''
    a = StockHistoryItem()
    a.initWithJson(jsonStr)
    print(a)