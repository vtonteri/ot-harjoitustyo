import unittest
import datetime

from services.workout_service import WorkoutService
from entities.user import User
from entities.workout import Workout


class TestWorkoutService(unittest.TestCase):
    def setUp(self):
        self.user_matti = User("matti", "matti123")
        self.workout = Workout("Puntti", self.user_matti, datetime.date(2022, 12, 23), True, True, "Benchpress 2 x 12", "Recovery week")

    def test_weight_adjust(self):
        answer = WorkoutService.adjust_weights(self, 100, 10)
        self.assertEqual(answer, 110)
