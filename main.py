from PyQt5.QtWidgets import QApplication
from Gui.BattleScene import BattleScene
from Classes.Pokemon import Pokemon

app = QApplication([])

player = Pokemon("ekans")
opponent = Pokemon("pidgey")

window = BattleScene(player, opponent)
window.show()

app.exec()
