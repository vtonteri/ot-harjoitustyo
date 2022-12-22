import unittest
from repositories.workout_repository import workout_repository
from entities.workout import Workout

class TestWorkoutRepository(unittest.TestCase):

    def setUp(self):
        workout_repository.delete_database()
        self.test_workout = Workout(2999, "Ville", "Puntti", "2022-12-14", "Weekly", "Cardio", "3x12", "Penkkipunnerrus")

    def test_create_workout(self):
        workout_repository.create_workout_to_database(self.test_workout)
        workout_from_database = workout_repository.select_workouts("Ville")

        for row in workout_from_database:

            self.assertEqual(row[0], 2999)
            self.assertEqual(row[1], "Ville")