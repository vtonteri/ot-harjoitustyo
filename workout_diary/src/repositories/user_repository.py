from entities.user import User
from database_connection import get_database_connection

def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None

class UserRepository:

    """Class handles user-class related activities 
    to and from sqlite3 database"""

    def __init__(self, connection) -> None:
        """Constructor

        Args:
        connection is the database_connection's connection-function"""
        
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def create(self, user):
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )
        self._connection.commit()

        return user

    def _read(self):
        users = []

        pass


if __name__ == "__main__":
    kayttaja = User()
    UserRepository.create(kayttaja)