import unittest

from services.workout_service import workout_service
from entities.user import User
from entities.workout import Workout


class TestWorkoutService(unittest.TestCase):
    def setUp(self):
        self.user_matti = User("matti", "matti123")
        self.workout = Workout(1010, "Puntti", self.user_matti.username, "2022-12-12", "Weekly", "Cardio", "Benchpress 2 x 12", "Recovery week")

    def test_create_workout_service(self):
        workout_test = workout_service.create_workout(self.user_matti.username, "Puntti", "2022-12-12", "Weekly", "Cardio", "Benchpress 2 x 12", "Recovery week")

        workout_from_database = workout_service.get_workouts(self.user_matti.username)

        for row in workout_from_database:
            self.assertTrue(1 <= row[0] <= 20000)
            self.assertEqual(row[2], "matti")