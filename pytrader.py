from kiwoom import *
import pickle
import pprint
import time


class PyTrader:

    def __init__(self):
        self.kiwoom = Kiwoom()
        self.kiwoom.CommConnect()

    # data.db를 읽어서 해당 종목 리스트에 있는 종목을 시장가로 매수
    def run(self):
        accounts = self.kiwoom.GetLoginInfo("ACCNO")
        print(accounts)
        account = accounts.split(';')[0]

        try:
            f = open("data.db", "rb")
            codes = pickle.load(f)
            f.close()
        except:
            codes = []

        print(codes)

        # 매수
        for code in codes:
            self.kiwoom.SendOder("buy_market_order", "0101", account, 1, code, 10, 0, "03", "")
            time.sleep(0.2)

if __name__ == "__main__":
    pytrader = PyTrader()
    pytrader.run()
