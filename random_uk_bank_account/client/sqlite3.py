import sqlite3
from functools import wraps


class SqlLite:

    def __init__(self, local_db):
        self.conn = sqlite3.connect(local_db)
        self.cur = self.conn.cursor()

    def commit(self):
        self.conn.commit()
        return self

    def close(self):
        self.conn.close()
        return self


class SqlLiteUtilities:

    @staticmethod
    def return_rows_as_list_dict(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            db_cursor = func(*args, **kwargs)
            if not isinstance(db_cursor, sqlite3.Cursor):
                raise Exception('return_rows_as_dict requires wrapped function to return sqlite3.Cursor object.')

            headers = [header[0] for header in db_cursor.description]
            rows = db_cursor.fetchall()
            rows_as_dict_array = []

            for row in rows:
                row_array = [item for item in row]
                rows_as_dict_array.append(dict(zip(headers, row_array)))
            return rows_as_dict_array

        return wrap

    @staticmethod
    def return_rows_as_dict(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            rows_as_list_dict = SqlLiteUtilities.return_rows_as_list_dict(func)(*args, **kwargs)
            if rows_as_list_dict:
                return rows_as_list_dict
            else:
                return {}

        return wrap
