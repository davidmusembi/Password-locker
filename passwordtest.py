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
        test case to initialize the test class with the given credentials and test if the user is created successfully
        """
        self.assertEqual(self.new_user.username,'Dave')
        self.assertEqual(self.new_user.password,'Qfg4hbg9')
        
        def test_save_user(self):
            """
            test case to save the user to the test class
            """
            self.new_user.save_user()
            self.assertEqual(len(User.user_list),1)
            
        class TestCredentials(unittest.TestCase):
            """
            test case to test credentials for the test class
            """
            def setUp(self):
                """
                method to set up the test class with the given credentials
                """
                self.new_credential = Credentials('Instagram','Dave','Wg8htb52')
    def test_init(self):
        """
        test case to initialize the test class with the given credentials and  test credentials
        """
        self.assertEqual(self.new_credential.account,'Instagram')
        self.assertEqual(self.new_credential.userName,'Dave')
        self.assertEqual(self.new_credential.password,'Wg8htb52')
