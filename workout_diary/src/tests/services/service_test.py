import unittest

from ...services.workout_service import WorkoutService
from ...entities.user import User
from ...entities.workout import Workout

class TestWorkoutService(unittest.TestCase):
    def setUp(self):
        pass

    def test_weight_adjust(self):
        answer = WorkoutService.adjust_weights(100,10)
        self.assertEqual(answer, 110)
