#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Thermometer.py
@Time    :   2020/12/20 09:38:52
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''
import re

KW_ZHUBAN = "主  板"
KW_KECHUANG = "科创板"
KW_CHUANG_YE = "创业板"
KE_ZHONGXIAO = "中小板"
KW_ALL = "全部"

class MakrketHot(object):
    def __init__(self,allHistoryData):
        self.allHistoryData = allHistoryData
        self.groupedHistoryData = {
            KW_ZHUBAN:[],
            KW_KECHUANG:[],
            KW_CHUANG_YE:[],
            KE_ZHONGXIAO:[],
            KW_ALL:[],
        }

    def GroupHistoryData(self):
        if self.allHistoryData is None:
            return None
        
        for stockID in self.allHistoryData:
            stockData = self.allHistoryData[stockID]
            if re.search('^60\d{4}.SH'):
                self.groupedHistoryData[KW_ZHUBAN].append(stockData)
            elif re.search('^^68\d{4}.SH'):
                self.groupedHistoryData[KW_KECHUANG].append(stockData)
            elif re.search('^30\d{4}.SZ'):
                self.groupedHistoryData[KW_CHUANG_YE].append(stockData)
            elif re.search('^00\d{4}.SZ'):
                self.groupedHistoryData[KE_ZHONGXIAO].append(stockData)
            else:
                raise Exception('unknown type')

            self.groupedHistoryData[KW_ALL].append(self.allHistoryData[stockID])

    