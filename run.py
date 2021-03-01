from kiwoom import *
import pprint

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인")

# TR
kiwoom.SetInputValue("종목코드", "352770")
kiwoom.CommRqData("opt10001", "opt10001", 0, "0101")
print("데이터 요청 완료")
print(kiwoom.tr_data["PBR"])
