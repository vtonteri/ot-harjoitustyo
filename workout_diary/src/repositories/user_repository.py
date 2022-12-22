from entities.user import User
from database_connection import get_database_connection

def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None

class UserRepository:

    """Class handles user-class related activities 
    to and from sqlite3 database"""

    def __init__(self, connection):
        """Constructor

        Args:
        connection is the database_connection's connection-function"""
        
        self._connection = connection

    def find_all(self):
        "Method returns all users as a list from the database"
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        return list(map(get_user_by_row, rows))

    def create(self, user):
        "Method creates new user to the database"
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )
        self._connection.commit()
 
        return user

    def check_if_username_exist(self, username):

        """Method checks if a username already exists
        
        Args:
            username
        Returns:
            False: username does not exist
            Username: username already exists
        
        """

        cursor = self._connection.cursor()

        try:
            if cursor.execute("SELECT username FROM users WHERE username = %(username)s, (username,)") == username:
                return username

        except:
            return False

    def check_username_and_password(self, username):

        """Method checks what is usernames password
        
        Args:
            username
        Returns:
            Usernames password (hashed)
        
        """

        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM users where username = ?", (username,))

        row = cursor.fetchone()

        return get_user_by_row(row)

    def delete_database(self):

        """Method deletes users database"""

        cursor = self._connection.cursor()
        cursor.execute("delete from users")

        self._connection.commit()


user_repository = UserRepository(get_database_connection())