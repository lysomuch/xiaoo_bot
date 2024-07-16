from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWidgets import QMainWindow, QApplication, QAction
import os

basedir = '/Users/olight/Documents/resarch/AI/gpt/test/DyberPet'

class YourMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.StatMenu = self.menuBar().addMenu('Menu')  # Assuming you have a menu bar

        action = QAction(QIcon(os.path.join(basedir, 'res/icons/website.svg')), 'Open Website', self)
        action.triggered.connect(self.openWebsite)

        self.StatMenu.addAction(action)

    def openWebsite(self):
        url = QUrl('https://ai.olightcloud.com')
        QDesktopServices.openUrl(url)

if __name__ == '__main__':
    app = QApplication([])
    window = YourMainWindow()
    window.show()
    app.exec()

