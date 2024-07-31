from PyQt5 import QtWidgets
# some people use QWidget instead of QMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)  # s.ab. giving config setup based on OS
    win = QMainWindow()
    win.setGeometry(100, 50, 350, 350)
    win.setWindowTitle("Tech with Lim")

    label = QtWidgets.QLabel(win)
    label.setText("first PyQt5 label")
    label.move(50,50)

    win.show()
    sys.exit(app.exec_())

window()
