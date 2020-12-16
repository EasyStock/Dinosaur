#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   THSCONST.py
@Time    :   2020/12/16 21:10:23
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''

COLUMNS_MAP_THS = {
    'sid' : '^股票代码',
    'date' : '^日期',
    'open' : '^开盘价',
    'close' : '^收盘价',
    'low' : '^最低价',
    'high': '^最高价',
    'pre_close': '^昨日收盘价',
    'vol': '^成交量',
    'turnover': '^成交额',
    'ma5': '^5日均线',
    'ma10': '^10日均线',
    'ma20': '^20日均线',
    'ma30': '^30日均线',
    'ma60': '^60日均线',
    'ma120': '^120日均线',
    'ma240': '^240日均线',
    'macd': '^macd\(macd值\)',
    'bollu': '^boll\(upper值\)',
    'bollm': '^boll\(mid值\)',
    'bolll': '^boll\(lower值\)',
    'rsi6': '^rsi\(rsi6值\)',
    'rsi12': '^rsi\(rsi12值\)',
    'rsi24': '^rsi\(rsi24值\)',
}

KEY_TABLE_NAME_THS = 'AllDailyDataTHS'
KEY_TABLE_NAME_THS_INSERTED = 'InsertFiles'

CREATE_STOCK_TABLE_ALL_DATA = '''
CREATE TABLE IF NOT EXISTS %s (
    date      TEXT     NOT NULL,
    sid       TEXT     NOT NULL,
    open      NUMERIC,
    close     NUMERIC,
    low       NUMERIC,
    high      NUMERIC,
    pre_close NUMERIC,
    vol       NUMERIC,
    turnover  NUMERIC,
    ma5       NUMERIC DEFAULT ( -9999),
    ma10      NUMERIC DEFAULT ( -9999),
    ma20      NUMERIC DEFAULT ( -9999),
    ma30      NUMERIC DEFAULT ( -9999),
    ma60      NUMERIC DEFAULT ( -9999),
    ma120     NUMERIC DEFAULT ( -9999),
    ma240     NUMERIC DEFAULT ( -9999),
    macd      NUMERIC DEFAULT ( -9999),
    bollu     NUMERIC DEFAULT ( -9999),
    bollm     NUMERIC DEFAULT ( -9999),
    bolll     NUMERIC DEFAULT ( -9999),
    rsi6      NUMERIC DEFAULT ( -9999),
    rsi12     NUMERIC DEFAULT ( -9999),
    rsi24     NUMERIC DEFAULT ( -9999),
    PRIMARY KEY(date,sid)
);
'''%(KEY_TABLE_NAME_THS)

CREATE_STOCK_TABLE_INSERT_FILES = '''
CREATE TABLE IF NOT EXISTS %s (
    fileName  TEXT     NOT NULL,
    PRIMARY KEY(fileName)
);
'''%(KEY_TABLE_NAME_THS_INSERTED)
