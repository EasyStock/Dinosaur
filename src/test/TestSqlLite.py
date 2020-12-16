#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   TestSqlLite.py
@Time    :   2020/12/03 22:35:28
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''

import sqlite3
import pandas as pd


# file1 =  '/Volumes/Data/Downloads/2020-12-03.xlsx'
# file2 =  '/Volumes/Data/Downloads/2020-12-02.xlsx'
# file3 =  '/Volumes/Data/Downloads/2020-12-01.xlsx'

# file4 =  '/Volumes/Data/Downloads/1111111.xlsx'
# df4 =  pd.read_excel(file4,index_col = None, encoding='utf_8_sig')
# print(df4)
# print(df4.index)
# print(df4.columns)
# df1 =  pd.read_excel(file1,index_col = None, encoding='utf_8_sig')
# df1['date'] = '2020-12-03'
# df2 =  pd.read_excel(file2,index_col = None, encoding='utf_8_sig')
# df2['date'] = '2020-12-02'
# df3 =  pd.read_excel(file3,index_col = None, encoding='utf_8_sig')
# df3['date'] = '2020-12-01'


# with sqlite3.connect(":memory:") as con:
#     c = con.cursor()
#     df1.to_sql("voters", con)
#     df2.to_sql("voters", con, if_exists="append")
#     df3.to_sql("voters", con, if_exists="append")
#     dfaaa = pd.read_sql_query('''select * from voters where date >= "2020-12-02" order by 股票代码''',con)
    
#     print(dfaaa)
#     dfaaa.to_excel('/tmp/bbbb.xlsx',index=False)

# area	str	所在地域
# industry	str	所属行业
# fullname	str	股票全称
# enname	str	英文全称
# market	str	市场类型 （主板/中小板/创业板/科创板/CDR）
# exchange	str	交易所代码
# curr_type	str	交易货币
# list_status	str	上市状态： L上市 D退市 P暂停上市
# list_date	str	上市日期
# delist_date	str	退市日期
# is_hs	str	是否沪深港通标的，N否 H沪股通 S深股通

with sqlite3.connect("/tmp/stockInfo.db") as con:
    drop = '''DROP TABLE StockBasicInfo;'''

    sql1 = '''
        CREATE TABLE StockBasicInfo(
            SID                     TEXT    PRIMARY KEY     NOT NULL,
            SNAME                   TEXT,    
            AREA                    TEXT,   
            INDUSTRY                TEXT,   
            FULLNAME                TEXT,    
            ENAME                   TEXT,    
            MARKET                  TEXT,    
            STATUS                  INT ,  
            LIST_DATE               TEXT,    
            IS_HS                   INT,
            BANKUAI                 TEXT  
            );
        '''
    cur = con.cursor()
    cur.execute(drop)
    cur.execute(sql1)

    insert = '''INSERT INTO StockBasicInfo (SID, SNAME,FULLNAME,IS_HS) VALUES ('AAAA','BBB','CCC',1)'''
    cur.execute(insert)

    query = 'SELECT * FROM StockBasicInfo'
    cur.execute(query)
    print(cur.description)
    res = cur.fetchall()
    print(res)
    # dfaaa = pd.read_sql_query(query,con)
    # print(dfaaa)

