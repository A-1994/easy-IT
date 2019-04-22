import sys
from PyQt5.QtWidgets import QApplication , QDialog, QMainWindow , QPushButton 
from PyQt5 import QtGui

class window(QMainWindow):
    def __init__ (self):
        super().__init__()


        self.title = 'First'
        self.top = 100
        self.left = 200
        self.width = 400
        self.height = 300
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon('77.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top, self.width, self.height)

    def button1(self):
        self.

        self.show()

App = QApplication(sys.argv)
window = window()
sys.exit(App.exec())