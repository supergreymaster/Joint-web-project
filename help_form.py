import sys
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename
from secondary_functions import Language

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTextEdit, QPushButton, QMessageBox

'''Появляется окно, в котором можно написать сообщение.
В итоге мы получим вопрос от пользователя на нашу почту,
А сам пользователь получит информационное письмо, что ответ поступит скоро'''
LANGUAGE = Language().request


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(LANGUAGE("support"))
        self.setGeometry(600, 300, 500, 570)
        self.initUi()

    def initUi(self):
        self.setStyleSheet("QWidget{background-color: #ffa500;}")

        self.email = QLineEdit(self)
        self.email.setFont(QFont("Times New Roman", 14))
        self.email.setPlaceholderText(LANGUAGE("in_em"))
        self.email.setFixedHeight(40)
        self.email.setStyleSheet("""
        QLineEdit{
            border: 1px solid #CCD6DD;
            background-color: #fff;
            border-radius: 15px;
        }
        """)
        self.email.resize(440, 20)
        self.email.move(30, 20)

        self.question = QTextEdit(self)
        self.question.setFont(QFont("Times New Roman", 14))
        self.question.setPlaceholderText(LANGUAGE("problem"))
        self.question.setStyleSheet("""
        QTextEdit{
            border: 1px solid #CCD6DD;
            background-color: #fff;
            border-radius: 15px;
        }""")
        self.question.resize(440, 440)
        self.question.move(30, 70)

        self.send_question = QPushButton(self)
        self.send_question.setFont(QFont("Times New Roman", 14))
        self.send_question.setText(LANGUAGE("send"))
        self.send_question.move(350, 520)
        self.send_question.clicked.connect(self.sending)
        self.send_question.setStyleSheet("""
        QPushButton:hover {
         background-color: #AAB6FB;
         border-style: outset;
        border-width: 2px;
        border-radius: 15px;
        border-color: black;
        padding: 4px;
    }
    QPushButton:!hover {
        background-color: #fff;
        border-style: outset;
        border-width: 2px;
        border-radius: 15px;
        border-color: black;
        padding: 4px;}
    
    QPushButton:pressed {
     background-color: rgb(0, 255, 0);
      }""")

    def sending(self):
        if self.email.text() == '':
            msg = QMessageBox(self)
            msg.setText(LANGUAGE("wrong3"))
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle(LANGUAGE("mistake"))
            msg.setFont(QFont("Times New Roman", 14))
            x = msg.exec_()
        elif self.question.toPlainText() == '':
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setText(LANGUAGE("wrong2"))
            msg.setWindowTitle(LANGUAGE("mistake"))
            msg.setFont(QFont("Times New Roman", 14))
            x = msg.exec_()
        else:
            try:
                addr_from = 'help.converter@yandex.ru'
                password = 'YandexLyceum2021'

                server = smtplib.SMTP('smtp.yandex.ru', 587)
                server.ehlo()
                server.starttls()
                server.login(addr_from, password)

                addr_to = self.email.text()

                msg = MIMEMultipart()
                msg['From'] = addr_from
                msg['To'] = addr_to
                msg['Subject'] = 'Подтверждение'
                body = 'Здравствуйте! \n' \
                       'Мы получили Ваше сообщение и ответим в течение 3-х рабочих дней.\n\n' \
                       'С уважением, команда разработчиков.'
                msg.attach(MIMEText(body, 'plain'))

                server.send_message(msg)
                msg = MIMEMultipart()
                msg['From'] = addr_from
                msg['To'] = addr_from
                msg['Subject'] = 'Новый вопрос'
                body = f'Получен новый вопрос.\nОтправитель: {addr_to}\n' \
                       f'Текст: "{self.question.toPlainText()}"'
                msg.attach(MIMEText(body, 'plain'))

                path_report = 'reports/report.json'
                with open(path_report, 'rb') as report:
                    part = MIMEApplication(
                        report.read(),
                        name=basename(path_report)
                    )
                    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(path_report)
                    msg.attach(part)
                server.send_message(msg)
                server.quit()
                msg = QMessageBox(self)
                msg.setText(LANGUAGE("send_request"))
                msg.setWindowTitle(LANGUAGE("title_success"))
                msg.setFont(QFont("Times New Roman", 14))
                x = msg.exec_()
                self.close()
            except Exception as e:
                msg = QMessageBox(self)
                msg.setText(LANGUAGE("wrong1"))
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle(LANGUAGE("mistake"))
                msg.setFont(QFont("Times New Roman", 14))
                x = msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    app.exit(app.exec_())
