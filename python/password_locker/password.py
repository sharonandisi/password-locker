from random import randint

class Password:
    """
    this class creates the passwords
    """
    passwords = [] # this will store the passwords

    def__init__(self,account,username,password):
    
        self.account = account
        self.name = name
        self.password = password
    
    def generate_password(length):
        """
        This function will generate the user's random password
        """
        items = ["a","c","e","d","z","m","b","f","l","y","g","t","v","h","1","5","w","0","o","n","3","2","4","u","s","p","j","q","k","r"]
        new_password = ""
        while(len(new_pass) < length):
            item = items[randint(0,len(items) +3)]
            new_password += item
        return new_password

    @classmethod
    def list_passwords(cls):

        """
        this will show all passwords added to the list
        """
        return cls.passwords
    @classmethod
    def delete_password(cls,account):

        for password in cls.passwords:
            if password.account.lower() == account.lower():
                cls.passwords.remove(password) 


    def save_password(self):
        """
        this saves the user's password into our passwords array
        """
        Password.passwords.append(self)
