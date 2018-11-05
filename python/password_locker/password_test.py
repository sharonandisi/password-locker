import unittest
from password import Password

class Passwordtest(unittest.TestCase):
    """
    This is where we run all tests
    """

    def create(self)
    """
    this functions creates a new password before a test runs
    """
    self.new_password = Password("Instagram", "migidza-andisi","shay123")

    def new_password_test(self):
        """
        this is to test whether a new passowrd is generated well
        """

        self.assertEqual(self.new_password.account,"Instagram")
        self.assertEqual(self.newPassword.name,"migidza-andisi")
        self.assertEqual(self.new_password.password,"sahy123")

    def test_password_length(self):
        """
        this checks if the password length is equal to the users required length
        """
        self.new_password.save_password()
        self.assertEqual(len(Password.passwords),1)
