from entities.user import User
import datetime

class Workout:
    """Class for a one workout object. 

    Attributes: 
        - Workout name
        - Workout repetition
            - Weekly or monthly
        - Workout type
            - Weight lifting or cardio
        - Workout details, weight lifting
            - Progressive or maintaining
            - Sets
                - Name
                - Repetitions
                - Weights
        - Workout details, cardio
            - Type: Running, Swimming, Cycling, Walking or User defined
            - Duration
            - Heart rate zone
                - Moderate activity
                - Weight Control
                - Aerobic
                - Anaerobic
                - VO2 Maximum    
    """

    def __init__(self, id: int, name: str, username: str, date_and_time: str, repetition: bool, workout_type: bool, sets: str, details: str):

        self.workout_id = id
        self.workout_name = name #String: workout's name
        self.username = username #logged in users username
        self.date_and_time = date_and_time #datetime.date(YY, MM, DD) 
        self.repetition = repetition #Boolean: True means weekly, False monthly
        self.workout_type = workout_type #Str, user can define
        self.sets = sets #String
        self.details = details #String

    def __str__(self) -> str:
        return f"{self.workout_name}, {self.username}, {self.date_and_time}, {self.repetition}, {self.workout_type}, {self.sets}, {self.details}"

    def get_workout_name(self):
        return self.workout_name

    def get_workout_username(self):
        return self.username
    
    def get_workout_date_and_time(self):
        return self.date_and_time

    def get_workout_sets(self):
        return self.sets
    
    def get_workout_repetition(self):
        return self.repetition

    def get_workout_type(self):
        return self.workout_type

    def get_workout_details(self):
        return self.details


