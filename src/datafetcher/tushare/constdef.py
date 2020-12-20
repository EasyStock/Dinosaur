#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   constdef.py
@Time    :   2020/12/19 11:20:38
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''

BASIC_TABLE_NAME = 'basicInfo'
CREATE_STOCK_TABLE_BASIC_INFO = '''
CREATE TABLE IF NOT EXISTS %s (
    sid       TEXT     NOT NULL,
    name       TEXT     NOT NULL,
    area       TEXT     NOT NULL,
    industry       TEXT     NOT NULL,
    fullname       TEXT     NOT NULL,
    list_date       TEXT,
    bankuai TEXT,
    PRIMARY KEY(sid)
);
'''%(BASIC_TABLE_NAME)

if __name__ == "__main__":
    print(CREATE_STOCK_TABLE_BASIC_INFO)
