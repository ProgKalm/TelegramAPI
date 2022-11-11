import os
import sqlite3

from aiogram import Bot, types
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
        if self.get_user(user.id) is not None:
            return
        self.__cur.execute(f"INSERT INTO users VALUES ({user.id}, '{user.name}', '{user.status}')")
        self.__base.commit()

    def get_user(self, user_id):
        self.__cur.execute(f"SELECT * FROM users WHERE id={user_id}")
        res: list = self.__cur.fetchall()
        if res is None or len(res) == 0:
            return None
        return User(*res[0])

    def __delete_user(self, user_id):
        self.__cur.execute(f"DELETE FROM users WHERE id={user_id}")

    def set_user_status(self, user: User, status):
        user_x = self.get_user(user.id)
        if user_x is None:
            user.status = "Guest"
            self.add_user(user)
        else:
            self.__delete_user(user.id)
            user_x.status = status
            self.add_user(user_x)

    def close(self):
        self.__cur.close()
        self.__base.close()

    def get_super_admin(self):
        self.__cur.execute(f"SELECT * FROM users WHERE status='SuperAdmin'")
        res: list = self.__cur.fetchall()
        return User(*res[0])


database = DataBase("database.db")
user_help: dict = None


def get_user_by_msg(message: types.Message):
    id = message.from_user.id
    fn = message.from_user.first_name if message.from_user.first_name is not None else ""
    ln = message.from_user.last_name if message.from_user.last_name is not None else ""
    return User(id, str(fn + " " + ln).strip(), "Guest")


def get_user_status(user_id):
    user: User = database.get_user(user_id)
    if user is None:
        return None
    return user.status
