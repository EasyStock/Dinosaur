#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   NewHigherFilter.py
@Time    :   2020/12/27 21:22:08
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''

from Bear.columnsName import KW_CLOSE,KW_HIGH,KW_DATE
import pandas as pd

class CNewHigherFilter(object):
    def __init__(self):
        pass

    def checkParams(self,df):
        size = df.shape[0]
        if size < 180:
            return False

        return True

    def CheckNewHigh(self,df,columnName):
        df1 = pd.DataFrame(df,copy = True)
        columns = list(df1.columns)
        last = float(df1.iloc[-1][columnName])
        date = df1.iloc[-1][KW_DATE]
        if columnName not in columns:
            return (0,date)

        rows = df1.shape[0]
        N = 0
        for i in range(2, rows):
            if last < float(df1.iloc[-i][columnName]):
                break
            date = df1.iloc[-i][KW_DATE]
            N = N +1

        return (N,date)

    def doFilter(self,df):
        ret = {}
        if not self.checkParams(df):
            return (False,ret)
        
        (CloseNewHigh,closeDate) = self.CheckNewHigh(df,KW_CLOSE)
        (HighPriceNewHigh,HierPriceDate) = self.CheckNewHigh(df,KW_HIGH)
        ret['收盘价新高天数'] = CloseNewHigh
        ret['收盘价次高点日期'] = closeDate
        ret['最高价新高天数'] = HighPriceNewHigh
        ret['最高价次高点日期'] = HierPriceDate
        return (True,ret)
        


