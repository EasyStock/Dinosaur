#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tushareBasic.py
@Time    :   2020/12/08 22:51:07
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''

import tushare as ts
from tushareToken import MY_TOKEN
import datetime

def fetchTradingDayTillNow(pro,start_date='20150101'):
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    end_date = '%04d%02d%02d'%(year,month,day)
    df = pro.trade_cal(exchange='', start_date=start_date, end_date=end_date)
    trading_days_tillNow = list(df[df['is_open'] == 1]['cal_date'])
    print(trading_days_tillNow)
    return trading_days_tillNow

def fetchStockBasicInfoTillNow(pro):
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,fullname,area,industry,list_date,is_hs')
    print(data)
    data.to_excel('/tmp/aa.xlsx',encoding="utf_8_sig", index=False)

if __name__ == "__main__":
    pro = ts.pro_api(MY_TOKEN)
    fetchTradingDayTillNow(pro)
    fetchStockBasicInfoTillNow(pro)