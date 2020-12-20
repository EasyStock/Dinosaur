#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   stockInfoReaderTHSDB.py
@Time    :   2020/12/19 17:20:14
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''

import os
import sqlite3
import logging
import pandas as pd
import datetime

DBName = 'all_data_ths.db'
TABLE_NAME = 'AllDailyDataTHS'

logger = logging.getLogger()

def FetchDataWithSQL(sqliteConnection,sql):
    now = datetime.datetime.now()
    df = pd.read_sql_query(sql, sqliteConnection)
    now2 = datetime.datetime.now()
    logger.info('execute sql :%s cost: %s'%(sql,now2-now))
    return df

def ExecuteSQLTHS(dbFolder,sql):
    dbFullPath = os.path.join(dbFolder,DBName)
    df = None
    with sqlite3.connect(dbFullPath) as con:
        df = FetchDataWithSQL(con,sql)
    return df

def ReadFromTHSDB(dbFolder, sinceDate):
    sql = '''SELECT * FROM %s where date > '%s';'''%(TABLE_NAME,sinceDate)
    return ExecuteSQLTHS(dbFolder, sql)

def ReadFromTHSDBLastNDays(dbFolder, lastN):
    today = datetime.date.today()
    delta = datetime.timedelta(days=lastN)
    lastNDays = today - delta
    return ReadFromTHSDB(dbFolder, lastNDays)


if __name__ == "__main__":
    folder = '/Volumes/Data/Code/github/Dinosaur/data/'
    df = ReadFromTHSDBLastNDays(folder,3)
    print(df)
    print(df.columns)
