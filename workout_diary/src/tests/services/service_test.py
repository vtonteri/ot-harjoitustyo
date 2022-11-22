import unittest

from services.workout_service import WorkoutService
from entities.user import User
from entities.workout import Workout

class TestWorkoutService(unittest.TestCase):
    def setUp(self):
        self.workout = WorkoutService()
        self.user = User("Matti", "matti123")
        self.workout = Workout("Puntti", True, "cardio", 1908)

    def test_weight_adjust(self):
        answer = WorkoutService.adjust_weights(self, 100, 10)
        self.assertEqual(answer, 110)

    def test_add_weight_lifting_set(self):
        self.workout.add_weight_lifting_set("penkkipunnerrus", 3, 80)
        self.assertEqual(self.workout.workout_sets_weight_lifting["penkkipunnerrus"], (3, 80))