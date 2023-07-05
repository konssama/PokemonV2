from PyQt5.QtWidgets import QWidget, QGridLayout
from Gui.Image import Image


class BattleScene(QWidget):
    def __init__(self, player, opponent):
        super().__init__()

        layout = QGridLayout(self)

        playerImage = Image(image=player.imageBack, parent=self)
        layout.addWidget(playerImage, 1, 0)

        opponentImage = Image(image=opponent.imageFront, parent=self)
        layout.addWidget(opponentImage, 0, 1)

        self.setFixedSize(854, 480)
