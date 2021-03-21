import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QTextEdit
from PyQt5.QtGui import QPixmap, QFont, QIcon

from designer.secondary_functions import Request, Work_size_window

REQUEST = Request()


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        REQUEST.get_request("size_display")
        self.setWindowTitle(REQUEST.get_request("title_name"))


def except_hook(cls, exception, traceback):  # если произойдет ошибка то Pyqt5 не будет замалчивать её
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("photo/game_icon.png"))
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
