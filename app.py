# -*- coding: utf-8 -*-

from Charts import chart_folding_percent
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton


class Chart(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interface()

    def interface(self):

        label1 = QLabel('<font color=red size=24>Kurs</font>', self)
        label2 = QLabel('<font color=green size=24>Data</font>', self)
        button = QPushButton('Pokaz')

        grid_position = QGridLayout()
        grid_position.addWidget(label1, 0, 0)
        grid_position.addWidget(label2, 0, 1)

        button.show()
        self.setLayout(grid_position)
        self.resize(800, 500)
        self.setWindowTitle('Wykres złota')
        self.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Chart()
    sys.exit(app.exec_())

