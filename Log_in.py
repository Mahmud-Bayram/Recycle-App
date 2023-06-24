import sys
import sqlite3
from Main_page import App
from PyQt5 import QtWidgets
from PyQt5.uic.properties import QtCore
import time
import hashlib



class User_login(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.createLink()

    def createLink(self):
        self.link = sqlite3.connect("recycle.db")
        self.cursor = self.link.cursor()
        self.cursor.execute("Create Table If not exists UserInformations(Name TEXT, Lastname TEXT, Mail TEXT, Username TEXT, Password TEXT, SHA256 TEXT, Carbon INTEGER, Coin INTEGER)")
        self.cursor.execute("Create Table If not exists RecyclingQuotes(id INTEGER, Quotes TEXT)")
        self.cursor.execute("Create Table If not exists RecyclingMaterials(Plastic TEXT, Plastic_carbon_value INTEGER, Glass TEXT, Glass_carbon_value INTEGER, Paper TEXT, Paper_carbon_value INTEGER)")

        self.link.commit()

    def init_ui(self):
        self.usernameLabel = QtWidgets.QLabel("Username")
        self.username = QtWidgets.QLineEdit()
        self.passwordLabel = QtWidgets.QLabel("Password")
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login = QtWidgets.QPushButton("Login")
        self.register = QtWidgets.QPushButton("Register")
        self.writingArea = QtWidgets.QLabel()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.usernameLabel)
        v_box.addWidget(self.username)
        v_box.addWidget(self.passwordLabel)
        v_box.addWidget(self.password)
        v_box.addWidget(self.login)
        v_box.addWidget(self.register)
        v_box.addStretch()
        v_box.addWidget(self.writingArea)
        v_box.addStretch()

        self.setLayout(v_box)

        self.login.clicked.connect(self.Login)
        self.password.returnPressed.connect(self.loginWithEnter)
        self.register.clicked.connect(self.Register)

        width = 960
        height = 540
        appWidth = 165
        appHeight = 125
        self.setGeometry(width - appWidth, height - appHeight, appWidth * 2, appHeight * 2)

        self.setWindowTitle("Recycle App")

        self.show()

    def Login(self):
        if self.username.text() != "" and self.password.text() != "":
            self.cursor.execute("Select * From UserInformations Where Username = ? and Password = ?",
                                (self.username.text(), self.password.text()))
            user = self.cursor.fetchall()
            if len(user) != 0:
                self.close()
                time.sleep(1)
                self.userNotification = App(user[0][0])


            else:
                self.writingArea.setText("The username or password you entered is incorrect.")

        else:
            self.writingArea.setText("Please fill in the username and password section.")

    def loginWithEnter(self):
        if self.username.text() != "" and self.password.text() != "":
            self.cursor.execute("Select * From UserInformations Where Username = ? and Password = ?",
                                (self.username.text(), self.password.text()))
            user = self.cursor.fetchall()
            if len(user) != 0:
                self.close()
                time.sleep(1)
                self.userNotification = App(user[0][0])

            else:
                self.writingArea.setText("The username or password you entered is incorrect.")

        else:
            self.writingArea.setText("Please fill in the username and password section.")


    def Register(self):
        self.close()
        time.sleep(1)
        self.User_register = User_register()


class User_register(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.createLink()

    def createLink(self):
        self.link = sqlite3.connect("recycle.db")

        self.cursor = self.link.cursor()

        self.link.commit()

    def init_ui(self):
        self.nameLabel = QtWidgets.QLabel("Name")
        self.name = QtWidgets.QLineEdit()
        self.lastnameLabel = QtWidgets.QLabel("Lastname")
        self.lastname = QtWidgets.QLineEdit()
        self.mailLabel = QtWidgets.QLabel("Mail")
        self.mail = QtWidgets.QLineEdit()
        self.usernameLabel = QtWidgets.QLabel("Username")
        self.username = QtWidgets.QLineEdit()
        self.passwordLabel = QtWidgets.QLabel("Password")
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordVerificationLabel = QtWidgets.QLabel("Password Verification")
        self.passwordVerification = QtWidgets.QLineEdit()
        self.passwordVerification.setEchoMode(QtWidgets.QLineEdit.Password)
        self.register = QtWidgets.QPushButton("Register")
        self.login = QtWidgets.QPushButton("Login")
        self.back = QtWidgets.QPushButton("Back")
        self.writingArea = QtWidgets.QLabel()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.back)
        h_box.addStretch()


        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addStretch()
        v_box.addWidget(self.nameLabel)
        v_box.addWidget(self.name)
        v_box.addWidget(self.lastnameLabel)
        v_box.addWidget(self.lastname)
        v_box.addWidget(self.mailLabel)
        v_box.addWidget(self.mail)
        v_box.addWidget(self.usernameLabel)
        v_box.addWidget(self.username)
        v_box.addWidget(self.passwordLabel)
        v_box.addWidget(self.password)
        v_box.addWidget(self.passwordVerificationLabel)
        v_box.addWidget(self.passwordVerification)
        v_box.addStretch()
        v_box.addWidget(self.register)
        v_box.addStretch()
        v_box.addWidget(self.writingArea)
        v_box.addStretch()

        self.setLayout(v_box)

        self.register.clicked.connect(self.Register)
        self.back.clicked.connect(self.Back)

        width = 960
        height = 540
        appWidth = 160
        appHeight = 250
        self.setGeometry(width - appWidth, height - appHeight, appWidth * 2, appHeight * 2)

        self.setWindowTitle("Recycle App")

        self.show()

    def Register(self):
        name= self.name.text()
        lastname= self.lastname.text()
        mail= self.mail.text()
        username= self.username.text()
        password= self.password.text()
        hashedPassword = hashlib.sha256(self.password.text().encode("UTF-8")).hexdigest()

        if name != "" and lastname != "" and mail != "" and username != "" and password != "" and self.passwordVerification.text() != "":
            if self.password.text() != self.passwordVerification.text():
                self.writingArea.setText("The passwords you entered do not match.")
            else:
                self.cursor.execute("Insert into UserInformations Values(?, ?, ?, ?, ?, ?, 0, 0)", (name, lastname, mail, username, password, hashedPassword))
                self.link.commit()
                self.close()
                time.sleep(1)
                self.User_login = User_login()

        else:
            self.writingArea.setText("Please fill in all fields.")

    def Back(self):
        self.close()
        time.sleep(1)
        self.User_login = User_login()

app = QtWidgets.QApplication(sys.argv)
user_login = User_login()
sys.exit(app.exec_())


