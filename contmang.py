"""Basic context manager to be made more robust later"""

import mysql.connector


class ConnectionError(Exception):
    print("ConnectionError")

class CredentialsError(Exception):
    print("This is above your paygrade!")

class SQLError(Exception):
    print("The SQL is nuts, error!")

class UseDatabase:

    def __init__(self, config: dict):
        self.configuration = config

    def __enter__(self):
        try:
            self.conn = mysql.connector.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mysql.connector.errors.ProgrammingError as err:
            raise CredentialsError(err)
        except mysql.connector.errors.InerFaceError as err:
            raise ConnectionError(err)

    def __exit__(self, exc_type, exc_value, exc_trace):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is mysql.connector.errors.ProgrammingError:
            raise SQLError(exc_value)
        elif exc_type:
            raise exc_type(exc_value)




if __name__ == '__main__':
    "run testing examples"
    """will run anything after : if file run as main but not if it's imported
    ie __name__ != '__mani__'
    
