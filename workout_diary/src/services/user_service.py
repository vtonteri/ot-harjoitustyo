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

        if not user or password_check:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user

        return user

    def hash_password(self, plain_password):
        plain_password = str(plain_password).encode('utf-8')
        return bcrypt.hashpw(plain_password, bcrypt.gensalt(10))

    def check_password(self, user, plain_password):
        plain_password = str(plain_password).encode('utf-8')

        return bcrypt.checkpw(plain_password, user.password)
        

user_service = UserService()