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

    def get_request(self, request, tup=False, color=False):
        cur = self.base.cursor()

        table = self.table
        version = 'value'

        if color:
            table = "appcolors"
            version = cur.execute(f"SELECT value FROM constant WHERE name == 'version'").fetchall()[0][0]
        result = cur.execute(f"SELECT {version} FROM {table} WHERE name == '{request}'").fetchall()

        if not result and Admin.admin:
            print(f"По запросу {request} ничего не найдено")
            return
        else:
            result = result[0][0]
            pprint(result, " Результат запроса ", request)

        if tup:
            result = list(map(lambda x: int(x), result.split()))
        elif color:
            if "#" not in result:
                result = '#' + ''.join(map(lambda i: f"{hex(int(i))}"[2:], result.split()))

        return result

    def get_full_request(self, col_check, get_col, if_request,
                         tup=False, color=False, null=False, table=None, all=True):
        cur = self.base.cursor()

        if not table:
            table = self.table

        if color:
            table = "appcolors"

        if null:
            result = cur.execute(f"SELECT {get_col} FROM {table}").fetchall()
        else:
            result = cur.execute(f"SELECT {get_col} FROM {table} WHERE {col_check} == '{if_request}'").fetchall()

        if all:
            pprint(result, " Результат полного запроса ", if_request)
            return result

        if not result and Admin.admin:
            print(f"По запросу {if_request} ничего не найдено")
            return
        else:
            result = result[0][0]
            pprint(result, " Результат полного запроса ", if_request)

        if tup:
            result = list(map(lambda x: int(x), result.split()))
        elif color:
            if "#" not in result:
                result = '#' + ''.join(map(lambda i: f"{hex(int(i))}"[2:], result.split()))

        return result

    def change_base(self, name, value):
        cur = self.base.cursor()

        cur.execute(f"""UPDATE {self.table} SET value == '{value}' WHERE name == '{name}'""")
        self.base.commit()
        pprint("Изменена база данных ", name, " ", value)


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

        self.coef_x = self.wight_window / 1920
        self.coef_y = self.height_window / 1080
        self.coef_font = (self.coef_x / 2 + self.coef_y) / 1.5
        # self.coef_x = 1
        # self.coef_y = 1
        pprint(self.coef_x, " ", self.coef_y, " Коэфиценты")

    def get_w_h(self):
        return self.wight_window, self.height_window


    def change_size_window(self, size_x, size_y):
        self.wight_window = size_x
        self.height_window = size_y

    def adaptation(self, value, font=False):
        if font:
            if type(value) is list:
                value = value[0]
            return int(int(value) * self.coef_font)
        c = 0
        list_tmp = list()
        for i in value:
            if c % 2 == 0:
                list_tmp.append(int(int(i) * self.coef_x))  # здесь инт используется как уборка остатка
            else:
                list_tmp.append(int(int(i) * self.coef_y))
            c += 1
        return list_tmp


class Language:
    def __init__(self):
        self.base = sqlite3.connect("data/SQL/Constant.db")
        cur = self.base.cursor()
        self.language = cur.execute(f"SELECT value FROM constant WHERE name == 'language'").fetchall()[0][0]

    def request(self, rec):
        cur = self.base.cursor()

        result = cur.execute(f"SELECT {self.language} FROM language WHERE name == '{rec}'").fetchall()

        if not result:
            print("Пустой запрос язык", rec)
            return
        pprint(result[0][0], " Результат запроса языка ", rec)
        return result[0][0]




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

