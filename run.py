from kiwoom import *
import pprint
import time

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인")

kiwoom.GetConditionLoad()
# condition = kiwoom.GetConditionNameList()
# print(condition)

kiwoom.SendCondition("0101", "sungjin", "000", 0)
print(kiwoom.codition_codes)