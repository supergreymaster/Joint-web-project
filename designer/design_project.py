import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QTextEdit
from PyQt5.QtGui import QPixmap, QFont, QIcon, QCursor
from PyQt5.QtCore import QSize, Qt

from designer.secondary_functions import Request, Work_size_window, pprint

REQUEST = Request()
WIN = Work_size_window()
AD = WIN.adaptation


CSS_bg = "background-color: "
CSS_border = "border: "
CSS_col = "color: "

CSS_but = "QPushButton"
CSS_lab = "QLabel"
CSS_TE = "QTextEdit"

CSS_hov = ":hover"
CSS_pre = ":pressed"


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.cur = 0
        # cur_img_con = QPixmap("data/img/cursor_con.png").scaled(22, 22)
        # cur = QCursor(cur_img_con)
        # self.setCursor(cur)
        # cur_img = QPixmap("data/img/cursor.png").scaled(22, 22)
        # self.cur = QCursor(cur_img)

        self.setWindowFlags(Qt.FramelessWindowHint)
        size_win = AD(REQUEST.get_request("size_display", tup=True))
        pprint(size_win, " Ширина и высота приложения")
        self.setGeometry((WIN.wight_window - size_win[0]) // 2, (WIN.height_window - size_win[1]) // 2,
                         size_win[0], size_win[1])

        tmp_CSS = CSS_bg + REQUEST.get_request('background', color=True) + ";"

        self.label_main_window = QLabel(self)
        self.label_main_window.setGeometry(0, 0, size_win[0], size_win[1])
        self.label_main_window.setStyleSheet(CSS_lab + "{" + tmp_CSS + "}")

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
        pos = AD([0, 0, self.size_window[0], 25])
        self.gen_lab_head.setGeometry(pos[0], pos[1], pos[2], pos[3])
        tmp_CSS = CSS_bg + REQUEST.get_request("head", color=True) + ";"
        self.gen_lab_head.setStyleSheet(CSS_lab + "{" + tmp_CSS + "}")
        self.main_work.window["general"].append(self.gen_lab_head)

        self.gen_but_setting = QPushButton(self)
        pos = AD([int(self.size_window[0] * 0.925), 6, 15, 15])
        self.gen_but_setting.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.gen_but_setting.setIcon(QIcon("data/img/setting_button.png"))
        size = AD([15, 15])
        self.gen_but_setting.setIconSize(QSize(size[0], size[1]))
        tmp_CSS = CSS_border + "none;"
        self.gen_but_setting.setStyleSheet(CSS_but + "{" + tmp_CSS + "}")
        self.gen_but_setting.clicked.connect(self.main_work.setting)
        self.main_work.window["general"].append(self.gen_but_setting)

        self.gen_but_exit = QPushButton(self)
        pos = AD([int(self.size_window[0] * 0.975), 8, 10, 10])
        self.gen_but_exit.setGeometry(pos[0], pos[1], pos[2], pos[3])
        tmp_CSS = CSS_border + "none;"
        self.gen_but_exit.setStyleSheet(CSS_but + "{" + tmp_CSS + "}")
        self.gen_but_exit.setIcon(QIcon("data/img/exit_button.png"))
        size = AD([10, 10])
        self.gen_but_exit.setIconSize(QSize(size[0], size[1]))
        self.gen_but_exit.clicked.connect(self.main_work.exit_program)
        self.main_work.window["general"].append(self.gen_but_exit)

        self.gen_but_roll_up = QPushButton(self)
        pos = AD([int(self.size_window[0] * 0.95), 8, 10, 10])
        self.gen_but_roll_up.setGeometry(pos[0], pos[1], pos[2], pos[3])
        tmp_CSS = CSS_border + "none;"
        self.gen_but_roll_up.setStyleSheet(CSS_but + "{" + tmp_CSS + "}")
        self.gen_but_roll_up.setIcon(QIcon("data/img/roll_up_button.png"))
        size = AD([10, 10])
        self.gen_but_roll_up.setIconSize(QSize(size[0], size[1]))
        self.gen_but_roll_up.clicked.connect(self.roll_up)
        self.main_work.window["general"].append(self.gen_but_roll_up)

    def navigation_window(self):
        self.main_work.window["navigation"] = list()

        tap_list = [self.main_work.work1, self.main_work.work2, self.main_work.work3]


        self.gen_lab_nav = QLabel(self)
        pos = AD([0, 25, self.size_window[0] // 4, self.size_window[1] - 25])
        self.gen_lab_nav.setGeometry(pos[0], pos[1], pos[2], pos[3])
        tmp_CSS = CSS_bg + REQUEST.get_request("navigation", color=True) + ";"
        self.gen_lab_nav.setStyleSheet(CSS_lab + "{" + tmp_CSS + "}")
        self.main_work.window["navigation"].append(self.gen_lab_nav)

        count = int(REQUEST.get_request("count_nav_but"))
        pos = AD([0, 25, self.size_window[0] // 4, (self.size_window[1] - self.pos_top) // count])
        font = QFont()
        font.setPointSize(AD(16, font=True))

        tmp_CSS = CSS_col + REQUEST.get_request("nav_text", color=True) + "; "
        tmp1_CSS = CSS_border + REQUEST.get_request('radius_border') + " solid " \
                    + REQUEST.get_request('nav_border', color=True) + "; "
        tmp2_CSS = CSS_bg + REQUEST.get_request('navigation', color=True) + "; "

        tmp_h_CSS = CSS_col + REQUEST.get_request("nav_sec_text", color=True) + "; "
        tmp1_h_CSS = CSS_bg + REQUEST.get_request("nav_hover", color=True) + "; "

        tmp_p_CSS = CSS_bg + REQUEST.get_request("nav_bg_pres", color=True) + "; "
        tmp1_p_CSS = CSS_col + REQUEST.get_request("nav_pres_text", color=True) + "; "

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
            self.nav_button.setStyleSheet(CSS_but + "{" + tmp_CSS + tmp1_CSS + tmp2_CSS + "}" + " " + \
                                          CSS_but + CSS_hov + "{" + tmp_h_CSS + tmp1_h_CSS + "}" + " " + \
                                          CSS_but + CSS_pre + "{" + tmp_p_CSS + tmp1_p_CSS + "}")

            self.nav_button.setFont(font)
            self.nav_button.setText(text)
            self.nav_button.clicked.connect(click)
            if self.cur:
                self.nav_button.setCursor(self.cur)
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

        tmp_CSS = CSS_col + REQUEST.get_request("text", color=True) + "; "
        tmp1_CSS = CSS_bg + REQUEST.get_request("background", color=True) + "; "

        self.st_text_monologue.setStyleSheet(CSS_TE + "{" + tmp_CSS + tmp1_CSS + "}")  # пока не завершено
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
