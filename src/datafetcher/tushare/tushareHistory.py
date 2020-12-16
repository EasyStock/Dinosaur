#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tushareHistory.py
@Time    :   2020/12/09 22:04:30
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''

import os
import tushare as ts
import time
import datetime
import multiprocessing
from dataSource.tushare.tushareToken import MY_TOKEN

def fetchStockHistoryByMonth(pro, ts_code,stockID, year, month, folder, adj='qfq',asset = 'E'):
    pro1 = ts.pro_api(MY_TOKEN)
    start_date = '%04d%02d01'%(year, month)
    end_date = '%04d%02d31'%(year, month)
    print(start_date,end_date, "BBB")
    print(ts_code,stockID, year, month, folder, adj,asset)
    df = None
    for _ in range(3):
        try:
            df = ts.pro_bar(ts_code=ts_code,api =pro1, adj=adj, start_date=start_date,end_date = end_date,asset=asset)
            break
        except Exception as e:
            print(e)
            time.sleep(1)

    filename = '%s_%04d%02d.xlsx'%(stockID,year, month)
    fullname = os.path.join(folder, filename)
    print(fullname)
    df.to_excel(fullname ,encoding="utf_8_sig", index=False)


def PreparefetchStockHistoryParam(ts_code, stockID,year,month,folder):
    subFolder = os.path.join(folder,stockID,str(year))
    if os.path.exists(subFolder) == False:
        os.makedirs(subFolder)
    
    return (ts_code, stockID,year,month,subFolder)

def PreparefetchStockHistoryParamAll(basicInfo,years,folder):
    now = datetime.datetime.now()
    crrrentYear = now.year
    currentMonth = now.month
    ret = []
    for _, row in basicInfo.iterrows():
        ts_code = row['ts_code']
        stockID = row['symbol']
        for year in years:
            for month in range(1,13):
                if year == crrrentYear and month > currentMonth:
                    continue
                res = PreparefetchStockHistoryParam(ts_code,stockID,year,month,folder)
                ret.append(res)
    return ret


def fetchStockHistoryMonthly(pro,basicInfo,years,folder, adj='qfq',asset = 'E'):
    print('AAAAA')
    res = PreparefetchStockHistoryParamAll(basicInfo,years,folder)
    pool = multiprocessing.Pool(multiprocessing.cpu_count()*2) 
    for item in res:
        (ts_code,stockID, year, month, folder) = item
        print(item)
        pool.apply_async(fetchStockHistoryByMonth, (pro, ts_code,stockID,year,month, folder,adj,asset))

    pool.close()
    pool.join()


def fetchStockHistoryMonthlyAAA(pro,basicInfo,years,folder, adj='qfq',asset = 'E'):
    res = PreparefetchStockHistoryParamAll(basicInfo,years,folder)
    for item in res:
        (ts_code,stockID, year, month, folder) = item
        fetchStockHistoryByMonth(pro, ts_code,stockID,year,month, folder,adj,asset)