import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin_desinger.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 400)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(300, 9, 100, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.but_find = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.but_find.setObjectName("but_find")
        self.verticalLayout.addWidget(self.but_find)
        self.request = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.request.setObjectName("request")
        self.verticalLayout.addWidget(self.request)
        self.warning_request = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.warning_request.setObjectName("warning_request")
        self.warning_request.addItem("")
        self.warning_request.addItem("")
        self.warning_request.addItem("")
        self.warning_request.addItem("")
        self.verticalLayout.addWidget(self.warning_request)
        self.lab_all_request = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lab_all_request.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_all_request.setObjectName("lab_all_request")
        self.verticalLayout.addWidget(self.lab_all_request)
        self.all_request = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.all_request.setObjectName("all_request")
        self.verticalLayout.addWidget(self.all_request)
        self.lab_debug = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lab_debug.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_debug.setObjectName("lab_debug")
        self.verticalLayout.addWidget(self.lab_debug)
        self.debug = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.debug.setObjectName("debug")
        self.verticalLayout.addWidget(self.debug)
        self.lab_info = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lab_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_info.setObjectName("lab_info")
        self.verticalLayout.addWidget(self.lab_info)
        self.info = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.info.setObjectName("info")
        self.verticalLayout.addWidget(self.info)
        self.lab_warning = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lab_warning.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_warning.setObjectName("lab_warning")
        self.verticalLayout.addWidget(self.lab_warning)
        self.warning = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.warning.setObjectName("warning")
        self.verticalLayout.addWidget(self.warning)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 281, 381))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line_find = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.line_find.setObjectName("line_find")
        self.verticalLayout_2.addWidget(self.line_find)
        self.textEdit_request = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit_request.setObjectName("textEdit_request")
        self.verticalLayout_2.addWidget(self.textEdit_request)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.but_find.setText(_translate("Form", "Поиск"))
        self.warning_request.setItemText(0, _translate("Form", "Все запросов"))
        self.warning_request.setItemText(1, _translate("Form", "Debug"))
        self.warning_request.setItemText(2, _translate("Form", "Info"))
        self.warning_request.setItemText(3, _translate("Form", "Warning"))
        self.lab_all_request.setText(_translate("Form", "Всего запросов"))
        self.lab_debug.setText(_translate("Form", "Debug"))
        self.lab_info.setText(_translate("Form", "Info"))
        self.lab_warning.setText(_translate("Form", "Warning"))
        self.line_find.setPlaceholderText(_translate("Form", "Введите запрос "))



# Отнаследуем наш класс от простейшего графического примитива QWidget
class Example(QWidget, Ui_Form):
    def __init__(self):
        # Надо не забыть вызвать инициализатор базового класса
        super().__init__()
        # В метод initUI() будем выносить всю настройку интерфейса,
        # чтобы не перегружать инициализатор
        self.setupUi(self)
        # self.initUI()

    def initUI(self):
        # Зададим размер и положение нашего виджета,
        self.setGeometry(300, 300, 450, 450)
        # А также его заголовок
        self.setWindowTitle('Вычисление выражений')

        self.clik = QPushButton("->", self)
        self.clik.move(150, 30)
        self.clik.resize(80, 30)
        self.clik.clicked.connect(self.work)

        self.text_1 = QLabel(self)
        self.text_1.setText("Первое число (целое):")
        self.text_1.move(10, 5)

        self.input_number1 = QLineEdit(self)
        self.input_number1.move(10, 25)
        self.input_number1.resize(100, 20)

        self.text_1 = QLabel(self)
        self.text_1.setText("Второе число (целое):")
        self.text_1.move(10, 65)

        self.input_number2 = QLineEdit(self)
        self.input_number2.move(10, 80)
        self.input_number2.resize(100, 20)

        self.text_1 = QLabel(self)
        self.text_1.setText("Сумма:")
        self.text_1.move(300, 15)

        self.output_sum = QLCDNumber(self)
        self.output_sum.move(340, 10)
        self.output_sum.resize(100, 30)
        self.output_sum.setEnabled(False)

        self.text_1 = QLabel(self)
        self.text_1.setText("Разность:")
        self.text_1.move(285, 45)

        self.output_difference = QLCDNumber(self)
        self.output_difference.move(340, 45)
        self.output_difference.resize(100, 30)
        self.output_difference.setEnabled(False)

        self.text_1 = QLabel(self)
        self.text_1.setText("Частное:")
        self.text_1.move(288, 115)

        self.output_quotient = QLCDNumber(self)
        self.output_quotient.move(340, 115)
        self.output_quotient.resize(100, 30)
        self.output_quotient.setEnabled(False)

        self.text_1 = QLabel(self)
        self.text_1.setText("Произведение:")
        self.text_1.move(258, 80)

        self.output_product = QLCDNumber(self)
        self.output_product.move(340, 80)
        self.output_product.resize(100, 30)
        self.output_product.setEnabled(False)

    def work(self):
        number1 = int(self.input_number1.text())
        number2 = int(self.input_number2.text())
        self.output_sum.display(number1 + number2)
        self.output_difference.display(number1 - number2)
        self.output_product.display(number1 * number2)
        if number2 != 0:
            self.output_quotient.display(float(f"{number1 / number2:.2f}"))
        else:
            self.output_quotient.display("Error")


if __name__ == '__main__':
    # Создадим класс приложения PyQT
    app = QApplication(sys.argv)
    # А теперь создадим и покажем пользователю экземпляр
    # нашего виджета класса Example
    ex = Example()
    ex.show()
    # Будем ждать, пока пользователь не завершил исполнение QApplication,
    # а потом завершим и нашу программу
    sys.exit(app.exec())
