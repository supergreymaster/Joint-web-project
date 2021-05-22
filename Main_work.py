import sys
import pyperclip
from secondary_functions import pprint, Request, Language
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from animation import Title_work
from Admin_system import Admin_system
from get_text import get_text
from translate_text import translate_text
from text_voice import play_text, save_text_as_mp3
from save_text import save_docx_text, save_txt_text
from help_form import Main

REQUEST = Request()
LANGUAGE = Language().request


class Main_work:  # Главная функция где происходит обработка всех событий
    def __init__(self):  # Создает словарь страниц и переменных
        self.window = {}

    def exit_program(self):  # Обрабатывает закрытие страницы
        sys.exit()

    def work1(self):  # Обрабатывает переход в первую страницу
        for i in self.window['second']:
            i.hide()
        for j in self.window["start"]:
            j.show()

    def work2(self):  # Обрабатывает переход в вторую страницу
        for i in self.window['second']:
            i.hide()
        for j in self.window["window_2"]:
            j.show()

    def work3(self):  # Обрабатывает переход в третью страницу
        for i in self.window['second']:
            i.hide()
        for j in self.window["window_3"]:
            j.show()

    def setting(self):  # Обрабатывает переход в настройки
        pprint("Использовалась команда' ", "войти в ", "настройки")
        for i in self.window['second']:
            i.hide()
        for j in self.window["setting"]:
            j.show()

    def save(self, version):  # Обрабатывает команду сохранение
        pprint("Использовалась команда' ", "сохранение")
        REQUEST.change_base("version", version)

    def change_lan(self):  # Обрабатывает изменение языка
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
        self.window["self"].update()

    def void(self):  # Дополнительная функция которая скрывает все ошибачные функции
        pass

    def transformation_on_txt(self):  # Обрабатывает преобразование в txt
        pprint("Использовалась команда' ", "преобразовать в ", "txt")
        filename, ok = QFileDialog.getSaveFileName(self.window["self"],
                                                   LANGUAGE("save_file"),
                                                   ".",
                                                   "All Files(*.txt)")

        if not ok:
            pprint("Операция преобразовать в txt", " отменена")
            return

        if filename.split("/")[-1].split(".")[-1] == "txt":
            pass
        else:
            filename = filename + ".txt"

        text = self.window["self"].win_2_tex_ret.toPlainText()

        save_txt_text(filename, text)
        msg = QMessageBox(self.window["self"])
        msg.setText("Функция выполнена успешно")
        msg.setWindowTitle("Успех")
        x = msg.exec_()
        pprint("команда ", "преобразовать в' ", "txt", " выполнена успешно")

    def transformation_on_docx(self):  # Обрабатывает преобразование в docx
        pprint("Использовалась команда' ", "преобразовать в ", "docx")
        filename, ok = QFileDialog.getSaveFileName(self.window["self"],
                                                   LANGUAGE("save_file"),
                                                   ".",
                                                   "All Files(*.docx)")

        if not ok:
            pprint("Операция преобразовать в docx отменена")
            return

        if filename.split("/")[-1].split(".")[-1] == "docx":
            pass
        else:
            filename = filename + ".docx"

        text = self.window["self"].win_2_tex_ret.toPlainText()
        save_docx_text(filename, text)

        msg = QMessageBox(self.window["self"])
        msg.setText(LANGUAGE("success"))
        msg.setWindowTitle(LANGUAGE("title_success"))
        x = msg.exec_()
        pprint("команда ", "преобразовать в' ", "docx", " выполнена успешно")

    def transformation_on_mp3(self):  # Обрабатывает преобразование в mp3
        pprint("Использовалась команда' ", "преобразовать в ", "mp3")
        filename, ok = QFileDialog.getSaveFileName(self.window["self"],
                                                   LANGUAGE("save_file"),
                                                   ".",
                                                   "All Files(*.mp3)")
        if not ok:
            pprint("Операция преобразовать в mp3 отменена")
            return
        if filename.split("/")[-1].split(".")[-1] == "mp3":
            pass
        else:
            filename = filename + ".mp3"

        text = self.window["self"].win_2_tex_ret.toPlainText()
        if not text.strip():
            pprint("Операция преобразовать в mp3 отменена")
            return
        save_text_as_mp3(text, filename, REQUEST.get_request("language")[:-1])

        msg = QMessageBox(self.window["self"])
        msg.setText(LANGUAGE("success"))
        msg.setWindowTitle(LANGUAGE("title_success"))
        x = msg.exec_()
        pprint("команда ", "преобразовать в' ", "mp3", " выполнена успешно")

    def choose_file(self):  # Обрабатывает выбор файла
        fname = QFileDialog.getOpenFileName(
            self.window["self"], LANGUAGE("choose_file"), '',
            f'{LANGUAGE("image")} (*.jpg *.png);;{LANGUAGE("image")} (*.png);;'
            f'{LANGUAGE("image")} (*.jpg);;{LANGUAGE("all_file")} (*)')[0]
        self.window["fname"] = fname
        if not fname:
            pprint("Отменна операции ", "фотография не вставлена")
        else:
            pprint("Вставленна фотография' ", fname)
            text = get_text(fname)
            if type(text) is str:
                self.window["self"].win_2_tex_ret.setText(text)
            else:
                pprint("Нет связи с функцией get_text", warning="warning")
                self.window["self"].win_2_tex_ret.setText(LANGUAGE("error_prer"))

    def ccopy(self):
        pprint("Использовалась команда' ", "копировать ", "текст")
        pyperclip.copy(self.window["self"].win_2_tex_ret.toPlainText())
        pprint("Скопирован текст ", self.window["self"].win_2_tex_ret.toPlainText())

    def ccopy1(self):  # Обрабатывает копирование первого текста
        pprint("Использовалась команда' ", "копировать ", "первый текст")
        pyperclip.copy(self.window["self"].win_3_scr_1.toPlainText())
        pprint("Скопирован текст ", self.window["self"].win_3_scr_1.toPlainText())

    def ccopy2(self):  # Обрабатывает копирование второго текста
        pprint("Использовалась команда' ", "копировать ", "второй текст")
        pyperclip.copy(self.window["self"].win_3_scr_2.toPlainText())
        pprint("Скопирован текст ", self.window["self"].win_3_scr_2.toPlainText())

    def change_com_1(self):  # Обрабатывает изменение языка первого текста
        pprint("Использовалась команда' ", "изменить первый язык ")
        REQUEST.change_base("lan1", self.window["self"].sender().currentText())

    def change_com_2(self):  # Обрабатывает изменение языка второго текста
        pprint("Использовалась команда' ", "изменить второй язык ")
        REQUEST.change_base("lan2", self.window["self"].sender().currentText())

    def voice(self):
        pprint("Использовалась команда' ", "озвучить текст")
        if not self.warning():
            pprint("Отменена команда' ", "озвучить текст")
            return
        text = self.window["self"].win_2_tex_ret.toPlainText()
        lan = REQUEST.get_request("language")[:-1]
        if not lan:
            lan = "en"
        play_text(text, lan)

    def voice1(self):  # Обрабатывает озвучку первого текста
        pprint("Использовалась команда' ", "озвучить ", "первый текст")
        if not self.warning():
            pprint("Отменена команда' ", "озвучить ", "первый текст")
            return
        text = self.window["self"].win_3_scr_1.toPlainText()
        lan = REQUEST.get_request("lan1")
        if not lan:
            lan = "en"
        play_text(text, lan)

    def voice2(self):  # Обрабатывает озвучку второго текста
        pprint("Использовалась команда' ", "озвучить ", "второй текст")
        if not self.warning():
            pprint("Отменена команда' ", "озвучить ", "второй текст")
            return
        text = self.window["self"].win_3_scr_2.toPlainText()
        lan = REQUEST.get_request("lan2")
        if not lan:
            lan = "en"
        play_text(text, lan)

    def translate(self):  # Обрабатывает перевод текста
        pprint("Использовалась команда' ", "перевести текст ")
        text = self.window["self"].win_3_scr_1.toPlainText()

        try:
            tmp = REQUEST.get_request("lan2")
            if not tmp:
                tmp = "en"
            text_lan, lan1, lan2 = translate_text(text, tmp)
            # print(lan1, lan2)
            REQUEST.change_base("lan1", lan1)
            REQUEST.change_base("lan2", lan2)
            self.window["self"].win_3_com_box_lan1.setCurrentText(REQUEST.get_request("lan1"))
        except KeyError:
            text_lan = LANGUAGE("error_tran")
        self.window["self"].win_3_scr_2.setText(text_lan)

    def transition_admin(self):
        pprint("Использовалась команда' ", "войти в ", "админскую систему")
        if REQUEST.get_request("user") == "0":
            tmp = Title_work()
            if tmp:
                return
        self.admin_sys()

    def warning(self):  # обрабатывает предупреждение пользователя
        msg = QMessageBox.question(self.window["self"], LANGUAGE("warn"),
                                   LANGUAGE("warn1"),
                                   QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)
        if msg == QMessageBox.Ok:
            return True
        elif msg == QMessageBox.Cancel:
            return False
        else:
            return False

    def admin_sys(self):
        pprint("Использовалась команда' ", "ввойти в ", "админскую систему")
        self.window["self"].w2 = Admin_system()
        self.window["self"].w2.show()

    def feedback(self):
        pprint("Использовалась команда' ", "обратной связи")
        self.window["self"].w3 = Main()
        self.window["self"].w3.show()
