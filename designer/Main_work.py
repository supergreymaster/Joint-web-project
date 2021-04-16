import sys
import pyperclip
from designer.secondary_functions import pprint, Request
from PyQt5.QtWidgets import QFileDialog

REQUEST = Request()


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

    def void(self):  # Дополнительная функция которая скрывает все ошибачные функции
        pass

    def transformation_on_txt(self):  # Обрабатывает преобразование в txt
        pprint("Использовалась команда' ", "преобразовать в ", "txt")

    def transformation_on_docx(self):  # Обрабатывает преобразование в docx
        pprint("Использовалась команда' ", "преобразовать в ", "docx")

    def transformation_on_mp3(self):  # Обрабатывает преобразование в mp3
        pprint("Использовалась команда' ", "преобразовать в ", "mp3")

    def choose_file(self):  # Обрабатывает выбор файла
        fname = QFileDialog.getOpenFileName(
            self.window["self"], 'Выбрать картинку', '',
            'Картинка (*.jpg *.png);;Картинка (*.png);;Картинка (*.jpg);;Все файлы (*)')[0]
        self.window["fname"] = fname
        if not fname:
            pprint("Отменна операции ", "фотография не вставлена")
        else:
            pprint("Вставленна фотография' ", fname)

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

    def voice1(self):  # Обрабатывает озвучку первого текста
        pprint("Использовалась команда' ", "озвучить ", "первый текст")
        text = self.window["self"].win_3_scr_1.toPlainText()

    def voice2(self):  # Обрабатывает озвучку второго текста
        pprint("Использовалась команда' ", "озвучить ", "второй текст")
        text = self.window["self"].win_3_scr_2.toPlainText()

    def translate(self):  # Обрабатывает перевод текста
        pprint("Использовалась команда' ", "перевести текст ")
