import unittest
from  password import User, Credentials

class TestClass(unittest.TestCase):
    """
    Class that defines test cases for the user class behaviours.
    """
    def setUp(self): 
        """
        method to set up the test class with the given credentials
        """
        self.new_user = User('Dave','Qfg4hbg9')
        
    def test_init(self):
        """
        method to initialize the test class with the given credentials and test if the user is created successfully
        """
        self.assertEqual(self.new_user.username,'Dave')
        self.assertEqual(self.new_user.password,'Qfg4hbg9')