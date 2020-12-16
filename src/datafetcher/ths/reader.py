#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   reader_ths.py
@Time    :   2020/12/15 21:36:42
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''

from os import read
import re
import pandas as pd
import logging

from datafetcher.ths.constKeys import COLUMNS_MAP_THS, KEY_TABLE_NAME_THS,CREATE_STOCK_TABLE_ALL_DATA, \
                    KEY_TABLE_NAME_THS_INSERTED,CREATE_STOCK_TABLE_INSERT_FILES

class CReader_ths(object):
    def __init__(self):
        self.fileName = None
        self.date = None
        self.dataFrame = None
        self.logger = logging.getLogger()

    def keywordTranslator(self,dataframe_THS):
        columnsKeys = COLUMNS_MAP_THS.keys()
        dfKeys = dataframe_THS.columns
        retMap = {}
        firstCloseKey = None
        for key in columnsKeys:
            value = COLUMNS_MAP_THS[key]
            for dfKey in dfKeys:
                if dfKey.find('收盘价') != -1 and value.find('收盘价') != -1:
                    if firstCloseKey is None:
                        firstCloseKey = dfKey
                    else:
                        if dfKey > firstCloseKey:
                            retMap[key] = dfKey
                            retMap['pre_close'] = firstCloseKey
                        else:
                            retMap[key] = firstCloseKey
                            retMap['pre_close'] = dfKey
                        continue

                if re.match(value, dfKey) != None:
                    retMap[key] = dfKey

        return retMap

    def translateTHSTo(self,filename):
        self.fileName = filename
        dfs = pd.read_html(filename, encoding='utf-8',header=0)
        df = dfs[0]
        retMap = self.keywordTranslator(df)
        date = retMap['open'].split(')')[1].replace('.','-')
        self.dataFrame = pd.DataFrame(columns=retMap.keys())
        for key in retMap:
            self.dataFrame[key] = df[retMap[key]]
        self.dataFrame['date'] = date
        self.date = date

    @staticmethod
    def getInsertedFileNamesSQL():
        sql = '''select distinct fileName from %s;'''%(KEY_TABLE_NAME_THS_INSERTED)
        return sql

    @staticmethod
    def insertFileNameIntoSQL(fileName):
        sql = '''INSERT INTO %s VALUES ('%s')'''%(KEY_TABLE_NAME_THS_INSERTED,fileName)
        return sql

    def _insertToDB(self,con):
        if self.dataFrame is None:
            return
        dfNew = self.dataFrame.copy()
        dfNew = dfNew.set_index('sid')
        cursor = con.cursor()
        dfNew.to_sql(KEY_TABLE_NAME_THS, con, if_exists="append")
        con.commit()
        self.logger.info('insert file:%s to DB finished: total: %s X %s'%(self.fileName, dfNew.shape[0],dfNew.shape[1]))

    
    def _updateToDB(self,con):
        if self.dataFrame is None:
            return
        dfNew = self.dataFrame.copy()
        cursor = con.cursor()
        for index, row in dfNew.iterrows():
            sql = 'UPDATE %s SET '%(KEY_TABLE_NAME_THS)
            for key in dfNew.columns:
                sql = sql + ''''%s' = '%s', '''%(key,row[key])
            sql = sql[:-2]
            sql = sql + '''WHERE date = '%s' AND sid = '%s' '''%(row['date'],row['sid'])
            #print(sql)
            con.execute(sql)
            con.commit()
        self.logger.info('update file:%s to DB finished: total: %s X %s'%(self.fileName, dfNew.shape[0],dfNew.shape[1]))

    def InsertData(self,fileName,con):
        self.logger.info(fileName)
        self.translateTHSTo(fileName)
        self._insertToDB(con)

    
    def UpdateData(self,fileName,con):
        self.logger.info(fileName)
        self.translateTHSTo(fileName)
        self._updateToDB(con)
    




