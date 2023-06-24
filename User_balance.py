import sqlite3
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class User_balance(QtWidgets.QWidget):
    def __init__(self, SHA256Line):
        super().__init__()

        self.SHA256Line = SHA256Line

        self.createLink()

        self.init_ui()

    def createLink(self):
        self.link = sqlite3.connect("recycle.db")
        self.cursor = self.link.cursor()

        self.link.commit()

    def init_ui(self):
        self.arananCarbon = QtWidgets.QLabel("Carbon:")
        self.arananCarbonLine = QtWidgets.QLabel()
        self.arananCoin = QtWidgets.QLabel("Coin:")
        self.arananCoinLine = QtWidgets.QLabel()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.arananCarbon)
        v_box.addWidget(self.arananCarbonLine)
        v_box.addWidget(self.arananCoin)
        v_box.addWidget(self.arananCoinLine)

        self.setLayout(v_box)
        self.cursor.execute("Select Carbon, Coin from UserInformations where SHA256 = ?",
                            (self.SHA256Line,))
        kullanici = self.cursor.fetchall()
        carbon = kullanici[0][1]
        coin = kullanici[0][0]
        self.arananCoinLine.setText(str(carbon))
        self.arananCarbonLine.setText(str(coin))

        width = 960
        height = 540
        appWidth = 100
        appHeight = 75
        self.setGeometry(width - appWidth, height - appHeight, appWidth * 2, appHeight * 2)

        self.setWindowTitle("Geri Dönüşüm Uygulaması")

        self.show()
