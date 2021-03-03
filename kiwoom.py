import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *


class Kiwoom:
    def __init__(self):
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self._handle_login)
        self.ocx.OnReceiveTrData.connect(self._handle_tr)
        # self.ocx.OnReceiveChejanData.connect(self._)
        self.ocx.OnReceiveMsg.connect(self._handler_msg)
        self.ocx.OnReceiveConditionVer.connect(self._handler_condition_load)
        self.ocx.OnReceiveTrCondition.connect(self._handler_tr_condition)

    def _handler_tr_condition(self, screen, codelist, cond_name, cond_index, next):
        codes = codelist.split(';')
        self.codition_codes = codes[:-1]

        self.codition_tr_loop.exit()

    def _handler_msg(self, screen, rqname, trcode, msg):
        print("OnReceiveMsg: ", screen, rqname, trcode, msg)

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
        # self.tr_data = {}
        # per = self.GetCommData(trcode, rqname, 0, "PER")
        # pbr = self.GetCommData(trcode, rqname, 0, "PBR")
        # self.tr_data["PER"] = per
        # self.tr_data["PBR"] = pbr

        if next == '2':
            self.remained = True
        else:
            self.remained = False

        if rqname == "opt10081":
            self._opt10081(rqname, trcode)

        try:
            self.tr_loop.exit()
        except:
            pass

    def GetRepeatCnt(self, trcode, rqname):
        ret = self.ocx.dynamicCall("GetRepeatCnt(QString, QString", trcode, rqname)
        return ret

    def _opt10081(self, rqname, trcode):
        rows = self.GetRepeatCnt(trcode, rqname)
        for i in range(rows):
            date = self.GetCommData(trcode, rqname, i, "일자")
            open = self.GetCommData(trcode, rqname, i, "시가")
            high = self.GetCommData(trcode, rqname, i, "고가")
            low = self.GetCommData(trcode, rqname, i, "저가")
            close = self.GetCommData(trcode, rqname, i, "현재가")
            volume = self.GetCommData(trcode, rqname, i, "거래량")
            print(date, open, high, low, close, volume)

    def _handler_condition_load(self, ret, msg):
        print("OnReceiveConditionVer: ", ret, msg)
        self.condition_load_loop.exit()

    def GetConditionLoad(self):
        self.ocx.dynamicCall("GetConditionLoad()")

        self.condition_load_loop = QEventLoop()
        self.condition_load_loop.exec()

    def GetConditionNameList(self): # 키움 조건식 리스트 불러오기 [중요]
        data = self.ocx.dynamicCall("GetConditionNameList()")
        conditions = data.split(";")[:-1]

        ret = []
        for condition in conditions:
            index, name = condition.split('^')
            ret.append((index, name))

        return ret

    def SendCondition(self, screen, cond_name, cond_index, search): # 조건 검색 종목 불러오기
        self.ocx.dynamicCall("SendCondition(QString, QString, int, int)",screen, cond_name, cond_index, search)

        # event loop
        self.codition_tr_loop = QEventLoop()
        self.codition_tr_loop.exec()

app = QApplication(sys.argv)

