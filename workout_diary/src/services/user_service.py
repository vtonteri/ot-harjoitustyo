from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository)
import bcrypt

class InvalidCredentialsError(Exception):
    pass

class UserService:

    def __init__(self, user_repository = default_user_repository):
        self.new_user = None
        self._user_repository = user_repository
        self.logged_in_username = None

    def create_user(self, new_username, new_password):
        self.new_user = self._user_repository.create(User(new_username, new_password))
        
    def login_user(self, login_username, login_password):
        """
        Logs user in
        
        Args: 
            login_username: str, users unique username
            login_password: str, users unique password, hashed
        """

        user = self._user_repository.check_username_and_password(login_username)

        password_check = self.check_password(user, login_password)

        if not user or password_check == False:
            raise InvalidCredentialsError("Invalid username or password")
            
        self._user = user
        self.logged_in_username = user.username

        return user

    def hash_password(self, plain_password):
        encoded_password = str(plain_password).encode('utf-8')
        return bcrypt.hashpw(encoded_password, bcrypt.gensalt(10))

    def check_password(self, user, plain_password):       
        encoded_plain_password = str(plain_password).encode('utf-8')
        return bcrypt.checkpw(encoded_plain_password, user.password)

    def get_logged_in_username(self):
        return self.logged_in_username
        

user_service = UserService()