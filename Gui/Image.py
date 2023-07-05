import requests
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtGui import QPixmap


class Image(QLabel):
    def __init__(self, image: str, parent: QWidget):
        super().__init__(parent)

        self.pixmapImage = QPixmap()
        self.pixmapImage.loadFromData(requests.get(image).content)
        self.resizePixmapImage(100, 100)

        self.setPixmap(self.pixmapImage)

    def resizePixmapImage(self, x: int, y: int):
        self.pixmapImage.scaled(
            QSize(x, y), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio
        )
