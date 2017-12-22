"""
db handler of cybot
"""

import sqlite3  # we are using sqlite3 as our db

# global connection and cursor
conn = sqlite3.connect('cybot.db')
c = conn.cursor()


# create table wrapper
def create_table(name: str):
    """
    usage:
        @create_table(name='table_name')
        def func():
            return [
                {"name": "field_name", "type": "field_type"},
            ]
        func
    func should return list of fields
    :param name: name of table
    :return: bool
    """

    def create(name: str, fields: [dict]):
        """
        fields = [{'name': , 'type':}, ..]
        """
        fields_str = [f"{field['name']} {field['type']}" for field in fields]
        fields_str = ", ".join(fields_str)
        try:
            c.execute(f"CREATE TABLE {name} ({fields_str})")
        except Exception as e:
            print(e)
            return False
        print(f"table {name} created")
        return True

    def wrapper(func):
        fields = func()
        return create(name, fields)

    return wrapper


class RunCommand:
    """
    RunCommand should NEVER get user inputs
    """
    @staticmethod
    def add_row(table: str, values: [str]):
        values = ", ".join(values)
        try:
            c.execute(f"INSERT INTO {table} VALUES ({values})")
            conn.commit()
        except Exception as e:
            print(e)
            return False
        conn.commit()
        return True

    @staticmethod
    def update_row(table: str, expression: str, set: str):
        try:
            c.execute(f"UPDATE {table} SET {set} WHERE {expression}")
            conn.commit()
        except Exception as e:
            print(e)
            return False
        conn.commit()
        return True

    @staticmethod
    def select_row(table: str, fields: [str], expression: str):
        fields = ", ".join(fields)
        try:
            s = c.execute(f"SELECT {fields} FROM {table} WHERE {expression}")
        except Exception as e:
            print(e)
            return False
        return s.fetchone()


def InitDB():
    @create_table(name='karma')
    def karma():
        return [
            {"name": "user", "type": "text"},
            {"name": "karma", "type": "real"},
            {"name": "last_karma_gave", "type": "real"}
        ]

    @create_table(name='store')
    def store():
        return [
            {"name": "name", "type": "text"},
            {"name": "type", "type": "text"},
            {"name": "value", "type": "text"},
            {"name": "price", "type": "real"}
        ]

    karma
    store
    conn.commit()


InitDB()


def __del__(self):
    c.commit()
    conn.close()
    print("closed db")
