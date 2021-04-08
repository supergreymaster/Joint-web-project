import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QTextEdit, QComboBox, QFileDialog
from PyQt5.QtGui import QPixmap, QFont, QIcon, QCursor
from PyQt5.QtCore import QSize, Qt

from designer.secondary_functions import Request, Work_size_window, pprint, Language

tmp = Language()
LANGUAGE = tmp.request

REQUEST = Request()
WIN = Work_size_window()
AD = WIN.adaptation


CSS_bg = "background-color: "
CSS_border = "border: "
CSS_col = "color: "

CSS_but = "QPushButton"
CSS_lab = "QLabel"
CSS_TE = "QTextEdit"
CSS_CB = "QComboBox"

CSS_hov = ":hover"
CSS_pre = ":pressed"


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.main_work = Main_work()
        self.main_work.window["save"] = list()
        self.initUI()

    def initUI(self):
        self.CSS_dict = {}
        self.cur = 0
        # cur_img_con = QPixmap("data/img/cursor_con.png").scaled(22, 22)
        # cur = QCursor(cur_img_con)
        # self.setCursor(cur)
        # cur_img = QPixmap("data/img/cursor.png").scaled(22, 22)
        # self.cur = QCursor(cur_img)

        self.setWindowFlags(Qt.FramelessWindowHint)

        size_win = AD(REQUEST.get_request("size_display", tup=True))
        pprint(size_win, " Ширина и высота приложения'")
        self.setGeometry((WIN.wight_window - size_win[0]) // 2, (WIN.height_window - size_win[1]) // 2,
                         size_win[0], size_win[1])

        tmp_CSS = CSS_bg + REQUEST.get_request('background', color=True) + ";"

        self.label_main_window = QLabel(self)
        self.label_main_window.setGeometry(0, 0, size_win[0], size_win[1])
        self.label_main_window.setStyleSheet(CSS_lab + "{" + tmp_CSS + "}")

        self.setWindowTitle(REQUEST.get_request("title_name"))

        self.CSS_create()

        self.general_window()
        self.navigation_window()
        # self.start_work_window()
        # self.setting_window()
        self.window_2()

    def CSS_create(self):

        nav_text_CSS = CSS_col + REQUEST.get_request("nav_text", color=True) + "; "
        rad_bor_CSS = CSS_border + REQUEST.get_request('radius_border') + " solid " \
                      + REQUEST.get_request('nav_border', color=True) + "; "
        nav_bg_CSS = CSS_bg + REQUEST.get_request('navigation', color=True) + "; "

        nav_sec_text_h_CSS = CSS_col + REQUEST.get_request("nav_sec_text", color=True) + "; "
        nav_h_CSS = CSS_bg + REQUEST.get_request("nav_hover", color=True) + "; "

        nav_bg_p_CSS = CSS_bg + REQUEST.get_request("nav_bg_pres", color=True) + "; "
        nav_text_p_CSS = CSS_col + REQUEST.get_request("nav_pres_text", color=True) + "; "

        text_CSS = CSS_col + REQUEST.get_request("text", color=True) + "; "
        bg_CSS = CSS_bg + REQUEST.get_request("background", color=True) + "; "
        border_CSS = CSS_border + "none; "

        head_CSS = CSS_bg + REQUEST.get_request("head", color=True)

        self.CSS_dict["gen_lab_head"] = CSS_lab + "{" + head_CSS + ";}"

        border = CSS_but + "{" + border_CSS + "}"
        self.CSS_dict["gen_but_head"] = border
        self.CSS_dict["gen_but_exit"] = border
        self.CSS_dict["gen_but_roll_up"] = border

        self.CSS_dict["gen_lab_nav"] = CSS_lab + "{" + nav_bg_CSS + ";}"


        self.CSS_dict["nav_button"] = CSS_but + "{" + nav_text_CSS + rad_bor_CSS + nav_bg_CSS + "}" + " " + \
                                          CSS_but + CSS_hov + "{" + nav_sec_text_h_CSS + nav_h_CSS + "}" + " " + \
                                          CSS_but + CSS_pre + "{" + nav_bg_p_CSS + nav_text_p_CSS + "}"

        self.CSS_dict["st_text_monologue"] = CSS_TE + "{" + text_CSS + bg_CSS + border_CSS + "}"

        self.CSS_dict["set_lab_theme"] = CSS_lab + "{" + text_CSS + "}"
        self.CSS_dict["set_com_box_theme"] = CSS_CB + "{" + nav_text_CSS + nav_bg_CSS + "}"
        self.CSS_dict["set_but_save"] = CSS_but + "{" + nav_text_CSS + nav_bg_CSS + "}"
        self.CSS_dict["set_lab_cha_lan"] = CSS_lab + "{" + text_CSS + "}"
        self.CSS_dict["set_but_cha_lan"] = CSS_but + CSS_hov + "{" + rad_bor_CSS + "}"
        self.CSS_dict["win_2_but_find"] = CSS_but + "{" + nav_text_CSS + nav_bg_CSS + "}"

    def general_window(self):
        self.main_work.window["general"] = list()

        self.size_window = REQUEST.get_request("size_display", tup=True)

        self.pos_top = AD([0, 25])[1]


        self.gen_lab_head = QLabel(self)
        pos = AD([0, 0, self.size_window[0], 25])
        self.gen_lab_head.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.gen_lab_head.setStyleSheet(self.CSS_dict["gen_lab_head"])
        self.main_work.window["general"].append(self.gen_lab_head)

        self.gen_but_setting = QPushButton(self)
        pos = AD([int(self.size_window[0] * 0.925), 6, 15, 15])
        self.gen_but_setting.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.gen_but_setting.setIcon(QIcon("data/img/setting_button.png"))
        size = AD([15, 15])
        self.gen_but_setting.setIconSize(QSize(size[0], size[1]))
        self.gen_but_setting.setStyleSheet(self.CSS_dict["gen_but_head"])
        self.gen_but_setting.clicked.connect(self.main_work.setting)
        self.main_work.window["general"].append(self.gen_but_setting)

        self.gen_but_exit = QPushButton(self)
        pos = AD([int(self.size_window[0] * 0.975), 8, 10, 10])
        self.gen_but_exit.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.gen_but_exit.setStyleSheet(self.CSS_dict["gen_but_exit"])
        self.gen_but_exit.setIcon(QIcon("data/img/exit_button.png"))
        size = AD([10, 10])
        self.gen_but_exit.setIconSize(QSize(size[0], size[1]))
        self.gen_but_exit.clicked.connect(self.main_work.exit_program)
        self.main_work.window["general"].append(self.gen_but_exit)

        self.gen_but_roll_up = QPushButton(self)
        pos = AD([int(self.size_window[0] * 0.95), 8, 10, 10])
        self.gen_but_roll_up.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.gen_but_roll_up.setStyleSheet(self.CSS_dict["gen_but_roll_up"])
        self.gen_but_roll_up.setIcon(QIcon("data/img/roll_up_button.png"))
        size = AD([10, 10])
        self.gen_but_roll_up.setIconSize(QSize(size[0], size[1]))
        self.gen_but_roll_up.clicked.connect(self.roll_up)
        self.main_work.window["general"].append(self.gen_but_roll_up)

    def window_2(self):
        self.main_work.window["window_2"] = list()
        self.main_work.window["second"] = list()

        self.win_2_but_find = QPushButton(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 12,
                  25 + self.size_window[1] // 1.2, 100, 25])
        self.win_2_but_find.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.win_2_but_find.clicked.connect(self.choose_file)
        self.win_2_but_find.setStyleSheet(self.CSS_dict["win_2_but_find"])
        self.win_2_but_find.setText(LANGUAGE("find_file"))
        # self.win_2_but_find.clicked.connect(self.save)
        self.main_work.window["window_2"].append(self.win_2_but_find)
        self.main_work.window["second"].append(self.win_2_but_find)

        self.win_2_tex_ret = QTextEdit(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 12,
                  25 + self.size_window[1] // 12, 100, 25])
        self.win_2_tex_ret.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.win_2_tex_ret.append()


    def choose_file(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Картинка (*.png);;Картинка (*.jpg);;Все файлы (*)')[0]
        self.main_work.window["fname"] = fname
        pprint("Вставленна фотография' ", fname)


    def navigation_window(self):
        self.main_work.window["navigation"] = list()

        tap_list = [self.main_work.work1, self.main_work.work2, self.main_work.work3, self.main_work.setting]


        self.gen_lab_nav = QLabel(self)
        pos = AD([0, 25, self.size_window[0] // 4, self.size_window[1] - 25])
        self.gen_lab_nav.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.gen_lab_nav.setStyleSheet(self.CSS_dict["gen_lab_nav"])
        self.main_work.window["navigation"].append(self.gen_lab_nav)

        count = int(REQUEST.get_request("count_nav_but"))
        pos = AD([0, 25, self.size_window[0] // 4, (self.size_window[1] - self.pos_top) // count])
        font = QFont()
        font.setPointSize(AD(16, font=True))

        file = [LANGUAGE("nav_but_1"), LANGUAGE("nav_but_2"), LANGUAGE("nav_but_3"), LANGUAGE("nav_but_4")]
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
            # print(type(self.CSS_dict["nav_button"]) ,self.CSS_dict["nav_button"])
            self.nav_button.setStyleSheet(self.CSS_dict["nav_button"])

            self.nav_button.setFont(font)
            self.nav_button.setText(text)
            self.nav_button.clicked.connect(click)
            if self.cur:
                self.nav_button.setCursor(self.cur)
            self.main_work.window["navigation"].append(self.nav_button)

    def setting_window(self):
        self.main_work.window["setting"] = list()
        self.main_work.window["second"] = list()

        self.set_lab_theme = QLabel(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 10,
                  25 + self.size_window[1] // 10, 100, 50])
        self.set_lab_theme.setGeometry(pos[0], pos[1], pos[2], pos[3])
        # print(type(self.CSS_dict["set_lab_theme"]), self.CSS_dict["set_lab_theme"])
        self.set_lab_theme.setStyleSheet(self.CSS_dict["set_lab_theme"])
        self.set_lab_theme.setText("Тема")
        font = QFont()
        font.setPointSize(AD(20, font=True))
        self.set_lab_theme.setFont(font)
        self.main_work.window["setting"].append(self.set_lab_theme)
        self.main_work.window["second"].append(self.set_lab_theme)

        self.set_com_box_theme = QComboBox(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 12,
                  25 + self.size_window[1] // 10 * 2, 100, 25])
        self.set_com_box_theme.setGeometry(pos[0], pos[1], pos[2], pos[3])
        # self.set_com_box_theme.
        version = len(REQUEST.get_full_request("name", "*", "text", table="appcolors")[0]) - 3
        for i in range(1, version + 1):
            self.set_com_box_theme.addItem(f"version{i}")

        self.set_com_box_theme.setStyleSheet(self.CSS_dict["set_com_box_theme"])
        self.main_work.window["setting"].append(self.set_com_box_theme)
        self.main_work.window["second"].append(self.set_com_box_theme)

        self.set_but_save = QPushButton(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 12,
                  25 + self.size_window[1] // 3.5, 100, 25])
        self.set_but_save.setGeometry(pos[0], pos[1], pos[2], pos[3])

        self.set_but_save.setStyleSheet(self.CSS_dict["set_but_save"])
        self.set_but_save.setText(LANGUAGE("but_save"))
        self.set_but_save.clicked.connect(self.save)
        self.main_work.window["setting"].append(self.set_but_save)
        self.main_work.window["second"].append(self.set_but_save)

        self.set_lab_cha_lan = QLabel(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 2.8,
                  25 + self.size_window[1] // 7, 150, 35])
        self.set_lab_cha_lan.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.set_lab_cha_lan.setText(LANGUAGE("language_name"))
        self.set_lab_cha_lan.setStyleSheet(self.CSS_dict["set_lab_cha_lan"])
        self.set_lab_cha_lan.setFont(font)
        self.main_work.window["setting"].append(self.set_lab_cha_lan)
        self.main_work.window["second"].append(self.set_lab_cha_lan)

        self.set_but_cha_lan = QPushButton(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 3,
                  25 + self.size_window[1] // 5, 160, 110])
        self.set_but_cha_lan.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.set_but_cha_lan.setIcon(QIcon("data/img/" + LANGUAGE("way_image")))
        size = AD([150, 100])
        self.set_but_cha_lan.setIconSize(QSize(size[0], size[1]))
        self.set_but_cha_lan.setStyleSheet(self.CSS_dict["set_but_cha_lan"])
        self.set_but_cha_lan.clicked.connect(self.main_work.change_lan)
        self.main_work.window["setting"].append(self.set_but_cha_lan)
        self.main_work.window["second"].append(self.set_but_cha_lan)

    def save(self):
        # print(self.set_com_box_theme.currentText())
        self.main_work.save(self.set_com_box_theme.currentText())

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

        self.st_text_monologue.setStyleSheet(self.CSS_dict["st_text_monologue"])  # пока не завершено
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

    def save(self, version):
        pprint("Использовалась команда' ", "сохранение")
        REQUEST.change_base("version", version)

    def change_lan(self):
        pprint("Использовалась команда' ", "изменение языка")
        all_lang = REQUEST.get_full_request("name", "*", "language", table="language")[0][2:]
        now_lan = REQUEST.get_request("language")
        last_lan = ""
        war = False
        for i in all_lang:
            if i == now_lan:
                war = True
                continue
            if war:
                REQUEST.change_base("language", i)
                last_lan = i
                war = False
                break
        if war:
            REQUEST.change_base("language", all_lang[0])
            last_lan = all_lang[0]
        pprint("Изменён язык' ", "с ", now_lan, " на ", last_lan)

    def void(self):
        pass

    def setting(self):
        pprint("Использовалась команда' ", "войти в ", "настройки")


def except_hook(cls, exception, traceback):  # если произойдет ошибка то Pyqt5 не будет замалчивать её
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("photo/game_icon.png"))
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
