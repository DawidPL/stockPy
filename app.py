# -*- coding: utf-8 -*-
import sys
from PySide2.QtCore import Qt, Slot
from PySide2.QtWidgets import QApplication, QMainWindow, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWidowTitle("StockBook")

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        self.file_menu.addAction(exit_action)

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.resize(800, 600)
    window.show()

    sys.exit(app.exe_())

