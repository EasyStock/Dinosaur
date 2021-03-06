#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   readerTHSMgr.py
@Time    :   2020/12/16 21:40:57
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''
import sqlite3
import os
import logging

from datafetcher.ths.constKeys import CREATE_STOCK_TABLE_ALL_DATA,CREATE_STOCK_TABLE_INSERT_FILES,CREATE_STOCK_TABLE_MARKET_HOT
from datafetcher.ths.reader import CReader_ths

class CReaderMgr(object):
    def __init__(self):
        self.logger = logging.getLogger()
    
    def createTablesIfNeeded(self,con):
        con.execute(CREATE_STOCK_TABLE_ALL_DATA)
        con.execute(CREATE_STOCK_TABLE_INSERT_FILES)
        con.execute(CREATE_STOCK_TABLE_MARKET_HOT)
        con.commit()

    def InsertDataWithFiles(self,fileNames,con,destFolder):
        self.createTablesIfNeeded(con)
        
        sql = CReader_ths.getInsertedFileNamesSQL()
        res = con.execute(sql).fetchall()
        insertedFiles = [item[0] for item in res]

        for filename in fileNames:
            if filename in insertedFiles:
                self.logger.warning('file:%s already inserted !' %(filename))
                continue
            reader = CReader_ths()
            reader.InsertData(filename,con,destFolder)


    def InsertDataWithFile(self,fileName,dbName,destFolder):
        with sqlite3.connect(dbName) as con:
            self.createTablesIfNeeded(con)
            reader = CReader_ths()
            reader.InsertData(fileName, con,destFolder)
            reader.insertFileNameInto(fileName)

    def InsertDataWithFolder(self, srcFolder, dbName,destFolder):
        fileList = os.listdir(srcFolder)
        allFileNames = []
        if os.path.exists(destFolder) == False:
            os.makedirs(destFolder)

        for filename in fileList:
            if filename.find('.xls') == -1:
                continue
            fullName = os.path.join(srcFolder, filename)
            allFileNames.append(fullName)
        
        with sqlite3.connect(dbName) as con:
            self.InsertDataWithFiles(allFileNames,con,destFolder)


    def UpdateDataWithFiles(self,fileNames,con):
        for filename in fileNames:
            reader = CReader_ths()
            reader.UpdateData(filename,con)

    def UpdateDataWithFolder(self, srcFolder, dbName):
        fileList = os.listdir(srcFolder)
        allFileNames = []
        for filename in fileList:
            if filename.find('.xls') == -1:
                continue
            fullName = os.path.join(srcFolder, filename)
            allFileNames.append(fullName)
        
        with sqlite3.connect(dbName) as con:
            self.UpdateDataWithFiles(allFileNames,con)