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

    def __init__(self, name: str, user: User, date_and_time: datetime.date, repetition: bool, workout_type: bool, sets: str, details: str):

        self.workout_name = name #String: workout's name
        self.user = user #User(username, password)
        self.date_and_time = date_and_time #datetime.date(YY, MM, DD) 
        self.repetition = repetition #Boolean: True means weekly, False monthly
        self.workout_type = workout_type #Boolean: True means weight lift, False cardio
        self.sets = sets #String
        self.details = details #String

    def get_workout_name(self):
        return self.workout_name

    def get_workout_user(self):
        return self.user
    
    def get_workout_date_and_time(self):
        return self.date_and_time

    def get_workout_sets(self):
        return self.sets
    
    def get_workout_repetition(self):
        return self.repetition

    def get_workout_details(self):
        return self.details


