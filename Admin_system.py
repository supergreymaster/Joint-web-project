import sys
import json

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QRadioButton, QGridLayout, QLabel, QTextEdit
from PyQt5.QtWidgets import QCalendarWidget, QLCDNumber, QTextBrowser, QVBoxLayout, QComboBox, QMainWindow
from PyQt5.QtGui import QFont


class Admin_system(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.save = list()

        self.setGeometry(250, 250, 410, 410)
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QRect(300, 9, 100, 381))

        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.but_find = QPushButton(self.verticalLayoutWidget)
        self.but_find.setText("Поиск")
        self.but_find.clicked.connect(self.work)
        self.verticalLayout.addWidget(self.but_find)

        self.request = QComboBox(self.verticalLayoutWidget)
        self.request.addItem("Все запросы")
        with open("reports/report.json", encoding="utf-8") as file:
            test = json.load(file)
        for i in test["default"]:
            self.request.addItem(i)

        self.verticalLayout.addWidget(self.request)

        self.warning_request = QComboBox(self.verticalLayoutWidget)
        self.warning_request.addItem("Все ошибки")
        self.warning_request.addItem("Debug")
        self.warning_request.addItem("Warning")
        self.warning_request.addItem("Error")
        self.warning_request.activated[str].connect(self.check)
        self.verticalLayout.addWidget(self.warning_request)

        self.lab_all_request = QLabel(self.verticalLayoutWidget)
        self.lab_all_request.setAlignment(Qt.AlignCenter)
        self.lab_all_request.setText("Всего запросов")
        self.verticalLayout.addWidget(self.lab_all_request)

        self.all_request = QLCDNumber(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.all_request)

        self.lab_debug = QLabel(self.verticalLayoutWidget)
        self.lab_debug.setAlignment(Qt.AlignCenter)
        self.lab_debug.setText("Debug")
        self.verticalLayout.addWidget(self.lab_debug)

        self.debug = QLCDNumber(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.debug)

        self.lab_info = QLabel(self.verticalLayoutWidget)
        self.lab_info.setText("Warning")
        self.lab_info.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.lab_info)

        self.warning = QLCDNumber(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.warning)

        self.lab_warning = QLabel(self.verticalLayoutWidget)
        self.lab_warning.setText("Error")
        self.lab_warning.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.lab_warning)

        self.error = QLCDNumber(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.error)

        self.verticalLayoutWidget_2 = QWidget(self)
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 281, 381))

        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.line_find = QLineEdit(self.verticalLayoutWidget_2)
        self.line_find.setPlaceholderText("Введите запрос ")
        self.verticalLayout_2.addWidget(self.line_find)

        self.textEdit_request = QTextEdit(self.verticalLayoutWidget_2)
        self.verticalLayout_2.addWidget(self.textEdit_request)

        self.mistake()

    def work(self):
        self.mistake()
        self.textEdit_request.setText("")
        self.save = list()
        name = ""
        if self.warning_request.currentText() == "Все ошибки":
            if self.request.currentText() == "Все запросы":
                self.rec_all()
            else:
                self.rec_default(self.request.currentText())
        elif self.warning_request.currentText() == "Debug":
            if self.request.currentText() == "Все запросы":
                self.rec_default_all()
            else:
                self.rec_default(self.request.currentText())
        elif self.warning_request.currentText() == "Warning":
            self.rec_warning()
        elif self.warning_request.currentText() == "Error":
            self.rec_error()
        for i in self.save:
            if not self.line_find.text():
                self.textEdit_request.append(i)
            else:
                if self.line_find.text() in i:
                    self.textEdit_request.append(i)

    def mistake(self):
        with open("reports/report.json", encoding="utf-8") as file:
            test = json.load(file)

        all_request = len(test["all"])
        warning_request = len(test["warning"])
        error_request = len(test["error"])
        c = 0
        for i in test["default"]:
            for j in test["default"][i]:
                c += 1
        self.all_request.display(all_request)
        self.warning.display(warning_request)
        self.error.display(error_request)
        self.debug.display(c)

    def rec_all(self):
        with open("reports/report.json", encoding="utf-8") as file:
            test = json.load(file)

        if not test["all"]:
            self.textEdit_request.append("Ошибок нет")

        c = 1
        for i in test["all"]:
            self.save.append(f'{c}. ' + str(i))
            c += 1

    def rec_warning(self):
        with open("reports/report.json", encoding="utf-8") as file:
            test = json.load(file)

        if not test["warning"]:
            self.textEdit_request.append("Ошибок нет")

        c = 1
        for i in test["warning"]:
            self.save.append(f'{c}. ' + str(i))
            c += 1

    def rec_error(self):
        with open("reports/report.json", encoding="utf-8") as file:
            test = json.load(file)

        if not test["error"]:
            self.textEdit_request.append("Ошибок нет")

        c = 1
        for i in test["error"]:
            self.save.append(f'{c}. ' + str(i))
            c += 1

    def rec_default_all(self):
        with open("reports/report.json", encoding="utf-8") as file:
            test = json.load(file)

        if not test["default"]:
            self.textEdit_request.append("Ошибок нет")

        c = 1
        for i in test["default"]:
            for j in test["default"][i]:
                self.save.append(f"{c}. " + j)
                c += 1

    def rec_default(self, text):
        with open("reports/report.json", encoding="utf-8") as file:
            test = json.load(file)

        for i in test["default"]:
            if i == text:
                if not test["default"]:
                    self.save.append("Ошибок нет")
                c = 1
                for j in test["default"][i]:
                    self.save.append(f"{c}. " + j)
                    c += 1

    def check(self):
        if self.warning_request.currentText() == "Все ошибки":
            self.request.clear()
            self.request.addItem("Все запросы")
            with open("reports/report.json", encoding="utf-8") as file:
                test = json.load(file)
            for i in test["default"]:
                self.request.addItem(i)
        elif self.warning_request.currentText() == "Debug":
            self.request.clear()
            self.request.addItem("Все запросы")
            with open("reports/report.json", encoding="utf-8") as file:
                test = json.load(file)
            for i in test["default"]:
                self.request.addItem(i)
        elif self.warning_request.currentText() == "Warning":
            self.request.clear()
            self.request.addItem("Все запросы")
        elif self.warning_request.currentText() == "Error":
            self.request.clear()
            self.request.addItem("Все запросы")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def admin_system():
    app = QApplication(sys.argv)
    ex = Admin_system()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Admin_system()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
