#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   reader_ths.py
@Time    :   2020/12/15 21:36:42
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''

import os
import re
import pandas as pd
import logging

from datafetcher.ths.constKeys import COLUMNS_MAP_THS, KEY_TABLE_NAME_THS, \
                    KEY_TABLE_NAME_THS_INSERTED,KW_ZHUBAN,KW_KECHUANG ,KW_CHUANG_YE ,KE_ZHONGXIAO,KEY_TABLE_NAME_THS_MARKET_HOT

class CReader_ths(object):
    def __init__(self):
        self.fileName = None
        self.date = None
        self.dataFrame = None
        self.logger = logging.getLogger()

    def keywordTranslator(self,dataframe_THS):
        columnsKeys = COLUMNS_MAP_THS.keys()
        dfKeys = dataframe_THS.columns
        retMap = {}
        firstCloseKey = None
        for key in columnsKeys:
            value = COLUMNS_MAP_THS[key]
            for dfKey in dfKeys:
                if dfKey.find('收盘价') != -1 and value.find('收盘价') != -1:
                    if firstCloseKey is None:
                        firstCloseKey = dfKey
                    else:
                        if dfKey > firstCloseKey:
                            retMap[key] = dfKey
                            retMap['pre_close'] = firstCloseKey
                        else:
                            retMap[key] = firstCloseKey
                            retMap['pre_close'] = dfKey
                        continue

                if re.match(value, dfKey) != None:
                    retMap[key] = dfKey

        return retMap

    @staticmethod
    def MarketName(sid):
        regStr = str(sid)
        if re.search('^60\d{4}.SH',regStr):
            return KW_ZHUBAN
        elif re.search('^68\d{4}.SH',regStr):
            return KW_KECHUANG
        elif re.search('^30\d{4}.SZ',regStr):
            return KW_CHUANG_YE
        elif re.search('^00\d{4}.SZ',regStr):
            return KE_ZHONGXIAO
        else:
            return 'UnKnown'

    def addMarketInfo(self):
        if self.dataFrame is None:
            return

        self.dataFrame['market'] = self.dataFrame.apply(lambda row : CReader_ths.MarketName(row['sid']), axis = 1)

    def translateTHSTo(self,filename):
        self.fileName = filename
        if filename.find('.xlsx') != -1:
            self.dataFrame = pd.read_excel(filename)
            self.date = self.dataFrame['date'][0]
        elif filename.find('.xls') != -1:
            dfs = pd.read_html(filename, encoding='utf-8',header=0)
            df = dfs[0]
            retMap = self.keywordTranslator(df)
            date = retMap['open'].split(')')[1].replace('.','-')
            self.dataFrame = pd.DataFrame(columns=retMap.keys())
            for key in retMap:
                self.dataFrame[key] = df[retMap[key]]
            self.dataFrame['date'] = date
            self.date = date
            self.addMarketInfo()
        else:
            raise Exception('read Exception!')

    @staticmethod
    def getInsertedFileNamesSQL():
        sql = '''select distinct fileName from %s;'''%(KEY_TABLE_NAME_THS_INSERTED)
        return sql

    @staticmethod
    def insertFileNameIntoSQL(fileName):
        sql = '''INSERT INTO %s VALUES ('%s')'''%(KEY_TABLE_NAME_THS_INSERTED,fileName)
        return sql

    def _insertToDB(self,con):
        if self.dataFrame is None:
            return
        dfNew = self.dataFrame.copy()
        dfNew = dfNew.set_index('sid')

        dfNew.to_sql(KEY_TABLE_NAME_THS, con, if_exists="append")
        self.logger.info('insert file:%s to DB finished: total: %s X %s'%(self.fileName, dfNew.shape[0],dfNew.shape[1]))

    def _GetRatioOf(self, df, column1, column2, key):
        totalSize = df.shape[0]
        if totalSize == 0:
            return {key:0.0}
        res = df[df[column1] >= df[column2]]
        ratio= round(float(1.0*res.shape[0]/df.shape[0]),3)
        return {
            key:ratio
        }

    def _GetRatioOfGreateThanConst(self, df, column1, constValue, key):
        totalSize = df.shape[0]
        if totalSize == 0:
            return {key:0.0}
        res = df[df[column1] >= constValue]
        ratio= round(float(1.0*res.shape[0]/df.shape[0]),3)
        return {
            key:ratio
        }

    def _GetRatioOfGreateLessConst(self, df, column1, constValue, key):
        totalSize = df.shape[0]
        if totalSize == 0:
            return {key:0.0}
        res = df[df[column1] <= constValue]
        ratio= round(float(1.0*res.shape[0]/df.shape[0]),3)
        return {
            key:ratio
        }

    def _Count(self, df):
        res = {}
        size_all = df.shape[0]
        res['total'] = size_all
        res['date'] = self.date
        df1 = pd.DataFrame(df, columns=('close','ma5','ma10','ma20', 'ma30', 'ma60', 'ma120', 'ma240','bollu','bolll','rsi6'),copy = True,dtype = float) 
        res.update(self._GetRatioOf(df1, 'close', 'ma5', 'raito_gt_ma5'))
        res.update(self._GetRatioOf(df1, 'close', 'ma10', 'raito_gt_ma10'))
        res.update(self._GetRatioOf(df1, 'close', 'ma20', 'raito_gt_ma20'))
        res.update(self._GetRatioOf(df1, 'close', 'ma30', 'raito_gt_ma30'))
        res.update(self._GetRatioOf(df1, 'close', 'ma60', 'raito_gt_ma60'))
        res.update(self._GetRatioOf(df1, 'close', 'ma120', 'raito_gt_ma120'))
        res.update(self._GetRatioOf(df1, 'close', 'ma240', 'raito_gt_ma240'))
        res.update(self._GetRatioOf(df1, 'close', 'bollu', 'raito_gt_bollup'))
        res.update(self._GetRatioOf(df1, 'bolll', 'close', 'raito_le_bolldown'))
        res.update(self._GetRatioOfGreateThanConst(df1, 'rsi6', 80, 'raito_gt_rsi80'))
        res.update(self._GetRatioOfGreateLessConst(df1, 'rsi6', 20, 'raito_ls_rsi20'))
        return res

    def _InsertMarketHotData(self,con, df,banKuaiName):
        res = self._Count(df)
        res['market'] = banKuaiName
        dfNew = pd.DataFrame.from_dict(res,orient='index')
        dfNew = dfNew.T
        dfNew = dfNew.set_index('date',drop = True)
        dfNew.to_sql(KEY_TABLE_NAME_THS_MARKET_HOT, con, if_exists="append")
        self.logger.info('insert market [%s] Hot Data to DB finished.'%(banKuaiName))

    def _UpdateMarketHotData(self,con, df,banKuaiName):
        res = self._Count(df)
        res['market'] = banKuaiName

        sql = 'UPDATE %s SET '%(KEY_TABLE_NAME_THS_MARKET_HOT)
        for key in res:
            sql = sql + ''''%s' = '%s', '''%(key,res[key])

        sql = sql[:-2]
        sql = sql + ''' WHERE date = '%s' AND market = '%s' '''%(self.date,banKuaiName)
        # print(sql)
        con.execute(sql)
        self.logger.info('update marketHotData to DB finished.')


    def _insertMarketHotDataToDB(self,con):
        if self.dataFrame is None:
            return

        dfNew = self.dataFrame.copy()
        dfNew = dfNew.replace('--', 9999)
        df_zhuban = dfNew[dfNew['market'] == KW_ZHUBAN]
        df_kechuang = dfNew[dfNew['market'] == KW_KECHUANG]
        df_chuangye = dfNew[dfNew['market'] == KW_CHUANG_YE]
        df_zhognxiao = dfNew[dfNew['market'] == KE_ZHONGXIAO]
        self._InsertMarketHotData(con,dfNew,'ALL')
        self._InsertMarketHotData(con,df_zhuban,KW_ZHUBAN)
        self._InsertMarketHotData(con,df_kechuang,KW_KECHUANG)
        self._InsertMarketHotData(con,df_chuangye,KW_CHUANG_YE)
        self._InsertMarketHotData(con,df_zhognxiao,KE_ZHONGXIAO)
    
    def _updateMarketHotDataToDB(self,con):
        if self.dataFrame is None:
            return

        dfNew = self.dataFrame.copy()
        dfNew = dfNew.replace('--', 9999)
        df_zhuban = dfNew[dfNew['market'] == KW_ZHUBAN]
        df_kechuang = dfNew[dfNew['market'] == KW_KECHUANG]
        df_chuangye = dfNew[dfNew['market'] == KW_CHUANG_YE]
        df_zhognxiao = dfNew[dfNew['market'] == KE_ZHONGXIAO]
        self._UpdateMarketHotData(con,dfNew,'ALL')
        self._UpdateMarketHotData(con,df_zhuban,KW_ZHUBAN)
        self._UpdateMarketHotData(con,df_kechuang,KW_KECHUANG)
        self._UpdateMarketHotData(con,df_chuangye,KW_CHUANG_YE)
        self._UpdateMarketHotData(con,df_zhognxiao,KE_ZHONGXIAO)

        
    def _updateToDB(self,con):
        if self.dataFrame is None:
            return
        dfNew = self.dataFrame.copy()
        cursor = con.cursor()
        for index, row in dfNew.iterrows():
            sql = 'UPDATE %s SET '%(KEY_TABLE_NAME_THS)
            for key in dfNew.columns:
                sql = sql + ''''%s' = '%s', '''%(key,row[key])
            sql = sql[:-2]
            sql = sql + ''' WHERE date = '%s' AND sid = '%s' '''%(row['date'],row['sid'])
            #print(sql)
            con.execute(sql)
        self.logger.info('update file:%s to DB finished: total: %s X %s'%(self.fileName, dfNew.shape[0],dfNew.shape[1]))

    def InsertData(self,fileName,con,destFolder):
        self.logger.info('begin: [%s]'%(fileName))
        try:
            self.translateTHSTo(fileName)
            self._insertToDB(con)
            self._insertMarketHotDataToDB(con)
            sql1 = CReader_ths.insertFileNameIntoSQL(fileName)
            con.execute(sql1)
            self.SaveToFile(destFolder)
            con.commit()
            self.logger.info('end: [%s]'%(fileName))
        except Exception as e:
            con.rollback()
            self.logger.error('exception: [%s],exception:%s'%(fileName,e))

    
    def UpdateData(self,fileName,con):
        self.logger.info('begin: [%s]'%(fileName))
        try:
            self.translateTHSTo(fileName)
            self._updateToDB(con)
            self._updateMarketHotDataToDB(con)
            con.commit()
            self.logger.info('end: [%s]'%(fileName))
        except Exception as e:
            con.rollback()
            self.logger.error('exception: [%s],exception:%s'%(fileName,e))
    

    def SaveToFile(self,folder):
        if self.dataFrame is None or self.date is None:
            return
        
        fileName = '%s.xlsx'%(self.date)
        fullPath = os.path.join(folder,fileName)
        df = self.dataFrame.copy()
        df = df.set_index('sid')
        df.to_excel(fullPath,encoding='utf-8',index = True)



