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
        """Method returns User's information as str"""
        return f"{self.username}, {self.password}"

    def username(self):
        """Method returns Users username as str"""
        return self.username

    def password(self):
        """Method returns Users password as a str"""
        return self.password
