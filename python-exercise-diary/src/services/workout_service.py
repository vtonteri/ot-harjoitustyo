from pathlib import Path
from ...entities.user import User
from ...entities.workout import Workout

class WorkoutService:

    def __init__(self) -> None:
        pass
        
    def create_weight_lift_workout(self):
        pass

    def create_cardio_workout(self):
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
