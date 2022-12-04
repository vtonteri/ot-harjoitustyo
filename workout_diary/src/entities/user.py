import bcrypt

class User:
    """Class, creates a new User.

    Attributes:
        - User details
            - Name
            - Password    
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def __str__(self):
        return f"Username: {self.username}, password (hashed): {self.password}"
