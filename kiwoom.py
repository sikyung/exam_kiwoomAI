import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *


class Kiwoom:
    def __init__(self):
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self._handle_login)
        self.ocx.OnReceiveTrData.connect(self._handle_tr)

    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")
        self.login_loop = QEventLoop()
        self.login_loop.exec()

    def _handle_login(self, err):
        self.login_loop.exit()

    def GetLoginInfo(self, tag):
        data = self.ocx.dynamicCall("GetLoginInfo(QString)", tag)
        return data

    def GetCodeListByMarket(self, market):
        data = self.ocx.dynamicCall("GetCodeListByMarket(QString)", market)
        codes = data.split(";")
        return codes[:-1]

    def GetMasterCodeName(self, code):
        data = self.ocx.dynamicCall("GetMasterCodeName(QString", code)
        return data

    def GetMasterListedStockDate(self, code):
        data = self.ocx.dynamicCall("GetMasterListedStockDate(QString", code)
        return data

    def GetMasterListedStockCnt(self, code):
        data = self.ocx.dynamicCall("GetMasterListedStockCnt(QString", code)
        return data


    def GetMasterLastPrice(self, code): # 전일 종가
        data = self.ocx.dynamicCall("GetMasterLastPrice(QString", code)
        return data

    def GetMasterConstruction(self, code): # 감리 구분
        data = self.ocx.dynamicCall("GetMasterConstruction(QString", code)
        return data

    def GetMasterStockState(self, code): # 종목 상태
        data = self.ocx.dynamicCall("GetMasterStockState(QString", code)
        return data

    def GetThemeGroupList(self, type):
        data = self.ocx.dynamicCall("GetThemeGroupList(int)", type)
        tokens = data.split(";")

        data_dic = {}
        for theme in tokens:
            code, name = theme.split("|")
            data_dic[code] = name
            if type == 0:
                data_dic[code] = name
            else:
                data_dic[name] = code

        return data_dic

    def GetThemeGroupCode(self, theme_code):
        data = self.ocx.dynamicCall("GetThemeGroupCode(QString)", theme_code)
        tokens = data.split(";")

        result =[]
        for code in tokens:
            result.append(code[1:])

        return result

    def SetInputValue(self, item, value):
        self.ocx.dynamicCall("SetInputValue(QString, QString)", item, value)

    def CommRqData(self, rqname, trcode, next, screen):
        self.ocx.dynamicCall("CommRqData(QString, QString, int, Qstring)", rqname, trcode, next, screen)
        self.tr_loop = QEventLoop()
        self.tr_loop.exec()

    def GetCommData(self, trcode, rqname, index, item):
        data = self.ocx.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, index, item)
        return data.strip()

    def _handle_tr(self, screen, rqname, trcode, record, next):
        self.tr_data = {}

        per = self.GetCommData(trcode, rqname, 0, "PER")
        pbr = self.GetCommData(trcode, rqname, 0, "PBR")
        self.tr_data["PER"] = per
        self.tr_data["PBR"] = pbr

        self.tr_loop.exit()

app = QApplication(sys.argv)

