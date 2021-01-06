#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Thermometer.py
@Time    :   2020/12/20 09:38:52
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''
import sqlite3
import pandas as pd
import logging
import datetime

KW_ZHUBAN = "主板"
KW_KECHUANG = "科创板"
KW_CHUANG_YE = "创业板"
KW_ZHONGXIAO = "中小板"
KW_ALL = "ALL"
KW_TABLE_NAME = 'MarketHot'
lastN = 365

logger = logging.getLogger()

    # total       NUMERIC DEFAULT (0),
    # raito_gt_ma5   NUMERIC DEFAULT (0),
    # raito_gt_ma10  NUMERIC DEFAULT (0),
    # raito_gt_ma20  NUMERIC DEFAULT (0),
    # raito_gt_ma30  NUMERIC DEFAULT (0),
    # raito_gt_ma60  NUMERIC DEFAULT (0),
    # raito_gt_ma120 NUMERIC DEFAULT (0),
    # raito_gt_ma240 NUMERIC DEFAULT (0),
    # raito_gt_bollup NUMERIC DEFAULT (0),
    # raito_le_bolldown NUMERIC DEFAULT (0),
    # raito_gt_rsi80 NUMERIC DEFAULT (0),
    # raito_ls_rsi20 NUMERIC DEFAULT (0),

class CMakrketingThremometer(object):
    def __init__(self):
        pass

    def formatSelectSql(self, banKuai):
        today = datetime.date.today()
        delta = datetime.timedelta(days=lastN)
        lastNDays = today - delta
        sql = '''SELECT date,raito_gt_ma5, raito_gt_ma10,raito_gt_bollup, raito_le_bolldown, raito_gt_rsi80, raito_ls_rsi20 FROM %s where market like '%%%s%%' AND date > '%s';''' % (KW_TABLE_NAME, banKuai,str(lastNDays))
        print(sql)
        return sql

    def QueryData(self, dbName, sql):
        with sqlite3.connect(dbName) as con:
            df = pd.read_sql_query(sql, con)
            df =df.set_index('date')
            return df

    def PrintMakrketingTemperature(self, banKuai, df):
        # logger.info("\n\n\n=============平均值 %s================" % (banKuai))
        # logger.info('\n%s\n\n'%(df.mean()))
        logger.info("\n\n\n=============分为数 %s================" % (banKuai))
        logger.info("\n%s\n\n"%(df.quantile(
            [0.05, 0.08, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.98])))

        logger.info("\n\n\n=============%s================" % (banKuai))
        logger.error("\n%s\n\n"%(df.tail(5)))

    def Testing(self, dbName, banKuai):
        sql = self.formatSelectSql(banKuai)
        df = self.QueryData(dbName, sql)
        if df is not None:
            self.PrintMakrketingTemperature(banKuai, df)

    def CalcMakrketingTemperature(self, dbName):
        self.Testing(dbName, KW_ALL)
        self.Testing(dbName, KW_ZHONGXIAO)
        self.Testing(dbName, KW_KECHUANG)
        self.Testing(dbName, KW_CHUANG_YE)
        self.Testing(dbName, KW_ZHUBAN)
