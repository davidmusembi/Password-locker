import random
import string
import pyperclip

class User:
    """
    class User
    """
    user_list = []
    
     def __init__(self, username, password):
          self.username = username
        self.password = password
        
    def save_user(self):
        """
        method to save the user to user_list
        """
        User.user_list.append(self)
        
    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        """
        deletes the user from user_list
        """
        User.user_list.remove(self)