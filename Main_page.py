import os
import time
import uuid

import cv2
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
import sqlite3
from User_balance import User_balance


id = 0
coin = 0


class App(QtWidgets.QMainWindow):
    def __init__(self, name):
        super().__init__()
        width = 960
        height = 540
        appWidth = 450
        appHeight = 300
        self.setGeometry(width-appWidth, height-appHeight, appWidth*2, appHeight*2)
        self.setWindowTitle("Recycle App")
        self.tab_app = Tabs(self, name)

        self.setCentralWidget(self.tab_app)

        self.show()


class Tabs(QtWidgets.QWidget):
    def __init__(self, basis, name):
        self.createLink()

        self.name = name

        super(QtWidgets.QWidget, self).__init__(basis)
        self.interface = QtWidgets.QVBoxLayout(self)
        self.interface2 = QtWidgets.QHBoxLayout(self)

        self.tabs = QtWidgets.QTabWidget()
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tab3 = QtWidgets.QWidget()
        self.tabs.resize(300, 200)

        self.tabs.addTab(self.tab1, "Main Page")
        self.tabs.addTab(self.tab2, "Recycle")
        self.tabs.addTab(self.tab3, "Informations")

        # TAB - 1
        self.image_tab1_1 = QtWidgets.QLabel(self.tab1)
        self.image_tab1_1.setPixmap(QtGui.QPixmap("Application_images/recycle1.jpg"))
        self.image_tab1_2 = QtWidgets.QLabel(self.tab1)
        self.image_tab1_2.setPixmap(QtGui.QPixmap("Application_images/recycle2.png"))
        self.image_tab1_3 = QtWidgets.QLabel(self.tab1)
        self.image_tab1_3.setPixmap(QtGui.QPixmap("Application_images/recycle3.jpg"))
        self.writingArea_tab1 = QtWidgets.QLabel(self.tab1)
        self.writingArea_tab1.move(100, 100)
        self.writingArea_tab1.setWindowIcon(QIcon("img.png"))
        self.changeButton = QtWidgets.QPushButton("Change")

        self.tab1.interface = QtWidgets.QVBoxLayout(self)
        self.tab1.interface2 = QtWidgets.QHBoxLayout(self)

        self.tab1.interface2.addWidget(self.image_tab1_1)
        self.tab1.interface2.addStretch()
        self.tab1.interface2.addWidget(self.image_tab1_2)
        self.tab1.interface2.addStretch()
        self.tab1.interface2.addWidget(self.image_tab1_3)

        self.tab1.interface.addLayout(self.tab1.interface2)
        self.tab1.interface.addSpacing(100)
        self.tab1.interface.addWidget(self.writingArea_tab1)
        self.tab1.interface.addSpacing(50)
        self.tab1.interface.addWidget(self.changeButton)
        self.tab1.interface.addStretch()
        self.cursor.execute("Select Quotes From RecyclingQuotes where id = ?", (id,))
        quote = self.cursor.fetchall()
        self.writingArea_tab1.setText(quote[0][0])

        self.changeButton.clicked.connect(self.Change)


        self.tab1.setLayout(self.tab1.interface)


        # TAB - 2
        self.image_tab2_1 = QtWidgets.QLabel(self.tab2)
        self.image_tab2_1.setPixmap(QtGui.QPixmap("Application_images/plastic.jpg"))
        self.image_tab2_2 = QtWidgets.QLabel(self.tab2)
        self.image_tab2_2.setPixmap(QtGui.QPixmap("Application_images/glass.jpg"))
        self.image_tab2_3 = QtWidgets.QLabel(self.tab2)
        self.image_tab2_3.setPixmap(QtGui.QPixmap("Application_images/paper.jpg"))
        self.writingArea_tab2_1 = QtWidgets.QLabel()
        self.writingArea_tab2_1.setText("""As plastic:
                      0,5L Bottle
                      0,33L Bottle
                      1,5L Bottle
                      2,5L Bottle
you can convert.""")
        self.writingArea_tab2_2 = QtWidgets.QLabel()
        self.writingArea_tab2_2.setText("""As glass:
                      200ml Glass Bottle
                      500ml Glass Bottle
                      1L Glass Bottle
you can convert.""")
        self.writingArea_tab2_3 = QtWidgets.QLabel()
        self.writingArea_tab2_3.setText("""As paper:
                      Paper
                      Magazine
                      Book
you can convert.""")
        self.recycleButton = QtWidgets.QPushButton("Recycle")
        self.arrangement_tab2_1 = QtWidgets.QLineEdit(self.tab2)
        self.arrangement_tab2_1.setPlaceholderText("Product Name")
        self.amount_1 = QtWidgets.QLineEdit()
        self.amount_1.setValidator(QtGui.QIntValidator(0, 100000000, self))
        self.amount_1.setPlaceholderText("Product Amount")
        self.amount_1.setToolTip("If you do not enter any value, 1 unit will be converted from the product whose name you entered.")
        self.arrangement_tab2_2 = QtWidgets.QLineEdit(self.tab2)
        self.arrangement_tab2_2.setPlaceholderText("Product Name")
        self.amount_2 = QtWidgets.QLineEdit()
        self.amount_2.setValidator(QtGui.QIntValidator(0, 100000000, self))
        self.amount_2.setPlaceholderText("Product Amount")
        self.amount_2.setToolTip("If you do not enter any value, 1 unit will be converted from the product whose name you entered.")
        self.arrangement_tab2_1.setPlaceholderText("Product Name")
        self.arrangement_tab2_3 = QtWidgets.QLineEdit(self.tab2)
        self.arrangement_tab2_3.setPlaceholderText("Product Name")
        self.amount_3 = QtWidgets.QLineEdit()
        self.amount_3.setValidator(QtGui.QIntValidator(0, 100000000, self))
        self.amount_3.setPlaceholderText("Product Amount")
        self.amount_3.setToolTip("If you do not enter any value, 1 unit will be converted from the product whose name you entered.")


        self.tab2.interfaceV1 = QtWidgets.QVBoxLayout(self)
        self.tab2.interfaceV2 = QtWidgets.QVBoxLayout(self)
        self.tab2.interfaceV3 = QtWidgets.QVBoxLayout(self)
        self.tab2.interfaceH = QtWidgets.QHBoxLayout(self)

        self.tab2.interfaceV1.addWidget(self.image_tab2_1)
        self.tab2.interfaceV1.addWidget(self.arrangement_tab2_1)
        self.tab2.interfaceV1.addWidget(self.amount_1)
        self.tab2.interfaceV1.addWidget(self.writingArea_tab2_1)
        self.tab2.interfaceV2.addWidget(self.image_tab2_2)
        self.tab2.interfaceV2.addWidget(self.arrangement_tab2_2)
        self.tab2.interfaceV2.addWidget(self.amount_2)
        self.tab2.interfaceV2.addWidget(self.writingArea_tab2_2)
        self.tab2.interfaceV2.addWidget(self.recycleButton)
        self.tab2.interfaceV3.addWidget(self.image_tab2_3)
        self.tab2.interfaceV3.addWidget(self.arrangement_tab2_3)
        self.tab2.interfaceV3.addWidget(self.amount_3)
        self.tab2.interfaceV3.addWidget(self.writingArea_tab2_3)

        self.tab2.interfaceH.addLayout(self.tab2.interfaceV1)
        self.tab2.interfaceH.addStretch()
        self.tab2.interfaceH.addLayout(self.tab2.interfaceV2)
        self.tab2.interfaceH.addStretch()
        self.tab2.interfaceH.addLayout(self.tab2.interfaceV3)

        self.recycleButton.clicked.connect(self.Recycle)

        self.tab2.setLayout(self.tab2.interfaceH)


        # TAB - 3
        self.searchSHA256 = QtWidgets.QLineEdit()
        self.searchSHA256.setPlaceholderText("SHA256 Address")
        self.searchSHA256.setToolTip("By entering the SHA256 address, you can find out the coin and carbon amount of the person you are looking for.")
        self.searchButton = QtWidgets.QPushButton("User Search")
        self.updateButton = QtWidgets.QPushButton(self.tab3)
        self.updateButton.setText("Update")
        self.updateButton.move(200, 465)
        self.deleteButton = QtWidgets.QPushButton(self.tab3)
        self.deleteButton.setText("Delete")
        self.deleteButton.move(550, 465)
        self.coinTransfer = QtWidgets.QPushButton(self.tab3)
        self.coinTransfer.setText("Coin Send")
        self.coinTransfer.move(120, 400)
        self.writingArea_tab3 = QtWidgets.QLabel(self.tab3)
        self.writingArea_tab3_2 = QtWidgets.QLabel(self.tab3)
        self.firstname = QtWidgets.QLabel(self.tab3)
        self.firstname.setText("Name:")
        self.firstnameLine = QtWidgets.QLineEdit(self.tab3)
        self.lastname = QtWidgets.QLabel(self.tab3)
        self.lastname.setText("Lastname:")
        self.lastnameLine = QtWidgets.QLineEdit(self.tab3)
        self.mail = QtWidgets.QLabel(self.tab3)
        self.mail.setText("Mail:")
        self.mailLine = QtWidgets.QLineEdit(self.tab3)
        self.username = QtWidgets.QLabel(self.tab3)
        self.username.setText("Username:")
        self.usernameLine = QtWidgets.QLineEdit(self.tab3)
        self.SHA256 = QtWidgets.QLabel(self.tab3)
        self.SHA256.setText("SHA256 Address:")
        self.SHA256Line = QtWidgets.QLabel(self.tab3)
        self.carbon = QtWidgets.QLabel(self.tab3)
        self.carbon.setText("Carbon:")
        self.carbonLine = QtWidgets.QLabel(self.tab3)
        self.coin = QtWidgets.QLabel(self.tab3)
        self.coin.setText("Recycle Coin:")
        self.coinLine = QtWidgets.QLabel(self.tab3)

        self.cursor.execute("Select Name, Lastname, Mail, Username, SHA256, Carbon, Coin From UserInformations Where Name = ?",
                            (self.name,))
        user = self.cursor.fetchall()


        name = str(user[0][0])
        lastname = str(user[0][1])
        mail = str(user[0][2])
        username = str(user[0][3])
        SHA256 = str(user[0][4])
        carbon = str(user[0][5])
        carbonInt = int(carbon)
        coin = 0

        if carbonInt > 99999999:
            coin = int(carbonInt / 100000000)

        if coin > 100000000:
            self.writingArea_tab3.setText("You can't have more than 100000000 Recycle Coins.")
            coin = 100000000
            carbonInt = 10000000000000000

        self.cursor.execute("Update UserInformations set Coin = ?, Carbon = ? where Name = ?",
                            (coin, carbonInt, self.name))
        self.link.commit()

        self.firstnameLine.setText(name)
        self.lastnameLine.setText(lastname)
        self.mailLine.setText(mail)
        self.usernameLine.setText(username)
        self.SHA256Line.setText(SHA256)
        self.carbonLine.setText(carbon)
        self.coinLine.setText(str(coin))

        self.tab3.interface = QtWidgets.QVBoxLayout(self)
        self.tab3.interfaceH = QtWidgets.QHBoxLayout(self)
        self.tab3.interfaceV2 = QtWidgets.QVBoxLayout(self)

        self.tab3.interfaceH.addWidget(self.searchSHA256)
        self.tab3.interfaceH.addWidget(self.searchButton)

        self.tab3.interfaceV2.addLayout(self.tab3.interfaceH)
        self.tab3.interfaceV2.addSpacing(10)
        self.tab3.interfaceV2.addWidget(self.writingArea_tab3_2)
        self.tab3.interfaceV2.addSpacing(10)

        self.tab3.interface.addLayout(self.tab3.interfaceV2)
        self.tab3.interface.addSpacing(10)
        self.tab3.interface.addWidget(self.firstname)
        self.tab3.interface.addWidget(self.firstnameLine)
        self.tab3.interface.addWidget(self.lastname)
        self.tab3.interface.addWidget(self.lastnameLine)
        self.tab3.interface.addWidget(self.mail)
        self.tab3.interface.addWidget(self.mailLine)
        self.tab3.interface.addWidget(self.username)
        self.tab3.interface.addWidget(self.usernameLine)
        self.tab3.interface.addWidget(self.SHA256)
        self.tab3.interface.addWidget(self.SHA256Line)
        self.tab3.interface.addWidget(self.carbon)
        self.tab3.interface.addWidget(self.carbonLine)
        self.tab3.interface.addWidget(self.coin)
        self.tab3.interface.addWidget(self.coinLine)

        self.tab3.interface.addStretch()
        self.tab3.interface.addWidget(self.writingArea_tab3)

        self.updateButton.clicked.connect(self.update)
        self.deleteButton.clicked.connect(self.delete)
        self.coinTransfer.clicked.connect(self.CoinTransfer)
        self.searchButton.clicked.connect(self.userSearch)

        self.tab3.setLayout(self.tab3.interface)


        self.interface.addWidget(self.tabs)
        self.setLayout(self.interface)

    def createLink(self):
        self.link = sqlite3.connect("recycle.db")
        self.cursor = self.link.cursor()

        self.link.commit()




# Tab - 1 Functions

    def Change(self):
        global id
        self.cursor.execute("Select Quotes From RecyclingQuotes where id = ?", (id,))
        quote = self.cursor.fetchall()
        self.writingArea_tab1.setText(quote[0][0])
        if True:
            id += 1
            if id == 20:
                id = 0


# Tab - 2 Functions

    def Recycle(self):
        self.cursor.execute("Select Carbon from UserInformations where SHA256 = ?",(self.SHA256Line.text(),))
        carbon = self.cursor.fetchall()
        carbonInt = int(carbon[0][0])

        self.cursor.execute("Select Plastic_carbon_value from RecyclingMaterials where Plastic = ?",(self.arrangement_tab2_1.text(),))
        plastic = self.cursor.fetchall()
        self.cursor.execute("Select Glass_carbon_value from RecyclingMaterials where Glass = ?",(self.arrangement_tab2_2.text(),))
        glass = self.cursor.fetchall()
        self.cursor.execute("Select Paper_carbon_value from RecyclingMaterials where Paper = ?",(self.arrangement_tab2_3.text(),))
        paper = self.cursor.fetchall()



        # This section is for gain carbon using image processing. This section will active when weight files download.

        # IMAGES_PATH = "C:\\Users\\MAHMUT\\PycharmProjects\\RecycleDeneme\\Images"
        #
        # cap = cv2.VideoCapture(0)
        # print('Collecting images')
        # time.sleep(5)
        # for imgnum in range(3):
        #     print('Collecting image {}'.format(imgnum))
        #     time.sleep(2)
        #     ret, frame = cap.read()
        #     imgname = os.path.join(IMAGES_PATH, str(imgnum) + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        #     cv2.imwrite(imgname, frame)
        #     cv2.imshow('frame', frame)
        #
        #
        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         break
        # cap.release()
        # cv2.destroyAllWindows()



        if len(plastic) > 0:
            amount = 1
            if self.amount_1.text() != "":
                amount = int(self.amount_1.text())
            carbonInt += (amount * int(plastic[0][0]))
            coin = int(carbonInt / 100000000)

            if coin > 99999999:
                coin = 100000000
                carbonInt = coin * 100000000

            self.cursor.execute("Update UserInformations set Carbon = ?, Coin = ? where Name = ?", (carbonInt, coin, self.name))
            self.link.commit()

            self.carbonLine.setText(str(carbonInt))
            self.coinLine.setText(str(coin))
            self.arrangement_tab2_1.setText("")
            self.amount_1.setText("")

        if len(glass) > 0:
            amount = 1
            if self.amount_2.text() != "":
                amount = int(self.amount_2.text())
            carbonInt += (amount * int(glass[0][0]))
            coin = int(carbonInt / 100000000)

            if coin > 99999999:
                coin = 100000000
                carbonInt = coin * 100000000

            self.cursor.execute("Update UserInformations set Carbon = ?, Coin = ? where Name = ?",
                                (carbonInt, coin, self.name))
            self.link.commit()

            self.carbonLine.setText(str(carbonInt))
            self.coinLine.setText(str(coin))

            self.arrangement_tab2_2.setText("")
            self.amount_2.setText("")


        if len(paper) > 0:
            amount = 1
            if self.amount_3.text() != "":
                amount = int(self.amount_3.text())

            carbonInt += (amount * int(paper[0][0]))
            coin = int(carbonInt / 100000000)

            if coin > 99999999:
                coin = 100000000
                carbonInt = coin * 100000000

            self.cursor.execute("Update UserInformations set Carbon = ?, Coin = ? where Name = ?",
                                (carbonInt, coin, self.name))
            self.link.commit()

            self.carbonLine.setText(str(carbonInt))
            self.coinLine.setText(str(coin))

            self.arrangement_tab2_3.setText("")
            self.amount_3.setText("")


# Tab - 3 Functions

    def update(self):
        self.cursor.execute("Update UserInformations set Name = ?, Lastname = ?, Mail = ?, Username = ? where SHA256 = ?",
                    (self.firstnameLine.text(), self.lastnameLine.text(), self.mailLine.text(),
                     self.usernameLine.text(), self.SHA256Line.text()))
        self.link.commit()

        self.writingArea_tab3.setText("The update process successfully completed.")


    def delete(self):
        self.certainty = areYouSure(self.name)

    def CoinTransfer(self):
        self.coinTransfer = CoinTransferClass(self.SHA256Line, self.coinLine, self.carbonLine)

    def userSearch(self):
        if self.searchSHA256.text() == "":
            self.writingArea_tab3_2.setText("Please enter a SHA256 Address.")
        else:
            self.cursor.execute("Select Carbon, Coin from UserInformations where SHA256 = ?", (self.searchSHA256.text(),))
            user = self.cursor.fetchall()
            if len(self.searchSHA256.text()) == 64:
                if self.SHA256Line.text() != self.searchSHA256.text():
                    if len(user) != 0:
                        self.userBalance = User_balance(self.searchSHA256.text())
                        self.searchSHA256.setText("")
                        self.writingArea_tab3_2.setText("")
                    else:
                        self.writingArea_tab3_2.setText("No one found with this SHA256 address.")
                else:
                    self.writingArea_tab3_2.setText("This is your own SHA256 address.")
            else:
                self.writingArea_tab3_2.setText("The SHA256 address consists of 64 units.")



class areYouSure(QtWidgets.QWidget):
    def __init__(self, name):
        super().__init__()
        self.init_ui()

        self.name = name

        self.createLink()

    def createLink(self):
        self.link = sqlite3.connect("recycle.db")
        self.cursor = self.link.cursor()

        self.link.commit()

    def init_ui(self):
        self.approveButton = QtWidgets.QPushButton("Approve")
        self.writingArea = QtWidgets.QLabel()
        self.writingArea.setText("Are you sure you want to close your account?")

        self.approveButton.close()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.writingArea)
        v_box.addStretch()
        v_box.addWidget(self.approveButton)

        self.setLayout(v_box)

        self.approveButton.clicked.connect(self.approve)

        width = 960
        height = 540
        appWidth = 110
        appHeight = 50
        self.setGeometry(width - appWidth, height - appHeight, appWidth * 2, appHeight * 2)

        self.setWindowTitle("Recycle App")

        self.show()

    def approve(self):
        self.cursor.execute("Delete From UserInformations Where Name = ?",
                            (self.name,))
        self.link.commit()
        i = 1
        self.close()

class CoinTransferClass(QtWidgets.QWidget):
    def __init__(self, SHA256Line, coinLine, carbonLine):
        super().__init__()
        self.init_ui()

        self.SHA256Line = SHA256Line
        self.coinLine = coinLine
        self.carbonLine = carbonLine

        self.createLink()

    def createLink(self):
        self.link = sqlite3.connect("recycle.db")
        self.cursor = self.link.cursor()

        self.link.commit()

    def init_ui(self):
        self.sendAmount = QtWidgets.QLabel("Gönderilecek Miktar:")
        self.sendAmountLine = QtWidgets.QLineEdit()
        self.sendAmountLine.setValidator(QtGui.QIntValidator(0, 100000000, self))
        self.sendPerson = QtWidgets.QLabel("Gönderilecek Kişi:")
        self.sendPersonLine = QtWidgets.QLineEdit()
        self.sendPersonLine.setPlaceholderText("SHA-256 Adresi")
        self.informationArea = QtWidgets.QLabel()
        self.sendButton = QtWidgets.QPushButton("Send")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.sendAmount)
        v_box.addWidget(self.sendAmountLine)
        v_box.addWidget(self.sendPerson)
        v_box.addWidget(self.sendPersonLine)
        v_box.addStretch()
        v_box.addWidget(self.informationArea)
        v_box.addStretch()
        v_box.addWidget(self.sendButton)

        self.setLayout(v_box)

        self.sendButton.clicked.connect(self.send)

        width = 960
        height = 540
        appWidth = 250
        appHeight = 150
        self.setGeometry(width - appWidth, height - appHeight, appWidth * 2, appHeight * 2)

        self.setWindowTitle("Recycle App")

        self.show()

    def send(self):
        self.cursor.execute("Select Coin, Carbon from UserInformations where SHA256 = ?", (self.SHA256Line.text(),))
        informations = self.cursor.fetchall()

        self.cursor.execute("Select Coin, Carbon From UserInformations Where SHA256 = ?", (self.sendPersonLine.text(),))
        sendedPerson = self.cursor.fetchall()

        coinInt = int(informations[0][0])
        carbonInt = int(informations[0][1])

        if self.sendAmountLine.text() != "" and self.sendPersonLine.text() != "":
            if len(self.sendPersonLine.text()) == 64:
                if len(sendedPerson)!= 0:
                    if self.SHA256Line.text() != self.sendPersonLine.text():
                        if int(self.sendAmountLine.text()) <= coinInt:
                            coinInt -= int(self.sendAmountLine.text())
                            carbonInt -= (100000000 * int(self.sendAmountLine.text()))

                            sendedPersonCoin = int(sendedPerson[0][0])
                            sendedPersonCarbon = int(sendedPerson[0][1])

                            sendedPersonCoin += int(self.sendAmountLine.text())
                            sendedPersonCarbon += (100000000 * int(self.sendAmountLine.text()))

                            kalan = 0
                            if sendedPersonCoin > 100000000:
                                kalan = sendedPersonCoin - 100000000
                                sendedPersonCoin = 100000000
                                sendedPersonCarbon = sendedPersonCoin * 100000000


                            coinInt += kalan
                            carbonInt += (kalan * 100000000)


                            self.cursor.execute("Update UserInformations set Coin = ?, Carbon = ? where SHA256 = ?",
                                                (coinInt, carbonInt, self.SHA256Line.text()))

                            self.cursor.execute("Update UserInformations set Coin = ?, Carbon = ? where SHA256 = ?",
                                                (sendedPersonCoin, sendedPersonCarbon, self.sendPersonLine.text()))

                            self.link.commit()

                            self.sendPersonLine.setText("")
                            self.informationArea.setText("Gönderme işlemi başarılı")

                            self.coinLine.setText(str(coinInt))
                            self.carbonLine.setText(str(carbonInt))

                        else:
                            self.informationArea.setText("You do not have enough Recycle Coins.")
                    else:
                        self.informationArea.setText("You cannot send your Recycle Coins to yourself.")
                else:
                    self.informationArea.setText("No user found with this SHA-256 address.")
            else:
                self.informationArea.setText("The SHA256 address consists of 64 units.")
        else:
            self.informationArea.setText("Please enter the SHA-256 address of the sender and the amount of Recycle Coin \nyou have determined.")

        self.link.commit()

