from entities.workout import Workout
import random
from repositories.workout_repository import (
    workout_repository as default_workout_repository)


class WorkoutService:

    def __init__(self, workout_repository = default_workout_repository) -> None:
        self.new_workout = None
        self._workout_repository = workout_repository

    def create_workout(self, username: str, workout_name: str, date_and_time: str, repetition: str, workout_type: str, sets: str, details: str):

        """
        Creates new workout and calls workout repositorys
        create_workout_to_database, which saves a workout to database (table workouts).
        Gives also a unique id to a workout (random integer between 1 - 20000).
        Checks if id already exists.

        Args:
            username: str, workout_name: str, date_and_time: str,
            repetition: string, workout_type: str, sets: str, details: str
        """

        i = 0
        for i in range(5):

            workout_id = random.randint(1, 20000)
            if self._check_workout_id(workout_id) == False:
                workout_to_database = Workout(workout_id, username, workout_name, date_and_time, repetition, workout_type, sets, details)
                default_workout_repository.create_workout_to_database(workout_to_database)
                break
            i += 1

    def get_workouts(self, username):

        """
        Returns all logged in users workouts

        Args:
            Username

        Return:
            Usernames all workouts, that are saved in the database (table: workouts)
        """

        return default_workout_repository.select_workouts(username)

    def _check_workout_id(self, workout_id):
        if default_workout_repository.get_workout_id(workout_id) == None:
            return False
        else:
            return True

workout_service = WorkoutService()