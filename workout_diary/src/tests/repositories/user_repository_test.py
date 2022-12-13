import unittest
from repositories.user_repository import user_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):

    def setUp(self):
        user_repository.delete_database()
        self.user_max = User("max", "password1")
        self.user_kim = User("kim", "password2")

    def test_create(self):
        user_repository.create(self.user_max)
        users = user_repository.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_max.username)

    def test_find_all(self):
        user_repository.create(self.user_max)
        user_repository.create(self.user_kim)
        users = user_repository.find_all()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.user_max.username)
        self.assertEqual(users[1].username, self.user_kim.username)

    def test_check_username_and_password(self):
        user_repository.create(self.user_kim)

        user = user_repository.check_username_and_password(self.user_kim.username)

        self.assertEqual(user.username, self.user_kim.username)