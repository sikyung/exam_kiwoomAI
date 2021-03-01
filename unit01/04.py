from kiwoom import *
import pprint
import time

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인")

codes = kiwoom.GetCodeListByMarket('0') + kiwoom.GetCodeListByMarket('1')

per_result =[]
for code in codes[:50]:
    kiwoom.SetInputValue("종목코드", code)
    kiwoom.CommRqData("opt10001", "opt10001", 0, "0101")

    per = kiwoom.tr_data["PER"]
    pbr = kiwoom.tr_data["PBR"]

    try:
        per = float(per)
    except:
        per = 0

    try:
        pbr = float(pbr)
    except:
        pbr = 0

    if 2.5 <= per <= 10:
        per_result.append((code, per, pbr))

    time.sleep(0.2)

print(per_result)

result = sorted(per_result, key=lambda x:x[2])

for i in result:
    print(i[0], i[1], i[2])

