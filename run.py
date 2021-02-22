from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("login")

# cnt = kiwoom.GetLoginInfo("ACCOUNT_CNT")
# print(cnt)
#
# account = kiwoom.GetLoginInfo("ACCNO")
# print(account)

# data = kiwoom.GetCodeListByMarket('0')
# print(data)


print(kiwoom.GetCodeListByMarket("005930"))
