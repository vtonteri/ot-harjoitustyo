from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
        ''')

    connection.commit()

    cursor_workout = connection.cursor()

    cursor_workout.execute('''
        drop table if exists workouts;
        ''')

    connection.commit()

def create_tables(connection):
    """
    Two tables are created to the database: users and workouts
    User and workout are connected together using username
    """
    cursor = connection.cursor()

    cursor.execute('''
        create table users  (
            username text primary key,
            password text
            );
    ''')

    connection.commit()

    cursor_workout = connection.cursor()
    
    cursor_workout.execute('''
        create table workouts   (
            workout_id integer primary key,
            username text,
            workout text,
            date_and_time text,
            repetition text,
            type text,
            sets text,
            details text
            );
    ''')

    connection.commit()

def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()