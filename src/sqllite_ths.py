#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sqllite_ths.py
@Time    :   2020/12/15 22:40:50
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''


from ColoredLog import InitLogger
import datetime
import os

from datafetcher.ths.readerMgr import CReaderMgr
from Bear.MakrketingThremometer import CMakrketingThremometer

dbName = '/Volumes/Data/Code/github/Dinosaur/data/all_data_ths.db'

def StartToInitLogger():
    folder = '/tmp/'
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    fullPath = os.path.join(folder,'%s.txt'%(now))
    logger = InitLogger(fullPath)
    return logger

def TestingMakrketingTemperature(dbName):
    market = CMakrketingThremometer()
    market.CalcMakrketingTemperature(dbName)

def StoreDailyToDB(dbName):
    srcFolder = '/Volumes/Data/Code/github/股票'
    destFolder = '/Volumes/Data/Code/github/AA'
    mgr = CReaderMgr()
    mgr.InsertDataWithFolder(srcFolder,dbName,destFolder)

if __name__ == "__main__":
    StartToInitLogger()
    StoreDailyToDB(dbName)
    TestingMakrketingTemperature(dbName)
    
    # srcFolder = '/Volumes/Data/Code/github/股票'
    # destFolder = '/Volumes/Data/Code/github/AA'
    # mgr = CReaderMgr()
    # mgr.InsertDataWithFolder(srcFolder,dbName,destFolder)
    #mgr.InsertDataWithFolder(destFolder,dbName,'/tmp/AAA')
    #mgr.UpdateDataWithFolder(srcFolder,dbName)



