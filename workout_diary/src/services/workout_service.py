from entities.user import User
from entities.workout import Workout
import datetime
import random
from repositories.workout_repository import (
    workout_repository as default_workout_repository)


class WorkoutService:

    def __init__(self, workout_repository = default_workout_repository) -> None:
        self.new_workout = None
        self._workout_repository = workout_repository

    def __str__(self) -> str:
        pass

    def create_workout(self, username: str, workout_name: str, date_and_time: str, repetition: bool, workout_type: str, sets: str, details: str):

        i = 0
        for i in range(5):

            workout_id = random.randint(1, 20000)
            if self._check_workout_id(workout_id) == False:
                workout_to_database = Workout(workout_id, username, workout_name, date_and_time, repetition, workout_type, sets, details)
                default_workout_repository.create_workout_to_database(workout_to_database)
                break
            i += 1
        #self.new_workout = Workout(workout_name, username, date_and_time, repetition, workout_type, sets, details)
        


    def get_workouts(self, username):

        return default_workout_repository.select_workouts(username)

    def create_cardio_workout(self):
        #cardio = Workout
        pass

    def delete_workout(self):
        pass

    def edit_weight_lift_workout(self):
        pass

    def adjust_weights(self, weight, percent):
        x = 1 + (percent / 100)
        return round(x * weight)

    def _check_workout_id(self, workout_id):
        if default_workout_repository.get_workout_id(workout_id) == None:
            return False
        else:
            return True

workout_service = WorkoutService()