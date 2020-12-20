#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2020/12/07 22:13:14
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''
import datetime
from ColoredLog import InitLogger
import os

from stockInfoReader.stockInfoReaderMgr import GetSplitedDataFrame

def StartToInitLogger():
    folder = '/tmp/'
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    fullPath = os.path.join(folder,'%s.txt'%(now))
    logger = InitLogger(fullPath)
    return logger

def Test():
    fileName = '/Volumes/Data/Code/github/2020-12-18.xlsx'
    import pandas as pd
    df = pd.read_excel(fileName)
    print(df.columns,df.shape)
    dfNew = df.replace('--', 9999)
    dfMa5 = dfNew[dfNew['收盘价:不复权(元)2020.12.18'] >= dfNew['5日均线2020.12.18']]
    print(1.0*dfMa5.shape[0] / df.shape[0])
    dfMa10 = dfNew[dfNew['收盘价:不复权(元)2020.12.18'] >= dfNew['10日均线2020.12.18']]
    print(1.0*dfMa10.shape[0] / df.shape[0])
    dfMa10 = dfNew[dfNew['收盘价:不复权(元)2020.12.18'] >= dfNew['20日均线2020.12.18']]
    print(1.0*dfMa10.shape[0] / df.shape[0])
    dfMa10 = dfNew[dfNew['收盘价:不复权(元)2020.12.18'] >= dfNew['30日均线2020.12.18']]
    print(1.0*dfMa10.shape[0] / df.shape[0])
    dfMa10 = dfNew[dfNew['收盘价:不复权(元)2020.12.18'] >= dfNew['60日均线2020.12.18']]
    print(1.0*dfMa10.shape[0] / df.shape[0])
    dfMa10 = dfNew[dfNew['收盘价:不复权(元)2020.12.18'] >= dfNew['120日均线2020.12.18']]
    print(1.0*dfMa10.shape[0] / df.shape[0])
    dfMa10 = dfNew[dfNew['收盘价:不复权(元)2020.12.18'] >= dfNew['240日均线2020.12.18']]
    print(1.0*dfMa10.shape[0] / df.shape[0])
    dfMa10 = dfNew[dfNew['收盘价:不复权(元)2020.12.18'] >= dfNew['boll(upper值)2020.12.18']]
    print(1.0*dfMa10.shape[0] / df.shape[0])
    dfMa10 = dfNew[dfNew['收盘价:不复权(元)2020.12.18'] <= dfNew['boll(lower值)2020.12.18']]
    print(1.0*dfMa10.shape[0] / df.shape[0])
    dfMa10 = dfNew[dfNew['rsi(rsi6值)2020.12.18'] >= 80]
    print(1.0*dfMa10.shape[0] / df.shape[0])
    dfMa10 = dfNew[dfNew['rsi(rsi6值)2020.12.18'] <= 20]
    print(1.0*dfMa10.shape[0] / df.shape[0])

if __name__ == "__main__":
    StartToInitLogger()
    #GetSplitedDataFrame(180)
    Test()