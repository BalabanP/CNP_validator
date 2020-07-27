from datetime import date
from datetime import datetime
import unittest



class Cnp_validator():

    def __init__(self, cnp):
        self.cnp = cnp

    def verify_S(self):
        S = self.cnp[0]
        # print(self.cnp[1:7])
        if S == '1' or S == '2' or S == '7' or S == '8':
            date = "19"+self.cnp[1:7]
            born_date = datetime.strptime(date,"%Y%m%d")
            if datetime(1900, 1, 1) <= born_date <= datetime(1999, 12, 31):
                return True
        elif S == '3' or S == '4' :
            date = "18"+self.cnp[1:7]
            born_date = datetime.strptime(date,"%Y%m%d")
            print(born_date)
            if datetime(1800, 1, 1) <= born_date <= datetime(1899, 12, 31):
                return True
        elif S == '5' or S == '6' or S == "9":
            date = "20"+self.cnp[1:7]
            born_date = datetime.strptime(date,"%Y%m%d")
            print(born_date)
            if datetime(2000, 1, 1) <= born_date <= datetime(2099, 12, 31):
                return True

        else:
            return False

    def verify_AA(self):
        return True

    def verify_LL(self):
        if int(self.cnp[3:5]) in range(1,12):
            return True
        else:
            return False

    def verify_ZZ(self):
        if int(self.cnp[5:7]) in range(1,31):
            return True
        else:
            return False

    def verify_JJ(self):
        coduri_judete = []
        for i in range(1,52):
            coduri_judete.append(str(i).zfill(2))

        if self.cnp[7:9] in coduri_judete:
            return True
        else:
            return False

    def verify_NNN(self):
        # generare fake numere de inregistrare
        NNN_list = []
        for i in range(1,999):
            NNN_list.append(str(i).zfill(3))
        if self.cnp[9:12] in NNN_list:
            return True
        else:
            return False


    def verify_C(self):
        nr = '279146358279'
        count=0
        produs = []
        for i in nr:
            op = int(self.cnp[count])*int(i)
            produs.append(op)
            count+=1

        if sum(produs)%11 == 10:
            if self.cnp[-1] == str(1):
                return True
            else:
                return False
        else:
            if self.cnp[-1] == str(sum(produs)%11):
                return True
            else:
                return False

def main_validator(CNP):
    if len(CNP) == 13:
        obj = Cnp_validator(CNP)
        if obj.verify_AA() and obj.verify_LL() and obj.verify_ZZ():
            if obj.verify_S() and obj.verify_JJ() and obj.verify_NNN() and obj.verify_C():
                return "CNP Valid"
            else:
                return "CNP Invalid"
        else:
            return "CNP Invalid"
    else:
        return "CNP Invalid"




class TestValidator(unittest.TestCase):

    def test_CNP(self):
        self.assertEqual(main_validator('1920314410084'), 'CNP Valid')
        self.assertEqual(main_validator('8980816400023'), 'CNP Valid')

if __name__ == '__main__':
    unittest.main()
