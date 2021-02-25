import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *


class Kiwoom:
    def __init__(self):
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self._handle_login)

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


app = QApplication(sys.argv)

