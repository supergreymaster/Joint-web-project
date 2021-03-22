import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QTextEdit
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import QSize, Qt

from designer.secondary_functions import Request, Work_size_window

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
        self.setGeometry(int(WIN.wight_window // 3.4), int(WIN.height_window // 4.5), size_win[0], size_win[1])
        CSS_bg = f"background-color: rgb{REQUEST.get_request('color_background', color=True)};"

        self.label_main_window = QLabel(self)
        self.label_main_window.setGeometry(0, 0, size_win[0], size_win[1])
        self.label_main_window.setStyleSheet("QLabel{" + CSS_bg + "}")

        self.setWindowTitle(REQUEST.get_request("title_name"))

        self.main_work = Main_work()

        self.general_window()
        self.navigation_window()


    def general_window(self):
        self.main_work.window["general"] = list()

        self.gen_but_setting = QPushButton(self)
        pos = AD([725, 25, 60, 60])
        self.gen_but_setting.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.gen_but_setting.setIcon(QIcon("data/img/setting_button.png"))
        size = AD([50, 50])
        self.gen_but_setting.setIconSize(QSize(size[0], size[1]))
        self.gen_but_setting.setStyleSheet("""QPushButton{border: none;}""")
        self.main_work.window["general"].append(self.gen_but_setting)

        self.gen_but_setting.show()  # <---del

        self.gen_lab_head = QLabel(self)
        color = REQUEST.get_request("color_head", color=True)
        text_col = f"background-color: rgb{color};"
        pos = AD([0, 0, 800, 25])
        self.gen_lab_head.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.gen_lab_head.setStyleSheet("QLabel{" + text_col + "}")
        self.main_work.window["general"].append(self.gen_lab_head)

        self.gen_but_exit = QPushButton(self)
        pos = AD([780, 8, 10, 10])
        self.gen_but_exit.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.gen_but_exit.setStyleSheet("QPushButton{border: none;}")
        self.gen_but_exit.setIcon(QIcon("data/img/exit_button.png"))
        size = AD([10, 10])
        self.gen_but_exit.setIconSize(QSize(size[0], size[1]))
        self.gen_but_exit.clicked.connect(self.main_work.exit_program)
        self.main_work.window["general"].append(self.gen_but_exit)

        self.gen_but_roll_up = QPushButton(self)
        pos = AD([760, 8, 10, 10])
        self.gen_but_roll_up.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.gen_but_roll_up.setStyleSheet("QPushButton{border: none;}")
        self.gen_but_roll_up.setIcon(QIcon("data/img/roll_up_button.png"))
        size = AD([10, 10])
        self.gen_but_roll_up.setIconSize(QSize(size[0], size[1]))
        self.gen_but_roll_up.clicked.connect(self.tmp)
        self.main_work.window["general"].append(self.gen_but_roll_up)

    def navigation_window(self):
        self.main_work.window["navigation"] = list()

        size_window = AD(REQUEST.get_request("size_display", tup=True))
        pos_top = AD([0, 25])[1]

        self.gen_lab_nav = QLabel(self)
        color = REQUEST.get_request("color_nav", color=True)
        text_col = f"background-color: rgb{color};"
        pos = [0, pos_top, size_window[0] // 4, size_window[1] - pos_top]
        self.gen_lab_nav.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.gen_lab_nav.setStyleSheet("QLabel{" + text_col + "}")
        self.main_work.window["navigation"].append(self.gen_lab_nav)

        count = int(REQUEST.get_request("count_nav_but"))
        pos = [0, pos_top, size_window[0] // 4, (size_window[1] - pos_top) // count]
        font = QFont()
        font.setPointSize(AD(16, font=True))

        file = open("data/text/" + REQUEST.get_request("name_file_nav"), encoding="utf-8").readlines()
        for i in range(count):
            if len(file) < i + 1:
                text = ""
            else:
                text = file[i]
            self.nav_button = QPushButton(self)
            self.nav_button.setGeometry(pos[0], pos[1] + ((size_window[1] - pos_top) // count) * i, pos[2], pos[3])
            self.nav_button.setStyleSheet("QPushButton{" + text_col + "}")
            self.nav_button.setFont(font)
            self.nav_button.setText(text)

    def tmp(self):
        self.showMinimized()


class Main_work:
    def __init__(self):
        self.window = {}

    def exit_program(self):
        sys.exit()


def except_hook(cls, exception, traceback):  # если произойдет ошибка то Pyqt5 не будет замалчивать её
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("photo/game_icon.png"))
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
