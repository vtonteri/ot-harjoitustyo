from entities.workout import Workout
from database_connection import get_database_connection

def get_workout_by_row(row):
    return Workout(row["workout_id"], row["username"], row["workout"], row["date_and_time"], 
    row["repetition"], row["type"], row["sets"], row["details"]) if row else None


class WorkoutRepository:
    
    """
    Class handles workout-class activities to and from sqlite3 database
    """

    def __init__(self, connection):
        self._connection = connection

    def create_workout_to_database(self, workout):
        """Method creates new workout to the database
        
        Args:
            Workout
        
        """

        cursor_workout = self._connection.cursor()

        cursor_workout.execute(
            "insert into workouts (workout_id, username, workout, date_and_time, repetition, type, sets, details) values (?, ?, ?, ?, ?, ?, ?, ?);",
            (workout.workout_id, workout.username, workout.workout_name,  workout.date_and_time, 
            workout.repetition, workout.workout_type, workout.sets, workout.details)
        )
        self._connection.commit()


    def select_workouts(self, username):

        """Method fetches and returns users workouts
        
        Args:
            Username
        Returns:
            Usernames all workouts
        
        """
        cursor_workout = self._connection.cursor()
        
        cursor_workout.execute(
            "select * from workouts where username = ?;", (username,)
        )

        rows = cursor_workout.fetchall()

        return rows

    def get_workout_id(self, workout_id):

        """Method checks if a workout_id already exists
        
        Args:
            workout_id
        Returns:
            False: workout_id does not exist
            True: workout_id do already exist
        
        """
        cursor_workout = self._connection.cursor()

        try:
            cursor_workout.execute(
                "select workout_id from workouts where workout_id = %(workout_id)s, (workout_id,);"
            )
            return True
        except:
            return None

    def delete_database(self):

        """Method deletes workputs database"""

        cursor = self._connection.cursor()
        cursor.execute("delete from workouts")

        self._connection.commit()

workout_repository = WorkoutRepository(get_database_connection())
    