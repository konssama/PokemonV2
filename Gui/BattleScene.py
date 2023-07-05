from PyQt5 import QtCore, QtGui, QtWidgets
from Classes.Pokemon import Pokemon
import requests


class BattleScene(object):
    def __init__(self, player: Pokemon, opponent: Pokemon):
        self.player = player
        self.opponent = opponent

        self.width = 640
        self.height = 480

        self.scene = QtWidgets.QWidget()
        self.setupUi()

    def setupUi(self):
        self.scene.setObjectName("BattleScene")
        self.scene.resize(self.width, self.height)
        self.scene.setFixedSize(QtCore.QSize(self.width, self.height))

        self.background = QtWidgets.QLabel(self.scene)
        self.background.setGeometry(QtCore.QRect(-10, -10, 711, 581))
        self.background.setStyleSheet("background-image: url(./Assets/bg.jpg)")
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("./Assets/bg.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")

        self.playerImage = QtWidgets.QLabel(self.scene)
        self.playerImage.setGeometry(QtCore.QRect(50, 200, 221, 231))
        self.playerImage.setText("")
        self.playerPixmap = QtGui.QPixmap()
        self.playerPixmap.loadFromData(requests.get(self.player.imageBack).content)
        self.playerImage.setPixmap(self.playerPixmap)
        self.playerImage.setScaledContents(True)
        self.playerImage.setIndent(-1)
        self.playerImage.setObjectName("playerImage")

        self.opponentImage = QtWidgets.QLabel(self.scene)
        self.opponentImage.setGeometry(QtCore.QRect(360, 30, 221, 231))
        self.opponentImage.setText("")
        self.opponentPixmap = QtGui.QPixmap()
        self.opponentPixmap.loadFromData(requests.get(self.opponent.imageFront).content)
        self.opponentImage.setPixmap(self.opponentPixmap)
        self.opponentImage.setScaledContents(True)
        self.opponentImage.setIndent(-1)
        self.opponentImage.setObjectName("opponentImage")

        self.background.raise_()
        self.playerImage.raise_()
        self.opponentImage.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.scene)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.scene.setWindowTitle(_translate("BattleScene", "Battle"))

    def show(self):
        self.scene.show()
