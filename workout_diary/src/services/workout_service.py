from entities.user import User
from entities.workout import Workout
import datetime
from repositories.workout_repository import (
    workout_repository as default_workout_repository)


class WorkoutService:

    def __init__(self, workout_repository = default_workout_repository) -> None:
        self.new_workout = None
        self._workout_repository = workout_repository

    def __str__(self) -> str:
        pass

    def create_workout(self, name: str, user: User, date_and_time: datetime.date, repetition: bool, workout_type: bool, sets: str, details: str):
        self.new_workout = self._workout_repository.create_workout(Workout(name, user, date_and_time, repetition, workout_type, sets, details))


    def create_cardio_workout(self):
        #cardio = Workout
        pass

    def add_weight_lifting_set(self, name, repetitions, weight):
        self.workout_sets_weight_lifting[name] = (repetitions, weight)

    def delete_workout(self):
        pass

    def edit_weight_lift_workout(self):
        pass

    def adjust_weights(self, weight, percent):
        x = 1 + (percent / 100)
        return round(x * weight)
