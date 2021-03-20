import sqlite3


class Request:
    def __init__(self):
        self.base = sqlite3.connect("data/SQL/Constant.db")
        self.table = "constant"

    def setRequest(self, name):
        if ".db" not in name:
            name = name + ".db"

        self.base = sqlite3.connect(f"data/SQL/{name}")

    def setTable(self, name):
        self.table = name

    def get_request(self, request, tup=False):
        cur = self.base.cursor()

        result = cur.execute(f"SELECT value FROM {self.table} WHERE name == '{request}'").fetchall()[0][0]
        if not result and Admin.admin:
            print(f"По запросу {request} ничего не найдено")
            return
        if tup:
            result = list(map(lambda x: int(x), result.split()))

        return result

    def get_full_request(self, col_check, get_col, if_request, tup=False):
        cur = self.base.cursor()

        result = cur.execute(f"SELECT {get_col} FROM {self.table} WHERE {col_check} == '{if_request}'").fetchall()[0][0]
        if not result and Admin.admin:
            print(f"По запросу {if_request} ничего не найдено")
            return
        if tup:
            result = list(map(lambda x: int(x), result.split()))

        return result


class Admin:
    admin = False
    file = open("data/text/admin.txt", encoding="utf-8").read()
    if file == "False":
        admin = False
    elif file == "True":
        admin = True


Admin()
