from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 성공")

codes = kiwoom.GetCodeListByMarket('0') + kiwoom.GetCodeListByMarket('10')

# for code in codes:
#     date = kiwoom.GetMasterListedStockDate(code)
#     name = kiwoom.GetMasterCodeName(code)
#
#     if date.startswith('2021'):
#         print(date, code, name)

for code in codes:
    state = kiwoom.GetMasterStockState(code)
    tokens = state.split('|')


    target = False
    if '거래정지' in tokens:
        target = True
    elif '관리종목' in tokens:
        target = True
    elif '감리종목' in tokens:
        target = True
    elif '투자유의종목' in tokens:
        target = True

    if target in True:
        print(code, state)