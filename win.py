import sys
from PyQt6.QtWidgets import QApplication
from Browser import Browser

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    browser.open_browser("https://ai.olightcloud.com")
    sys.exit(app.exec())

