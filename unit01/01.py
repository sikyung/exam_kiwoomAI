from kiwoom import *
from pandas import DataFrame


kiwoom = Kiwoom()
kiwoom.CommConnect()
print("login")

data = []
# samsung = []
kospi = kiwoom.GetCodeListByMarket('0')
kosdaq = kiwoom.GetCodeListByMarket('10')
codes = kospi + kosdaq

# for code in codes:
#     name = kiwoom.GetMasterCodeName(code)
#
#     if '삼성' in name:
#         samsung.append(code)
#
# print(samsung)
# print(len(samsung))

for code in codes:
    name = kiwoom.GetMasterCodeName(code)
    data.append((code, name))

df = DataFrame(data=data, columns=['code', '종목명'])
df = df.set_index('code')
df.to_excel("code.xlsx")