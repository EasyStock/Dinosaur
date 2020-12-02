#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   stockFormat.py
@Time    :   2020/10/31 20:26:15
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''

from stockKeyDef import stock_Date, stock_OpenPrice, stock_ClosePrice, stock_HighPrice, stock_LowerPrice,      \
    stock_Volumn, stock_Turnover, stock_ClosePrice_Yesterday,                             \
    stock_MA5, stock_MA10, stock_MA20, stock_MA30, stock_MA60, stock_MA120, stock_MA240,      \
    stock_OtherInfo, stock_Detail, stock_Details,                                                                          \
    stock_ID, stockName, stock_Days,

STOCK_BASE_ITEM_FORMAT = {
    stock_ID: "",
    stockName: "",
    stock_Days: "",
}

STOCK_ITEM_FORMAT = {
    stock_OpenPrice: "",
    stock_ClosePrice: "",
    stock_ClosePrice_Yesterday: "",
    stock_HighPrice: "",
    stock_LowerPrice: "",
    stock_Volumn: "",
    stock_Turnover: "",

    stock_MA5: "",
    stock_MA10: "",
    stock_MA20: "",
    stock_MA30: "",
    stock_MA60: "",
    stock_MA120: "",
    stock_MA240: "",
    stock_OtherInfo: "",
}

STOCK_INFO = {
    stock_ID: "",
    stock_Detail:STOCK_ITEM_FORMAT,
}

STOCK_INFOS = {
    stock_ID: "",
    stock_Details:[
        STOCK_ITEM_FORMAT,
    ],
}