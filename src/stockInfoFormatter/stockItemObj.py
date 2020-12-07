#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   stockItemBase.py
@Time    :   2020/12/07 21:27:16
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''

from stockInfoFormatter.stockKeyDef import keyConverterToShort,keyConverterToLong
import collections
import pandas as pd
import json

class StockItemObj(object):
    def __init__(self):
        self.stockItems = collections.OrderedDict()
    
    def toJson_shortKey(self):
        tmp = collections.OrderedDict()
        for key in self.stockItems:
            keyInshort = keyConverterToShort(key)
            tmp[keyInshort] = self.stockItems[key]
        return json.dumps(tmp,ensure_ascii=False)

    def toJson_longKey(self):
        return json.dumps(self.stockItems,ensure_ascii=False)

    def toList(self):
        return list(self.stockItems.values())

    def toDict(self):
        return dict(self.stockItems)

    def value(self):
        return self.stockItems

    def columns(self):
        return list(self.stockItems.keys())

    def __str__(self):
        series = pd.Series(self.stockItems)
        return str(series)

    def initWithJson(self,jsonStr):
        raise Exception("not implemented!")
