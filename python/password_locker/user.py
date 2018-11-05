class User:
    """
    this class holds user details
    """
    def __init__(self,login,password):
        """
        this creates credentials for the user
        """
        self.signin = signin
        self.password = password

    def user_existant(self,password):
        """
        this is for user authentification
        """
        if self.password == password:
            return True
        return False