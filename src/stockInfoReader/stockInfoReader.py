#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   stockInfoReader.py
@Time    :   2020/12/08 21:32:24
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''


import tushare as ts
pro = ts.pro_api('6f1803e888430998ab4dcbe8ec3d8665b7900118c0042c14acb2c37d')

# data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
# print(data)

df = pro.daily(ts_code='000001.SZ,600000.SH', start_date='20180701', end_date='20180718')
print(df)

a = pro.index_daily(ts_code='399300.SZ')
print(a)