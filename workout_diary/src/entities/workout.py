class Workout:
    """Class for a one workout object.
    Attributes:
        - Workout_id: integer
        - Workout name: string
        - Username: users username
        - Date and time: datetime.date object (YYYY-MM-DD)
        - Workout repetition: string
            - Weekly or none
            - Weekly: workout will be added to database three times with a weeks interval
        - Workout type
            - Weight lifting or cardio
        - Sets: string
        - Workout details: string
            - User can write details as wanted
    """

    def __init__(self, id: int, name: str, username: str, date_and_time: str,
    repetition: bool, workout_type: bool, sets: str, details: str):

        self.workout_id = id
        self.workout_name = name #String: workout's name
        self.username = username #logged in users username
        self.date_and_time = date_and_time #datetime.date(YY, MM, DD)
        self.repetition = repetition #Boolean: True means weekly, False monthlys
        self.workout_type = workout_type #Str, user can define
        self.sets = sets #String
        self.details = details #String

    def __str__(self) -> str:
        return f"{self.workout_name}, {self.username}, {self.date_and_time}, {self.repetition}, {self.workout_type}, {self.sets}, {self.details}"