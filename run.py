from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인")

# cnt = kiwoom.GetLoginInfo("ACCOUNT_CNT")
# print(cnt)
#
# account = kiwoom.GetLoginInfo("ACCNO")
# print(account)

# data = kiwoom.GetCodeListByMarket('0')
# print(data)

date = kiwoom.GetMasterStockState("005930")
print(date.split("|"))
