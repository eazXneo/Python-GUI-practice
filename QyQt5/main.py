from PyQt5 import QtWidgets
# some people use QWidget instead of QMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 50, 350, 350)
        self.setWindowTitle("Tech with Lim")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("first PyQt5 label")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You pressed the button.")
        self.update()

    def update(self):
        # WIT automatically(?!) adjusts the elements size to fit again
        #  --> it doesn't. Need to call it in clicked()
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)  # s.ab. giving config setup based on OS
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()
