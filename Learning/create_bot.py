import os
import sqlite3

from aiogram import Bot
from aiogram.dispatcher import Dispatcher

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)


class User:

    def __str__(self) -> str:
        return f"User<id={self.id}, name={self.name}, status={self.status}>"

    def __repr__(self) -> str:
        return self.__str__()

    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status


class DataBase:

    def __init__(self, path: str):
        self.__base = sqlite3.connect(path)
        self.__cur = self.__base.cursor()

    def add_user(self, user: User):
        print(user)
        if self.get_user(user.id) is not None:
            return
        self.__cur.execute(f"INSERT INTO users VALUES ({user.id}, '{user.name}', '{user.status}')")
        print("Added")
        self.__base.commit()

    def get_user(self, user_id):
        self.__cur.execute(f"SELECT * FROM users WHERE id={user_id}")
        res: list = self.__cur.fetchall()
        if res is None or len(res) == 0:
            return None
        print(res)
        return User(*res[0])

    def __delete_user(self, user_id):
        self.__cur.execute(f"DELETE FROM users WHERE id={user_id}")

    def set_user_status(self, user: User, status):
        user.status = status
        if self.get_user(user.id) is None:
            user.status = "Guest"
            self.add_user(user)
        else:
            self.__delete_user(user.id)
            self.add_user(user)

    def close(self):
        self.__cur.close()
        self.__base.close()


database = DataBase("database.db")
user_help: dict = None

