import unittest
import bcrypt
from entities.user import User
from services.user_service import user_service

class TestUserService(unittest.TestCase):
    
    def setUp(self):
        self.password = str("password11").encode('utf-8')
        self.password_hashed = bcrypt.hashpw(self.password, bcrypt.gensalt(10))
        self.user_max = User("max", self.password_hashed)

    def test_hash_password(self):
        plain_password = str("password11").encode('utf-8')

        self.assertTrue(bcrypt.checkpw(plain_password, self.password_hashed))
        