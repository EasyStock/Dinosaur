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


file1 =  '/Volumes/Data/Downloads/2020-12-03.xlsx'
file2 =  '/Volumes/Data/Downloads/2020-12-02.xlsx'
file3 =  '/Volumes/Data/Downloads/2020-12-01.xlsx'

file4 =  '/Volumes/Data/Downloads/1111111.xlsx'
df4 =  pd.read_excel(file4,index_col = None, encoding='utf_8_sig')
print(df4)
print(df4.index)
print(df4.columns)
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