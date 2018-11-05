import unittest
from user import User

class Usertest(unittest.TestCase):
    """
    This contains all user tests
    """

    def create(self):
        """
        this creates a new user before a test run
        """
        self.new_user = User("migidza-andisi","shay123")
    
    def signuptest(self):
        """
        this will test whether the user is saved correctly

        """

        self.assertEqual(self.new_user.login,"migidza-andisi")
        self.assertEqual(self.new_user.password,"shay123")

    def test_userexistance(self):

        """
        tests the user existance
        """

        self.assertTrue(User.user_existant)
if __name__ == " __main__":
    unittest.main()