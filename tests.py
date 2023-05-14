import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):
    def test1(self):
        # len(pwd) == 7 False
        pwd = "Asdfg1!"
        self.assertFalse(check_pwd(pwd))

    def test2(self):
        # len(pwd) == 10 True
        pwd = "Aaaaaaaaa1"
        self.assertFalse(check_pwd(pwd))

    def test3(self):
        # len(pwd) == 21
        pwd = "Asdfgdddddddddddddd12"
        self.assertFalse(check_pwd(pwd)) 

    def test4(self):
        # len(pwd) == 8 & All Upper
        pwd = "ABCDEFGH"
        self.assertFalse(check_pwd(pwd)) 
    
    def test5(self):
        # len(pwd) == 7 & All Lower
        pwd = "asdfghjs"
        self.assertFalse(check_pwd(pwd)) 

    def test6(self):
        # len(pwd) == 9 & Lower + Upper
        pwd = "AAAAAAaAA"
        self.assertFalse(check_pwd(pwd)) 

    def test7(self):
        # len(pwd) == 10 & Lower + Digit
        pwd = "AAAAAAAA12"
        self.assertFalse(check_pwd(pwd)) 

    def test8(self):
        # len(pwd) == 10 & Upper + Digit
        pwd = "aaaaaaaa12"
        self.assertFalse(check_pwd(pwd)) 

    def test9(self):
        # len(pwd) == 10 & Upper + Lower + Digit 
        pwd = "AAAaaaaaa12"
        self.assertFalse(check_pwd(pwd)) 

    def test10(self):
        # len(pwd) == 10 & Upper + Lower + Symbol
        pwd = "Aaaaaaaaaa!"
        self.assertFalse(check_pwd(pwd)) 

    def test11(self):
        # len(pwd) == 10 & Upper + Lower + Digit 
        pwd = "Aaaaaaaaa12"
        self.assertFalse(check_pwd(pwd)) 

    def test12(self):
        # len(pwd) == 10 & Upper + Digit + Symbol 
        pwd = "AAAAAAAA12!"
        self.assertFalse(check_pwd(pwd)) 

if __name__ == '__main__':
    unittest.main()