from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository)
import bcrypt

class UserService:

    def __init__(self, user_repository = default_user_repository):
        self.new_user = None
        self._user_repository = user_repository

    def create_user(self, new_username, new_password):
        self.new_user = self._user_repository.create(User(new_username, new_password))

    def _hash_password(self, password):
        pass

user_service = UserService()