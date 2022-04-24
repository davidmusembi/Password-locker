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
        
    def save_credential_test(self):
        """
        method to save the user to credential_list
        """
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def tearDown(self):
        Credentials.credentials_list = []
        
    def test_save_many_accounts(self):
        """
        TEST: save_many_accounts
        """
        self.new_credential.save_details()
        test_credential = Credentials("snapchat","Dave","JFGN5KJV") 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)
        
    def test_delete_credential(self):
        """
        test method if one can delete an account
        """
        self.new_credential.save_details()
        test_credential = Credentials("snapchat","Dave","JFGN5KJV")
        test_credential.save_details()
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def test_find_credentialr(self):
        self.new_credential.save_details()
        test_credential = Credentials("snapchat","Dave","JFGN5KJV")") 
        test_credential.save_details()

        the_credential = Credentials.find_credential("Instagram")

        self.assertEqual(the_credential.account,test_credential.account)
    
    def test_credential_exist(self):
        """
        test to check if one can find a credential
        """
    self.new_credential.save_details()
        the_credential = Credentials("snapchat", "Dave", "JFGN5KJV")  
        the_credential.save_details()
        credential_is_found = Credentials.if_credential_exist("snapchat")
        self.assertTrue(credential_is_found)
        
    def test_display_all_saved_credentials(self):
        """
        method to display all the saved credential
        """
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == "__main__":
    unittest.main()
     