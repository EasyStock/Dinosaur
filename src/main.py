#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2020/10/29 22:37:13
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''

import logging

import os
print(os.getcwd())
from ColoredLog import InitLogger
import datetime

def StartToInitLogger():
    folder = '/tmp/'
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    fullPath = os.path.join(folder,'%s.txt'%(now))
    logger = InitLogger(fullPath)
    return logger



if __name__ == "__main__":
    logger = StartToInitLogger()
    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.error("Finish")