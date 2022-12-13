from entities.user import User
from entities.workout import Workout
from database_connection import get_database_connection

def get_workout_by_row(row):
    return Workout(row["name"], row["date_and_time"]) if row else None


class WorkoutRepository:
    
    """
    Class handles workout-class activities to and from sqlite3 database
    """

    def __init__(self, connection):
        self._connection = connection

    def create_workout(self, workout):
        "Method creates new workout to the database"
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (workout, user, date_and_time, repetition, type, sets, details) values (?, ?, ?, ?, ?, ?, ?)",
            (workout.get_workout_name, workout.get_workout_user.username, workout.get_workout_date_and_time, 
            workout.get_workout_sets, workout.workout_repetition, workout.get_workout_details)
        )
        self._connection.commit()

        return workout


workout_repository = WorkoutRepository(get_database_connection())
    