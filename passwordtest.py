import unittest
from  password import User, Credentials

class TestClass(unittest.TestCase):
    def setUp(self): 
        self.new_user = User('Dave','Qfg4hbg9')