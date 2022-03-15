from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(1600, 1900)
        self.label1 = QLabel("Enter your host IP:", self)
        self.text = QLineEdit(self)
        self.text.move(10, 30)
        self.label3 = QLabel("enter your API key", self)
        self.text3 = QLineEdit(self)
        self.text3.move(10, 60)
        self.label3.move(150, 60)
        self.label4 = QLabel("enter your ip", self)
        self.label4.move(150, 90)
        self.text4 = QLineEdit(self)
        self.text4.move(10, 90)

        self.label2 = QLabel("Answer:", self)
        self.label2.move(10, 120)
        self.button = QPushButton("Send", self)
        self.button.move(10, 150)

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        hostname = self.text.text()
        API_key = self.text3.text()
        ip = self.text4.text()

        if hostname == "" or API_key == "" or ip == "":
            QMessageBox.about(self, "Error", "Please fill the fields")
        else:
            res = self.__query(hostname, API_key, ip)
            if res:
                self.label2.setText(str(res))
                self.label2.adjustSize()
                self.show()

    def __query(self, hostname, API_key, ip):
        url = "http://" + hostname +"/ip/" + ip + "?key=" + API_key
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()