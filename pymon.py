from kiwoom import *
import pickle


class PyMon:
    def __init__(self):
        # Kiwoom 클래스 객체를 생성
        self.kiwoom = Kiwoom()
        self.kiwoom.CommConnect()
        self.kiwoom.GetConditionLoad()

    def run(self):
        # 조건식에 해당하는 종목리스트 얻기
        self.kiwoom.SendCondition("0101", "test", "001", 0)
        codes = self.kiwoom.codition_codes

        # 파일로 쓰기
        f = open("data.db", "wb")
        pickle.dump(codes, f)
        f.close()

if __name__ == "__main__":
    pymon = PyMon()
    pymon.run()
