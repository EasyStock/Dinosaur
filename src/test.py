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

if __name__ == "__main__":
    StartToInitLogger()
    GetSplitedDataFrame(180)