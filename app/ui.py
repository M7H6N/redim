#!/usr/bin/python

"""
ReDim

Redim graphic interface

Author: mthgn
"""


import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(1000,500)
        self.move(150, 100)
        self.setWindowTitle("ReDim")
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self,checked):
        print("checked?", checked)

app = QApplication(sys.argv)

w = MainWindow()
w.show()

app.exec()


