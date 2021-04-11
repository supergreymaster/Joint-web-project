import sys

# Импорт модулей PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QTextEdit, QComboBox, QFileDialog
from PyQt5.QtGui import QPixmap, QFont, QIcon, QCursor
from PyQt5.QtCore import QSize, Qt

# Импорт модулей из secondary_function и Main_work
from designer.Main_work import Main_work
from designer.secondary_functions import Request, Work_size_window, pprint, Language

# Создание заготовленых команд
tmp = Language()
LANGUAGE = tmp.request
LANGUAGE_VALUE = tmp.request_value

REQUEST = Request()
WIN = Work_size_window()
AD = WIN.adaptation


# Создание заготовленых CSS шаблонов
CSS_bg = "background-color: "
CSS_border = "border: "
CSS_col = "color: "

CSS_but = "QPushButton"
CSS_lab = "QLabel"
CSS_TE = "QTextEdit"
CSS_CB = "QComboBox"

CSS_hov = ":hover"
CSS_pre = ":pressed"


# Начало интерфейса
class Example(QWidget):
    def __init__(self):  # инициальзаруется Main_work
        super().__init__()
        self.main_work = Main_work()
        self.main_work.window["save"] = list()
        self.main_work.window["self"] = self
        self.initUI()

    def initUI(self):  # Фон и обновление интерфейса
        self.CSS_dict = {}
        self.cur = 0
        # cur_img_con = QPixmap("data/img/cursor_con.png").scaled(22, 22)
        # cur = QCursor(cur_img_con)
        # self.setCursor(cur)
        # cur_img = QPixmap("data/img/cursor.png").scaled(22, 22)
        # self.cur = QCursor(cur_img)

        # Убирает шапку
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Создает фон
        size_win = AD(REQUEST.get_request("size_display", tup=True))
        pprint(size_win, " Ширина и высота приложения'")
        self.setGeometry((WIN.wight_window - size_win[0]) // 2, (WIN.height_window - size_win[1]) // 2,
                         size_win[0], size_win[1])

        tmp_CSS = CSS_bg + REQUEST.get_request('background', color=True) + ";"

        self.label_main_window = QLabel(self)
        self.label_main_window.setGeometry(0, 0, size_win[0], size_win[1])
        self.label_main_window.setStyleSheet(CSS_lab + "{" + tmp_CSS + "}")

        self.setWindowTitle(REQUEST.get_request("title_name"))

        # Активирует функции
        self.CSS_create()

        self.font_create()
        self.general_window()
        self.navigation_window()
        self.start_work_window()
        self.setting_window()
        self.window_2()
        self.window_3()
        self.main_work.work1()

    def font_create(self):  # Создает шрифты
        self.font_text = QFont()
        self.font_text.setPointSize(AD(16, font=True))

        self.font_lab = QFont()
        self.font_lab.setPointSize(AD(20, font=True))

        self.font_but = QFont()
        self.font_but.setPointSize(AD(16, font=True))

    def CSS_create(self):  # Ставит шаблоны на объекты

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

        but = CSS_but + "{" + nav_text_CSS + rad_bor_CSS + nav_bg_CSS + "}" + " " + \
                                          CSS_but + CSS_hov + "{" + nav_sec_text_h_CSS + nav_h_CSS + "}" + " " + \
                                          CSS_but + CSS_pre + "{" + nav_bg_p_CSS + nav_text_p_CSS + "}"

        text = CSS_TE + "{" + nav_text_CSS + nav_bg_CSS + "}"

        lab = CSS_lab + "{" + text_CSS + "}"

        com_box = CSS_CB + "{" + nav_text_CSS + nav_bg_CSS + rad_bor_CSS + "}"

        self.CSS_dict["nav_button"] = but

        self.CSS_dict["st_text_monologue"] = CSS_TE + "{" + text_CSS + bg_CSS + border_CSS + "}"

        self.CSS_dict["set_lab_theme"] = lab
        self.CSS_dict["set_com_box_theme"] = com_box
        self.CSS_dict["set_but_save"] = but
        self.CSS_dict["set_lab_cha_lan"] = lab
        self.CSS_dict["set_but_cha_lan"] = but
        self.CSS_dict["win_2_but_find"] = but
        self.CSS_dict["win_2_tex_ret"] = text
        self.CSS_dict["win_2_but_txt"] = but
        self.CSS_dict["win_2_but_docx"] = but
        self.CSS_dict["win_2_but_mp3"] = but
        self.CSS_dict["win_3_scr"] = text
        self.CSS_dict["win_3_lan1"] = lab
        self.CSS_dict["win_3_com_box_lan"] = com_box
        self.CSS_dict["win_3_but_voice"] = but
        self.CSS_dict["win_3_but_copy"] = but
        self.CSS_dict["win_3_but_tran"] = but

    def general_window(self):  # Создает шапку
        self.main_work.window["general"] = list()
        self.main_work.window["second"] = list()

        self.size_window = REQUEST.get_request("size_display", tup=True)

        self.pos_top = 25

        # Создает фон шапки
        self.gen_lab_head = QLabel(self)
        pos = AD([0, 0, self.size_window[0], 25])
        self.gen_lab_head.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.gen_lab_head.setStyleSheet(self.CSS_dict["gen_lab_head"])
        self.main_work.window["general"].append(self.gen_lab_head)

        # Создает кнопку выхода из программы
        self.gen_but_exit = QPushButton(self)
        pos = AD([int(self.size_window[0] * 0.975), 8, 10, 10])
        self.gen_but_exit.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.gen_but_exit.setStyleSheet(self.CSS_dict["gen_but_exit"])
        self.gen_but_exit.setIcon(QIcon("data/img/exit_button.png"))
        size = AD([10, 10])
        self.gen_but_exit.setIconSize(QSize(size[0], size[1]))
        self.gen_but_exit.clicked.connect(self.main_work.exit_program)
        self.main_work.window["general"].append(self.gen_but_exit)

        # Создает кнопку сворачивания программы
        self.gen_but_roll_up = QPushButton(self)
        pos = AD([int(self.size_window[0] * 0.95), 8, 10, 10])
        self.gen_but_roll_up.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.gen_but_roll_up.setStyleSheet(self.CSS_dict["gen_but_roll_up"])
        self.gen_but_roll_up.setIcon(QIcon("data/img/roll_up_button.png"))
        size = AD([10, 10])
        self.gen_but_roll_up.setIconSize(QSize(size[0], size[1]))
        self.gen_but_roll_up.clicked.connect(self.roll_up)
        self.main_work.window["general"].append(self.gen_but_roll_up)

    def navigation_window(self):
        self.main_work.window["navigation"] = list()

        tap_list = [self.main_work.work1, self.main_work.work2, self.main_work.work3, self.main_work.setting]

        # Создает фон навигации
        self.gen_lab_nav = QLabel(self)
        pos = AD([0, 25,
                  self.size_window[0] // 4,
                  self.size_window[1] - 25])
        self.gen_lab_nav.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.gen_lab_nav.setStyleSheet(self.CSS_dict["gen_lab_nav"])
        self.main_work.window["navigation"].append(self.gen_lab_nav)

        count = int(REQUEST.get_request("count_nav_but"))
        pos = AD([0, 25,
                  self.size_window[0] // 4,
                  (self.size_window[1] - self.pos_top) // count])

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
            # Сохдает кнопки навигации
            self.nav_button = QPushButton(self)
            self.nav_button.setGeometry(pos[0], pos[1] + pos[3] * i, pos[2], pos[3])
            # print(type(self.CSS_dict["nav_button"]) ,self.CSS_dict["nav_button"])
            self.nav_button.setStyleSheet(self.CSS_dict["nav_button"])

            self.nav_button.setFont(self.font_but)
            self.nav_button.setText(text)
            self.nav_button.clicked.connect(click)
            if self.cur:
                self.nav_button.setCursor(self.cur)
            self.main_work.window["navigation"].append(self.nav_button)

    def start_work_window(self):  # Создает объекты начало работы
        self.main_work.window["start"] = list()

        # Создает монолог
        self.st_text_monologue = QTextEdit(self)
        pos = AD([self.size_window[0] // 3, self.size_window[1] // 8,
                 self.size_window[0] - self.size_window[0] // 2.5,
                 self.size_window[1] // 1.5])

        self.st_text_monologue.setFont(self.font_text)

        self.st_text_monologue.setStyleSheet(self.CSS_dict["st_text_monologue"])
        self.st_text_monologue.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.st_text_monologue.setEnabled(False)
        text = open("data/text/start_monologue.txt", encoding="utf-8").readlines()
        for i in text:
            self.st_text_monologue.append(i)
        self.main_work.window["start"].append(self.st_text_monologue)
        self.main_work.window["second"].append(self.st_text_monologue)

    def window_2(self):  # Создает объекты Распознователя
        self.main_work.window["window_2"] = list()

        # Создает кнопку преобразования из img в текст
        self.win_2_but_find = QPushButton(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 20,
                  25 + self.size_window[1] // 1.2,
                  self.size_window[0] // 6,
                  self.size_window[1] // 20])
        self.win_2_but_find.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.win_2_but_find.clicked.connect(self.main_work.choose_file)
        self.win_2_but_find.setStyleSheet(self.CSS_dict["win_2_but_find"])
        self.win_2_but_find.setText(LANGUAGE("find_file"))
        # self.win_2_but_find.clicked.connect(self.save)
        self.main_work.window["window_2"].append(self.win_2_but_find)
        self.main_work.window["second"].append(self.win_2_but_find)

        # Создает поле куда помещается текст
        self.win_2_tex_ret = QTextEdit(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 12,
                  25 + self.size_window[1] // 12,
                  self.size_window[0] // 1.666,
                  self.size_window[1] // 1.5])
        self.win_2_tex_ret.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.win_2_tex_ret.setStyleSheet(self.CSS_dict["win_2_tex_ret"])
        self.win_2_tex_ret.setFont(self.font_text)
        self.main_work.window["window_2"].append(self.win_2_tex_ret)
        self.main_work.window["second"].append(self.win_2_tex_ret)

        # Создает кнопку преобразования из тескта в файл txt
        self.win_2_but_txt = QPushButton(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 4,
                  25 + self.size_window[1] // 1.2,
                  self.size_window[0] // 8.33,
                  self.size_window[1] // 20])
        self.win_2_but_txt.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.win_2_but_txt.clicked.connect(self.main_work.transformation_on_txt)
        self.win_2_but_txt.setStyleSheet(self.CSS_dict["win_2_but_txt"])
        self.win_2_but_txt.setText(LANGUAGE("con_txt"))
        # self.win_2_but_find.clicked.connect(self.save)
        self.main_work.window["window_2"].append(self.win_2_but_txt)
        self.main_work.window["second"].append(self.win_2_but_txt)

        # Создает кнопку преобразования из текста в файл docx
        self.win_2_but_docx = QPushButton(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 2.5,
                  25 + self.size_window[1] // 1.2,
                  self.size_window[0] // 8.33,
                  self.size_window[1] // 20])
        self.win_2_but_docx.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.win_2_but_docx.clicked.connect(self.main_work.transformation_on_docx)
        self.win_2_but_docx.setStyleSheet(self.CSS_dict["win_2_but_docx"])
        self.win_2_but_docx.setText(LANGUAGE("con_docx"))
        # self.win_2_but_find.clicked.connect(self.save)
        self.main_work.window["window_2"].append(self.win_2_but_docx)
        self.main_work.window["second"].append(self.win_2_but_docx)

        # Создает кнопку преобразования из текста в mp3
        self.win_2_but_mp3 = QPushButton(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 1.8,
                  25 + self.size_window[1] // 1.2,
                  self.size_window[0] // 8.33,
                  self.size_window[1] // 20])
        self.win_2_but_mp3.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.win_2_but_mp3.clicked.connect(self.main_work.transformation_on_mp3)
        self.win_2_but_mp3.setStyleSheet(self.CSS_dict["win_2_but_mp3"])
        self.win_2_but_mp3.setText(LANGUAGE("con_mp3"))
        # self.win_2_but_find.clicked.connect(self.save)
        self.main_work.window["window_2"].append(self.win_2_but_mp3)
        self.main_work.window["second"].append(self.win_2_but_mp3)

    def window_3(self):  # Создает объекты переводчика
        self.main_work.window["window_3"] = list()

        # Создает первое поле ввода
        self.win_3_scr_1 = QTextEdit(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 19,
                  25 + self.size_window[1] // 5,
                  self.size_window[0] // 3.333,
                  self.size_window[1] // 1.5])
        self.win_3_scr_1.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.win_3_scr_1.setStyleSheet(self.CSS_dict["win_3_scr"])
        self.win_3_scr_1.setFont(self.font_text)
        self.main_work.window["window_3"].append(self.win_3_scr_1)
        self.main_work.window["second"].append(self.win_3_scr_1)

        # Создает второе поле ввода
        self.win_3_scr_2 = QTextEdit(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 2.5,
                  25 + self.size_window[1] // 5,
                  self.size_window[0] // 3.333,
                  self.size_window[1] // 1.5])
        self.win_3_scr_2.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.win_3_scr_2.setStyleSheet(self.CSS_dict["win_3_scr"])
        self.win_3_scr_2.setFont(self.font_text)
        self.main_work.window["window_3"].append(self.win_3_scr_2)
        self.main_work.window["second"].append(self.win_3_scr_2)

        # Создает название вкладки
        self.win_3_lan1 = QLabel(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 3.1,
                  25 + self.size_window[1] // 50,
                  self.size_window[0] // 5,
                  self.size_window[1] // 10])
        self.win_3_lan1.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.win_3_lan1.setStyleSheet(self.CSS_dict["win_3_lan1"])
        # self.win_3_lan1.setText("Привет")
        self.win_3_lan1.setText(LANGUAGE("nav_but_3"))
        self.win_3_lan1.setFont(self.font_lab)
        self.main_work.window["window_3"].append(self.win_3_lan1)
        self.main_work.window["second"].append(self.win_3_lan1)

        # Создает объект для изменения языка который отвечает за первое поле ввода
        self.win_3_com_box_lan1 = QComboBox(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 19,
                  25 + self.size_window[1] // 6.3,
                  self.size_window[0] // 9.6,
                  self.size_window[1] // 24])
        self.win_3_com_box_lan1.setGeometry(pos[0], pos[1], pos[2], pos[3])
        # self.set_com_box_theme.
        version = REQUEST.get_request("lan_val").split()
        for i in version:
            self.win_3_com_box_lan1.addItem(str(i))

        self.win_3_com_box_lan1.setCurrentText(REQUEST.get_request("lan1"))
        self.win_3_com_box_lan1.activated[str].connect(self.main_work.change_com_1)

        self.win_3_com_box_lan1.setStyleSheet(self.CSS_dict["win_3_com_box_lan"])
        self.main_work.window["window_3"].append(self.win_3_com_box_lan1)
        self.main_work.window["second"].append(self.win_3_com_box_lan1)

        # Создает объект для изменения языка который отвечает за второго поле ввода
        self.win_3_com_box_lan2 = QComboBox(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 2.5,
                  25 + self.size_window[1] // 6.3,
                  self.size_window[0] // 10,
                  self.size_window[1] // 24])
        self.win_3_com_box_lan2.setGeometry(pos[0], pos[1], pos[2], pos[3])
        # self.set_com_box_theme.
        version = REQUEST.get_request("lan_val").split()
        for i in version:
            self.win_3_com_box_lan2.addItem(str(i))

        self.win_3_com_box_lan2.setCurrentText(REQUEST.get_request("lan2"))
        self.win_3_com_box_lan2.activated[str].connect(self.main_work.change_com_2)

        self.win_3_com_box_lan2.setStyleSheet(self.CSS_dict["win_3_com_box_lan"])
        self.main_work.window["window_3"].append(self.win_3_com_box_lan2)
        self.main_work.window["second"].append(self.win_3_com_box_lan2)

        # Создает кнопку озвучиващию первый текст
        self.win_3_but_voice1 = QPushButton(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 6.5,
                  25 + self.size_window[1] // 6.3,
                  self.size_window[0] // 10,
                  self.size_window[1] // 24])
        self.win_3_but_voice1.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.win_3_but_voice1.clicked.connect(self.main_work.voice1)
        self.win_3_but_voice1.setStyleSheet(self.CSS_dict["win_3_but_voice"])
        self.win_3_but_voice1.setText(LANGUAGE("voice"))
        self.main_work.window["window_3"].append(self.win_3_but_voice1)
        self.main_work.window["second"].append(self.win_3_but_voice1)

        # Создает кнопку озвучиващию второй текст
        self.win_3_but_voice2 = QPushButton(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 2,
                  25 + self.size_window[1] // 6.3,
                  self.size_window[0] // 10,
                  self.size_window[1] // 24])
        self.win_3_but_voice2.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.win_3_but_voice2.clicked.connect(self.main_work.voice2)
        self.win_3_but_voice2.setStyleSheet(self.CSS_dict["win_3_but_voice"])
        self.win_3_but_voice2.setText(LANGUAGE("voice"))
        self.main_work.window["window_3"].append(self.win_3_but_voice2)
        self.main_work.window["second"].append(self.win_3_but_voice2)

        # Создает кнопку копирующию первый текст
        self.win_3_but_copy1 = QPushButton(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 3.95,
                  25 + self.size_window[1] // 6.3,
                  self.size_window[0] // 10,
                  self.size_window[1] // 24])
        self.win_3_but_copy1.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.win_3_but_copy1.clicked.connect(self.main_work.ccopy1)
        self.win_3_but_copy1.setStyleSheet(self.CSS_dict["win_3_but_copy"])
        self.win_3_but_copy1.setText(LANGUAGE("copy"))
        self.main_work.window["window_3"].append(self.win_3_but_copy1)
        self.main_work.window["second"].append(self.win_3_but_copy1)

        # Создает кнопку копирующию второй текст
        self.win_3_but_copy2 = QPushButton(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 1.6666,
                  25 + self.size_window[1] // 6.3,
                  self.size_window[0] // 10,
                  self.size_window[1] // 24])
        self.win_3_but_copy2.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.win_3_but_copy2.clicked.connect(self.main_work.ccopy2)
        self.win_3_but_copy2.setStyleSheet(self.CSS_dict["win_3_but_copy"])
        self.win_3_but_copy2.setText(LANGUAGE("copy"))
        self.main_work.window["window_3"].append(self.win_3_but_copy2)
        self.main_work.window["second"].append(self.win_3_but_copy2)

        # Создает кнопку переводяший первый текст на одном языке в второй на другом языке
        self.win_3_but_tran = QPushButton(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 1.6666,
                  25 + self.size_window[1] // 1.13,
                  self.size_window[0] // 10,
                  self.size_window[1] // 24])
        self.win_3_but_tran.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.win_3_but_tran.clicked.connect(self.main_work.translate)
        self.win_3_but_tran.setStyleSheet(self.CSS_dict["win_3_but_tran"])
        self.win_3_but_tran.setText(LANGUAGE("translate"))
        self.main_work.window["window_3"].append(self.win_3_but_tran)
        self.main_work.window["second"].append(self.win_3_but_tran)

    def setting_window(self):   # Создает объекты настроек
        self.main_work.window["setting"] = list()

        # Создает текст темы
        self.set_lab_theme = QLabel(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 10,
                  25 + self.size_window[1] // 10,
                  self.size_window[0] // 10,
                  self.size_window[1] // 12])
        self.set_lab_theme.setGeometry(pos[0], pos[1], pos[2], pos[3])
        # print(type(self.CSS_dict["set_lab_theme"]), self.CSS_dict["set_lab_theme"])
        self.set_lab_theme.setStyleSheet(self.CSS_dict["set_lab_theme"])
        self.set_lab_theme.setText("Тема")
        self.set_lab_theme.setFont(self.font_lab)
        self.main_work.window["setting"].append(self.set_lab_theme)
        self.main_work.window["second"].append(self.set_lab_theme)

        # Создает выбор тем
        self.set_com_box_theme = QComboBox(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 12,
                  25 + self.size_window[1] // 10 * 2,
                  self.size_window[0] // 10,
                  self.size_window[1] // 24])
        self.set_com_box_theme.setGeometry(pos[0], pos[1], pos[2], pos[3])
        # self.set_com_box_theme.
        version = len(REQUEST.get_full_request("name", "*", "text", table="appcolors")[0]) - 3
        for i in range(1, version + 1):
            self.set_com_box_theme.addItem(f"version{i}")

        self.set_com_box_theme.setCurrentText(REQUEST.get_request("version"))

        self.set_com_box_theme.setStyleSheet(self.CSS_dict["set_com_box_theme"])
        self.main_work.window["setting"].append(self.set_com_box_theme)
        self.main_work.window["second"].append(self.set_com_box_theme)

        # Создает кнопку сохраняющая изменения темы
        self.set_but_save = QPushButton(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 12,
                  25 + self.size_window[1] // 3.5,
                  self.size_window[0] // 10,
                  self.size_window[1] // 24])
        self.set_but_save.setGeometry(pos[0], pos[1], pos[2], pos[3])

        self.set_but_save.setStyleSheet(self.CSS_dict["set_but_save"])
        self.set_but_save.setText(LANGUAGE("but_save"))
        self.set_but_save.clicked.connect(self.save)
        self.main_work.window["setting"].append(self.set_but_save)
        self.main_work.window["second"].append(self.set_but_save)

        # Создает текст языка
        self.set_lab_cha_lan = QLabel(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 2.8,
                  25 + self.size_window[1] // 7,
                  self.size_window[0] // 6.66,
                  self.size_window[1] // 17.14])
        self.set_lab_cha_lan.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.set_lab_cha_lan.setText(LANGUAGE("language_name"))
        self.set_lab_cha_lan.setStyleSheet(self.CSS_dict["set_lab_cha_lan"])
        self.set_lab_cha_lan.setFont(self.font_lab)
        self.main_work.window["setting"].append(self.set_lab_cha_lan)
        self.main_work.window["second"].append(self.set_lab_cha_lan)

        # Создает кнопку смены языка
        self.set_but_cha_lan = QPushButton(self)
        pos = AD([self.size_window[0] // 4 + self.size_window[0] // 3,
                  25 + self.size_window[1] // 5,
                  self.size_window[0] // 6.25,
                  self.size_window[1] // 5.45])
        self.set_but_cha_lan.setGeometry(pos[0], pos[1], pos[2], pos[3])
        self.set_but_cha_lan.setIcon(QIcon("data/img/" + LANGUAGE("way_image")))
        size = AD([self.size_window[0] // 6.66,
                   self.size_window[1] // 6])
        self.set_but_cha_lan.setIconSize(QSize(size[0], size[1]))
        self.set_but_cha_lan.setStyleSheet(self.CSS_dict["set_but_cha_lan"])
        self.set_but_cha_lan.clicked.connect(self.main_work.change_lan)
        self.main_work.window["setting"].append(self.set_but_cha_lan)
        self.main_work.window["second"].append(self.set_but_cha_lan)

    def save(self):  # Обрабатывает нажатие кнопки сохранения
        # print(self.set_com_box_theme.currentText())
        self.main_work.save(self.set_com_box_theme.currentText())

    def roll_up(self):  # сворачивание экрана
        self.showMinimized()


def except_hook(cls, exception, traceback):  # если произойдет ошибка то Pyqt5 не будет замалчивать её
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("photo/game_icon.png"))  # пока не работает создает иконку приложения
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
