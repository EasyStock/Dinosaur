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

def StartToInitLogger():
    folder = '/tmp/'
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    fullPath = os.path.join(folder,'%s.txt'%(now))
    logger = InitLogger(fullPath)
    return logger

if __name__ == "__main__":
    StartToInitLogger()
    destfolder = '/Volumes/Data/Code/github/Dinosaur/data'
    srcFolder = '/Volumes/Data/Code/github/股票'
    dbName = '/tmp/all_data_ths.db'
    mgr = CReaderMgr()
    mgr.InsertDataWithFolder(srcFolder,dbName)
    #mgr.UpdateDataWithFolder(srcFolder,dbName)


