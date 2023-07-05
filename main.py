from PyQt5.QtWidgets import QApplication
from Gui.BattleScene import BattleScene
from Classes.Pokemon import Pokemon

if __name__ == "__main__":
    app = QApplication([])

    player = Pokemon("charizard")
    opponent = Pokemon("ekans")

    window = BattleScene(player, opponent)
    window.show()

    app.exec_()
