#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tushareBasic.py
@Time    :   2020/12/08 22:51:07
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''

import datetime
import sqlite3
import tushare as ts

def fetchTradingDayTillNow(pro,start_date='20150101'):
    now = datetime.datetime.now()
    year = now.year
    end_date = '%04d1231'%(year)
    df = pro.trade_cal(exchange='', start_date=start_date, end_date=end_date)
    trading_days_tillNow = list(df[df['is_open'] == 1]['cal_date'])
    print(trading_days_tillNow)
    return trading_days_tillNow

def fetchStockBasicInfoTillNow(pro):
    '''
        ts_code	str	TS代码
        symbol	str	股票代码
        name	str	股票名称
        area	str	所在地域
        industry	str	所属行业
        fullname	str	股票全称
        enname	str	英文全称
        market	str	市场类型 （主板/中小板/创业板/科创板/CDR）
        exchange	str	交易所代码
        curr_type	str	交易货币
        list_status	str	上市状态： L上市 D退市 P暂停上市
        list_date	str	上市日期
        delist_date	str	退市日期
        is_hs	str	是否沪深港通标的，N否 H沪股通 S深股通
    '''
    columns = ('ts_code','exchange','symbol','name','fullname','area','industry','list_date','is_hs')
    data = pro.stock_basic(exchange='', list_status='L', fields=columns)#'ts_code,symbol,name,fullname,area,industry,list_date,is_hs')
    print(data)
    print(data.columns)
    return data


if __name__ == "__main__":
    pro = ts.pro_api('6f1803e888430998ab4dcbe8ec3d8665b7900118c0042c14acb2c37d')
    fetchStockBasicInfoTillNow(pro)