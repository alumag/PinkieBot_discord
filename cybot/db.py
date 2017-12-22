"""
db handler of cybot
"""

import sqlite3  # we are using sqlite3 as our db

conn = sqlite3.connect('cybot.db')
c = conn.cursor()


def create_table(name: str):
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
        return True

    def wrapper(func):
        fields = func()
        return create(name, fields)

    return wrapper


def InitDB():
    @create_table(name='karma')
    def karma():
        return [
            {"name": "user", "type": "text"},
            {"name": "karma", "type": "real"}
        ]

    karma


InitDB()