import sqlite3
import sys
from win32api import GetSystemMetrics

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

        result = cur.execute(f"SELECT value, win FROM {self.table} WHERE name == '{request}'").fetchall()
        if not result and Admin.admin:
            print(f"По запросу {request} ничего не найдено")
            return
        else:
            pprint(result, " Результат запроса ", request)
            if result[0][1] == "True":
                result = window.adaptation(result[0][0])
            else:
                result = result[0][0]
        if tup:
            result = list(map(lambda x: int(x), result.split()))

        return result

    def get_full_request(self, col_check, get_col, if_request, tup=False):
        cur = self.base.cursor()

        result = cur.execute(f"SELECT {get_col} FROM {self.table} WHERE {col_check} == '{if_request}'").fetchall()[0][0]
        if not result and Admin.admin:
            print(f"По запросу {if_request} ничего не найдено")
            return
        else:
            pprint(result, " Результат запроса ", if_request)
            if result[0][1]:
                result = window.adaptation(result[0][1])
            else:
                result = result[0][0]
        if tup:
            result = list(map(lambda x: int(x), result.split()))

        return result


class Work_size_window:
    def __init__(self):
        self.platform = sys.platform
        if self.platform == "win32":
            self.wight_window = GetSystemMetrics(0)
            self.height_window = GetSystemMetrics(1)
        else:
            self.wight_window = 1920
            self.height_window = 1080
        pprint(self.platform, " Операционая система")
        pprint("width=", self.wight_window, " Разрешение экрана")
        pprint("height=", self.height_window, " Разрешение экрана")

        self.coef_x = self.wight_window // 1920
        self.coef_y = self.height_window // 1080

    def get_w_h(self):
        return self.wight_window, self.height_window

    def change_size_window(self, size_x, size_y):
        self.wight_window = size_x
        self.height_window = size_y

    def adaptation(self, value):
        c = 0
        text = ''
        for i in value.split():
            if c % 2 == 0:
                text = text + str(int(int(i) * self.coef_x))  # здесь инт используется как уборка остатка
            else:
                text = text + str(int(int(i) * self.coef_y))
            text = text + " "
            c += 1
        return text

def pprint(*text):
    if Admin.admin:
        tmp = ''
        for i in text:
            tmp = tmp + str(i)
        print(tmp)


class Admin:
    admin = False
    file = open("data/text/admin.txt", encoding="utf-8").read()
    if file == "False":
        admin = False
    elif file == "True":
        admin = True


Admin()
window = Work_size_window()

