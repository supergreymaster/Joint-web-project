import json
import sqlite3
import sys
import datetime
from win32api import GetSystemMetrics


class Request:  # Работает с базами данных
    def __init__(self):  # Ставит первоначальныю базу данных и таблицу
        self.base = sqlite3.connect("data/SQL/Constant.db")
        self.table = "constant"
        self.admin_check(self.table)

    def setRequest(self, name):  # при вызове сменяет базу данных
        if ".db" not in name:
            name = name + ".db"

        self.base = sqlite3.connect(f"data/SQL/{name}")
        self.admin_check(self.table)

    def setTable(self, name):  # при вызове сменяет таблицу
        self.table = name
        self.admin_check(self.table)

    def get_request(self, request, tup=False, color=False):  # запрашивает данные
        cur = self.base.cursor()

        table = self.table
        version = 'value'

        if color:  # если цвет правда, то он сменяет таблицу
            table = "appcolors"
            self.admin_check(table)

            version = cur.execute(f"SELECT value FROM constant WHERE name == 'version'").fetchall()[0][0]
        result = cur.execute(f"SELECT {version} FROM {table} WHERE name == '{request}'").fetchall()

        try:
            if not result[0][0].strip():  # обрабатывает пустой запрос
                pprint(f"По запросу {request} ничего не найдено'", warning="warning")
                return ""
            else:
                result = result[0][0]
                pprint(result, " Результат запроса' ", request)
        except IndexError:
            pprint(f"По запросу {request} ничего не найдено'", warning="warning")
            return ""

        if tup:  # если правда то возращает в виде списка числа
            result = list(map(lambda x: int(x), result.split()))
        elif color:  # если правда переводит цвет в шестнацитиричную систему
            if Admin.admin and (len(result.split()) != 3 or "#" in result):
                pprint("Некоректный цвет по запросу ", request, " ответ: ", result, warning="error")
            if "#" not in result:
                result = '#' + ''.join(map(lambda i: f"{hex(int(i))}"[2:], result.split()))

        return result

    def get_full_request(self, col_check, get_col, if_request,
                         tup=False, color=False, null=False, table=None, all=True):
        # запрашивает полный запрос с таблицей и всеми значениями
        cur = self.base.cursor()
        tablee = str(table)
        table = tablee

        if not tablee:  # если таблица не заполнена, то вводится стандартная
            table = self.table

        if color:  # если цвет правда, то он сменяет таблицу
            table = "appcolors"
            self.admin_check(table)

        if tablee:
            table = tablee

        if null:  # запрашивает без условия
            result = cur.execute(f"SELECT {get_col} FROM {table}").fetchall()
        else:
            result = cur.execute(f"SELECT {get_col} FROM {table} WHERE {col_check} == '{if_request}'").fetchall()

        if all:  # отправляет без форматировния
            pprint(result, " Результат полного запроса' ", if_request)
            return result

        try:
            if not result[0][0].strip():
                pprint(f"По запросу {if_request} ничего не найдено'", warning="warning")
                return
            else:
                result = result[0][0]
                pprint(result, " Результат полного запроса' ", if_request)
        except IndexError:
            pprint(f"По запросу {if_request} ничего не найдено'", warning="warning")

        if tup:
            if Admin.admin and " " not in result:
                pprint("Список некоректен по запросу ", if_request, " ответ: ",
                       result, warning="error")
            result = list(map(lambda x: int(x), result.split()))
        elif color:
            if Admin.admin and (len(result.split()) != 3 or "#" in result):
                pprint("Некоректный цвет по запросу", if_request, " ответ: ", result, warning="error")
            if "#" not in result:
                result = '#' + ''.join(map(lambda i: f"{hex(int(i))}"[2:], result.split()))

        return result

    def change_base(self, name, value):  # изменяет базу данных
        cur = self.base.cursor()

        self.admin_check(self.table, value='name', com=1)
        self.admin_check(self.table, value='value', com=1)

        cur.execute(f"""UPDATE {self.table} SET value == '{value}' WHERE name == '{name}'""")
        self.base.commit()
        pprint("Изменена база данных' ", name, " ", value)

    def admin_check(self, table, value=None, com=0):
        if Admin.admin:
            if com == 0:
                try:
                    cur = self.base.cursor()
                    result = cur.execute(f"SELECT * FROM {table}").fetchall()
                except sqlite3.OperationalError:
                    pprint(f"Несуществует {self.base} базы данных или {table} таблицы", warning="error")
            elif com == 1:
                try:
                    cur = self.base.cursor()
                    result = cur.execute(f"SELECT {value} FROM {table}").fetchall()
                except sqlite3.OperationalError:
                    pprint(f"Стобца {value} не существует", warning="error")


class Work_size_window:  # работает с адаптацией окна
    def __init__(self):
        self.platform = sys.platform
        if self.platform == "win32":  # достает разрешение экрана
            self.wight_window = GetSystemMetrics(0)
            self.height_window = GetSystemMetrics(1)
        else:
            self.wight_window = 1920
            self.height_window = 1080
        pprint(self.platform, " Операционая система'")
        pprint("width=", self.wight_window, " Разрешение экрана x'")
        pprint("height=", self.height_window, " Разрешение экрана y'")

        # создает коэффиценты отношение экрана к первоначальному виду
        self.coef_x = self.wight_window / 1920
        self.coef_y = self.height_window / 1080
        self.coef_font = (self.coef_x / 2 + self.coef_y) / 1.5
        # self.coef_x = 1
        # self.coef_y = 1
        pprint(self.coef_x, " ", self.coef_y, " Коэфиценты'")

    def get_w_h(self):  # возвращает длинну и ширину экрана
        return self.wight_window, self.height_window

    def change_size_window(self, size_x, size_y):  # изменяет длинну экрана
        self.wight_window = size_x
        self.height_window = size_y
        Request().change_base("size_display", f"{size_x} {size_y}")

    def adaptation(self, value, font=False):  # функция адаптируящая все размеры
        if font:
            if type(value) is list:
                value = value[0]
            return int(int(value) * self.coef_font)
        c = 0

        if type(value) is list:
            pass
        else:
            pprint("Некоректные данные. не список. функция адаптация ", value, warning="error")

        list_tmp = list()
        for i in value:
            if c % 2 == 0:
                list_tmp.append(int(int(i) * self.coef_x))  # здесь инт используется как уборка остатка
            else:
                list_tmp.append(int(int(i) * self.coef_y))
            c += 1
        return list_tmp


class Language:  # Изменение языка
    def __init__(self):
        self.base = sqlite3.connect("data/SQL/Constant.db")
        cur = self.base.cursor()
        self.language = cur.execute(f"SELECT value FROM constant WHERE name == 'language'").fetchall()[0][0]

        self.admin_check()
        self.admin_check(table="language_value")
        self.admin_check(value="name", com=1)
        self.admin_check(value=self.language, com=1)

    def request(self, rec):
        cur = self.base.cursor()

        result = cur.execute(f"SELECT {self.language} FROM language WHERE name == '{rec}'").fetchall()

        try:
            if not result[0][0].strip():
                pprint("Пустой запрос язык' ", rec, warning="warning")
                return
        except IndexError:
            pprint("Пустой запрос язык' ", rec, warning="warning")
        pprint(result[0][0], " Результат запроса языка' ", rec)
        return result[0][0]

    # def request_value(self, rec):
    #     cur = self.base.cursor()
    #
    #     result = cur.execute(f"SELECT {self.language} FROM language_value WHERE name == '{rec}'").fetchall()
    #
    #     if not result:
    #         pprint("Пустой запрос язык' ", rec, warning="warning")
    #         return
    #     pprint(result[0][0], " Результат запроса языка' ", rec)
    #     return result[0][0]

    def admin_check(self, table="language", value=None, com=0):
        if Admin.admin:
            if com == 0:
                try:
                    cur = self.base.cursor()
                    result = cur.execute(f"SELECT * FROM {table}").fetchall()
                except sqlite3.OperationalError:
                    pprint(f"Несуществует {self.base} базы данных или {table} таблицы", warning="error")
            elif com == 1:
                try:
                    cur = self.base.cursor()
                    result = cur.execute(f"SELECT {value} FROM {table}").fetchall()
                except sqlite3.OperationalError:
                    pprint(f"Стобца {value} не существует", warning="error")


def pprint(*text, warning="default"):  # система отчетов
    if warning == "default":
        tmp = ""
        bs_name = ""
        for i in text:
            i = str(i)
            if "'" in i:
                bs_name = i.strip()[:-1]
            tmp = tmp + i

        tmp = f"{tmp} | время {datetime.datetime.now()}"
        if bs_name not in report.base["default"]:
            report.base["default"][bs_name] = list()
        report.base["default"][bs_name].append(tmp)
        report.base["all"].append(tmp)
        # print(report.base)
    elif warning == "error":
        tmp = ""
        for i in text:
            i = str(i)
            tmp = tmp + i
        tmp = f"{tmp} | время {datetime.datetime.now()}"
        report.base["error"].append(tmp)
        report.base["all"].append(tmp)
    else:
        tmp = ""
        for i in text:
            i = str(i)
            tmp = tmp + i
        tmp = f"{tmp} | время {datetime.datetime.now()}"
        report.base["warning"].append(tmp)
        report.base["all"].append(tmp)
    with open("data/reports/report.json", "w", encoding="utf-8") as file:
        json.dump(report.base, file, ensure_ascii=False)


class Report_database:
    base = {
        "default": {},
        "warning": [],
        "error": [],
        "all": []
    }


class Admin:  # система проверки админских прав
    admin = False
    file = open("data/text/admin.txt", encoding="utf-8").read()
    if file == "False":
        admin = False
    elif file == "True":
        admin = True


report = Report_database()
Admin()
