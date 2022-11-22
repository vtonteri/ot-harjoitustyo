from entities.user import User
from entities.workout import Workout

class WorkoutService:

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        pass
        
    def create_workout(self, name: str, repetition: bool, workout_type: str, workout_id:None):

        if workout_type == "weight_lift":
            self.workout = Workout(name, repetition, workout_type, workout_id)
        elif workout_type == "cardio":
            self.workout = Workout(name, )

        #Workout is saved in the database
        #workout id links it to a certain user

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
