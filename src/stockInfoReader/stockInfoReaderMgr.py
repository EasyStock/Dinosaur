#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   stockInfoReaderMgr.py
@Time    :   2020/12/19 17:46:18
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''
import datetime
import logging
import concurrent.futures

from stockInfoReader.stockInfoReaderTHSDB import ReadFromTHSDBLastNDays,ReadFromTHSDB,ExecuteSQLTHS
THS_DB_FOLDER = '/Volumes/Data/Code/github/Dinosaur/data/'

logger = logging.getLogger()

def ExecuteSQL(sql):
    return ExecuteSQLTHS(THS_DB_FOLDER,sql)

def ReadFromDBSince(sinceDate):
    return ReadFromTHSDB(THS_DB_FOLDER,sinceDate)

def ReadFromDBLastN(lastNDays):
    return ReadFromTHSDBLastNDays(THS_DB_FOLDER,lastNDays)

def GetStockIDs():
    sql = ''' SELECT distinct sid FROM AllDailyDataTHS;'''
    stockIDs = ExecuteSQL(sql)
    return stockIDs

def _SplitFun(dataframe, stockID):
    data = dataframe[dataframe['sid'] == stockID].copy()
    #print(stockID)
    return {stockID:data}
    
def GetSplitedDataFrame(lastNDays):
    now = datetime.datetime.now()
    allHistorieData =  ReadFromDBLastN(lastNDays)
    stockIDs = list(allHistorieData['sid'].drop_duplicates())
    res = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=32) as executor:
        futures = [executor.submit(_SplitFun, allHistorieData,stockID) for stockID in stockIDs]
        for future in concurrent.futures.as_completed(futures):
                res.update(future.result())
    now2 = datetime.datetime.now()
    logger.info('GetSplitedDataFrame cost: %s'%(now2-now))
    return res
    
