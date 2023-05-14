import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):
    def test1(self):
        # len(pwd) == 7
        pwd = "Asdfg1!"
        self.assertFalse(check_pwd(pwd))

if __name__ == '__main__':
    unittest.main()