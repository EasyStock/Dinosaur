#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   stockKeyValidate.py
@Time    :   2020/10/29 23:14:00
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''
import sys
import os
sys.path.append(os.getcwd()) 

import stockInfoFormatter.stockKeyDef as sk

def ValidateListDuplicate(destList):
    ls = list(set(destList))
    if len(ls) == len(destList):
        return
    res = []
    for key in destList:
        if key not in ls:
            res.append(key)
        else:
            ls.remove(key)

    print("duplicate key:", res)

    raise Exception('duplicate key Exception')


def validateColumn():
    ValidateListDuplicate(sk.all_Stock_keys)


def validateKeyWords():
    first = [key[0] for key in sk.stockKeyWordsMap]
    ValidateListDuplicate(first)

    second = [key[1] for key in sk.stockKeyWordsMap]
    ValidateListDuplicate(second)

    for key in sk.all_Stock_keys:
        if key not in second:
            raise Exception('miss key in second:%s' % (key))

    for key in second:
        if key not in sk.all_Stock_keys:
            raise Exception('miss key in columns:%s' % (key))


def validate():
    validateColumn()
    validateKeyWords()


def PrintKey():
    for item in sk.stockKeyWordsMap:
        msg = '{0:{3}<15}\t{1:^15}\t{2:<10}'.format(
            item[1], "----->", item[0], chr(12288), end='')
        print(msg)


def KeyConverTest():
    for key in sk.all_Stock_keys:
        value = sk.keyConverter(key)
        print('key: %s          convert to:          %s'%(key, value))

def shortNameTest():
    d = sk.toShortNameDict()
    print(d)

def longNameTest():
    d = sk.toLongNameDict()
    print(d)

if __name__ == "__main__":
    validate()
    PrintKey()
    KeyConverTest()
    shortNameTest()
    longNameTest()
