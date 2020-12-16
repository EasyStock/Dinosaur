#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tushareMain.py
@Time    :   2020/12/10 21:24:10
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''

from dataSource.tushare.tushareBasic import fetchTradingDayTillNow,fetchStockBasicInfoTillNow
import tushare as ts
from dataSource.tushare.tushareToken import MY_TOKEN
from dataSource.tushare.tushareHistory import fetchStockHistoryMonthly,fetchStockHistoryByMonth,fetchStockHistoryMonthlyAAA

    
if __name__ == "__main__":
    pro = ts.pro_api(MY_TOKEN)
    basicInfo = fetchStockBasicInfoTillNow(pro)
    folder = '/tmp/11/'
    fetchStockHistoryMonthlyAAA(pro,basicInfo,(2018,2019,2020),folder)
    #fetchStockHistoryByMonth(pro, '000001.SZ','000001', 2020, 1, folder, adj='qfq',asset = 'E')