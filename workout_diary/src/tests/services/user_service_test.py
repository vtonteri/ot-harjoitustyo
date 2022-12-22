import unittest
import bcrypt
from entities.user import User
from services.user_service import user_service
import initialize_database

class TestUserService(unittest.TestCase):
    
    def setUp(self):
        initialize_database.initialize_database()

        self.password = str("password11").encode('utf-8')
        self.password_hashed = bcrypt.hashpw(self.password, bcrypt.gensalt(10))
        self.user_max = User("max", self.password_hashed)
        self.new_user = user_service.create_user("max", self.password_hashed)

    def test_hash_password(self):
        plain_password = str("password11").encode('utf-8')

        self.assertTrue(bcrypt.checkpw(plain_password, self.password_hashed))
        
    def test_check_password(self):
        result = user_service.check_password(self.user_max, "password11")

        self.assertTrue(result)