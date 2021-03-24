import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QTextEdit
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import QSize, Qt

from designer.secondary_functions import Request, Work_size_window, pprint

REQUEST = Request()
WIN = Work_size_window()
AD = WIN.adaptation


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        size_win = AD(REQUEST.get_request("size_display", tup=True))
        pprint(size_win, " Ширина и высота приложения")
        self.setGeometry((WIN.wight_window - size_win[0]) // 2, (WIN.height_window - size_win[1]) // 2,
                         size_win[0], size_win[1])
        CSS_bg = f"background-color: rgb{REQUEST.get_request('color_background', color=True)};"

        self.label_main_window = QLabel(self)
        self.label_main_window.setGeometry(0, 0, size_win[0], size_win[1])
        self.label_main_window.setStyleSheet("QLabel{" + CSS_bg + "}")

        self.setWindowTitle(REQUEST.get_request("title_name"))

        self.main_work = Main_work()

        self.general_window()
        self.navigation_window()
        self.start_work_window()


    def general_window(self):
        self.main_work.window["general"] = list()

        self.size_window = REQUEST.get_request("size_display", tup=True)

        self.pos_top = AD([0, 25])[1]


        self.gen_lab_head = QLabel(self)
        color = REQUEST.get_request("color_head", color=True)
        CSS_color = f"background-color: rgb{color};"
        pos = AD([0, 0, self.size_window[0], 25])
        self.gen_lab_head.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.gen_lab_head.setStyleSheet("QLabel{" + CSS_color + "}")
        self.main_work.window["general"].append(self.gen_lab_head)

        self.gen_but_setting = QPushButton(self)
        pos = AD([int(self.size_window[0] * 0.925), 6, 15, 15])
        self.gen_but_setting.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.gen_but_setting.setIcon(QIcon("data/img/setting_button.png"))
        size = AD([15, 15])
        self.gen_but_setting.setIconSize(QSize(size[0], size[1]))
        self.gen_but_setting.setStyleSheet("""QPushButton{border: none;}""")
        self.gen_but_setting.clicked.connect(self.main_work.setting)
        self.main_work.window["general"].append(self.gen_but_setting)

        self.gen_but_exit = QPushButton(self)
        pos = AD([int(self.size_window[0] * 0.975), 8, 10, 10])
        self.gen_but_exit.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.gen_but_exit.setStyleSheet("QPushButton{border: none;}")
        self.gen_but_exit.setIcon(QIcon("data/img/exit_button.png"))
        size = AD([10, 10])
        self.gen_but_exit.setIconSize(QSize(size[0], size[1]))
        self.gen_but_exit.clicked.connect(self.main_work.exit_program)
        self.main_work.window["general"].append(self.gen_but_exit)

        self.gen_but_roll_up = QPushButton(self)
        pos = AD([int(self.size_window[0] * 0.95), 8, 10, 10])
        self.gen_but_roll_up.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.gen_but_roll_up.setStyleSheet("QPushButton{border: none;}")
        self.gen_but_roll_up.setIcon(QIcon("data/img/roll_up_button.png"))
        size = AD([10, 10])
        self.gen_but_roll_up.setIconSize(QSize(size[0], size[1]))
        self.gen_but_roll_up.clicked.connect(self.roll_up)
        self.main_work.window["general"].append(self.gen_but_roll_up)

    def navigation_window(self):
        self.main_work.window["navigation"] = list()

        tap_list = [self.main_work.work1, self.main_work.work2, self.main_work.work3]


        self.gen_lab_nav = QLabel(self)
        color = REQUEST.get_request("color_nav", color=True)
        CSS_color = f"background-color: rgb{color};"
        pos = AD([0, 25, self.size_window[0] // 4, self.size_window[1] - 25])
        self.gen_lab_nav.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.gen_lab_nav.setStyleSheet("QLabel{" + CSS_color + "}")
        self.main_work.window["navigation"].append(self.gen_lab_nav)

        count = int(REQUEST.get_request("count_nav_but"))
        pos = AD([0, 25, self.size_window[0] // 4, (self.size_window[1] - self.pos_top) // count])
        font = QFont()
        font.setPointSize(AD(16, font=True))

        color_text = REQUEST.get_request("color_text", color=True)
        CSS_color_text = f"color: rgb{(color_text[0], color_text[1], color_text[2])};"

        file = open("data/text/" + REQUEST.get_request("name_file_nav"), encoding="utf-8").readlines()
        for i in range(count):
            if len(file) < i + 1:
                text = ""
            else:
                text = file[i]
            if len(tap_list) < i + 1:
                click = self.main_work.void
            else:
                click = tap_list[i]
            self.nav_button = QPushButton(self)
            self.nav_button.setGeometry(pos[0], pos[1] + pos[3] * i, pos[2], pos[3])
            self.nav_button.setStyleSheet("QPushButton{" + CSS_color + " "
                                          + CSS_color_text + "}")
            self.nav_button.setFont(font)
            self.nav_button.setText(text)
            self.nav_button.clicked.connect(click)
            self.main_work.window["navigation"].append(self.nav_button)

    def setting_window(self):
        self.main_work.window["setting"] = list()
        self.main_work.window["second"] = list()

    def roll_up(self):
        self.showMinimized()

    def start_work_window(self):
        self.main_work.window["start"] = list()
        self.main_work.window["second"] = list()

        self.st_text_monologue = QTextEdit(self)
        pos = AD([self.size_window[0] // 3, self.size_window[1] // 8,
                 self.size_window[0] - self.size_window[0] // 2.5,
                 self.size_window[1] // 1.5])

        font = QFont()
        font.setPointSize(20)
        self.st_text_monologue.setFont(font)

        color_text = REQUEST.get_request("color_text", color=True)
        CSS_color_text = f"color: rgb{(color_text[0], color_text[1], color_text[2])};"

        color = REQUEST.get_request("color_background", color=True)
        CSS_color = f"background-color: rgb{color};"

        self.st_text_monologue.setStyleSheet("QTextEdit{" + CSS_color +
                                             CSS_color_text +
                                             "border:none;" + "}")  # пока не завершено
        self.st_text_monologue.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.st_text_monologue.setEnabled(False)
        text = open("data/text/start_monologue.txt", encoding="utf-8").readlines()
        for i in text:
            self.st_text_monologue.append(i)


class Main_work:
    def __init__(self):
        self.window = {}

    def exit_program(self):
        sys.exit()

    def work1(self):
        print("1")

    def work2(self):
        print("2")

    def work3(self):
        print("3")

    def void(self):
        pass

    def setting(self):
        pprint("Зашёл в setting")


def except_hook(cls, exception, traceback):  # если произойдет ошибка то Pyqt5 не будет замалчивать её
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("photo/game_icon.png"))
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
