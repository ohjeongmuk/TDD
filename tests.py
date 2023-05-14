import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):
    def test1(self):
        # len(pwd) == 7
        pwd = "Asdfg1!"
        self.assertFalse(check_pwd(pwd))

    def test2(self):
        # len(pwd) == 10
        pwd = "aaaaaaaaa1"
        self.assertFalse(check_pwd(pwd))

    def test3(self):
        # len(pwd) == 21
        pwd = "Asdfgdddddddddddddd12"
        self.assertFalse(check_pwd(pwd)) 

    def test4(self):
        # len(pwd) == 8 & All lower
        pwd = "ABCDEFGH"
        self.assertFalse(check_pwd(pwd)) 
    
    def test5(self):
        # len(pwd) == 7 & All upper
        pwd = "asdfghjs"
        self.assertFalse(check_pwd(pwd)) 


if __name__ == '__main__':
    unittest.main()