from entities.user import User
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
        """Method creates new workout to the database"""
        #workout_id, username, workout_name, date_and_time, repetition, workout_type, sets, details
        cursor_workout = self._connection.cursor()

        #cursor_workout.execute(
        #    "insert into workouts (workout_id, username, workout, date_and_time, repetition, type, sets, details) values (?, ?, ?, ?, ?, ?, ?, ?)",
        #    (int(workout_id), str(username), str(workout_name), str(date_and_time), str(repetition),
        #    str(sets), str(workout_type), str(details))
        #)
        
        cursor_workout.execute(
            "insert into workouts (workout_id, username, workout, date_and_time, repetition, type, sets, details) values (?, ?, ?, ?, ?, ?, ?, ?);",
            (workout.workout_id, workout.username, workout.workout_name,  workout.date_and_time, 
            workout.repetition, workout.workout_type, workout.sets, workout.details)
        )
        self._connection.commit()


    def select_workouts(self, username):
        cursor_workout = self._connection.cursor()
        
        cursor_workout.execute(
            "select * from workouts where username = ?;", (username,)
        )

        rows = cursor_workout.fetchall()

        #for row in rows:
        #    print(row[0])
        #    print(row[1])
        #    print(row[2])
        #    print(row[3])
        #    print(row[4])
        #    print(row[5])
        #    print(row[6])
        #    print(row[7])

        return rows

    def get_workout_id(self, workout_id):
        cursor_workout = self._connection.cursor()

        try:
            cursor_workout.execute(
                "select workout_id from workouts where workout_id = %(workout_id)s, (workout_id,);"
            )
            return True
        except:
            return None

workout_repository = WorkoutRepository(get_database_connection())
    