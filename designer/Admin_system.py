import sys

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QRadioButton, QGridLayout, QLabel, QTextEdit
from PyQt5.QtWidgets import QCalendarWidget, QLCDNumber, QTextBrowser, QVBoxLayout, QComboBox, QMainWindow
from PyQt5.QtGui import QFont


class Admin_system(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(250, 250, 410, 410)
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QRect(300, 9, 100, 381))

        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.but_find = QPushButton(self.verticalLayoutWidget)
        self.but_find.setText("Поиск")
        self.verticalLayout.addWidget(self.but_find)

        self.request = QComboBox(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.request)

        self.warning_request = QComboBox(self.verticalLayoutWidget)
        self.warning_request.addItem("Все запросов")
        self.warning_request.addItem("Debug")
        self.warning_request.addItem("Warning")
        self.warning_request.addItem("Error")
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
        self.lab_info.setText("Info")
        self.lab_info.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.lab_info)

        self.info = QLCDNumber(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.info)

        self.lab_warning = QLabel(self.verticalLayoutWidget)
        self.lab_warning.setText("Warning")
        self.lab_warning.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.lab_warning)

        self.warning = QLCDNumber(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.warning)

        self.verticalLayoutWidget_2 = QWidget(self)
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 281, 381))

        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.line_find = QLineEdit(self.verticalLayoutWidget_2)
        self.line_find.setPlaceholderText("Введите запрос ")
        self.verticalLayout_2.addWidget(self.line_find)

        self.textEdit_request = QTextEdit(self.verticalLayoutWidget_2)
        self.verticalLayout_2.addWidget(self.textEdit_request)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def work():
    app = QApplication(sys.argv)
    ex = Admin_system()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
