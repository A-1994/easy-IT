
gmail = "abduallah.ibrahim.gouda@gmail.com"
pasword = "1223456"
port=22
username='brown'
passwordssh='123456'

#import sys
#from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
#from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import pyqtSlot
 
#class App(QMainWindow):
 
#    def __init__(self):
#        super().__init__()
#        self.title = 'PyQt5 textbox - pythonspot.com'
#        self.left = 10
#        self.top = 10
#        self.width = 400
#        self.height = 140
#        self.initUI()
 
#    def initUI(self):
#        self.setWindowTitle(self.title)
#        self.setGeometry(self.left, self.top, self.width, self.height)
         
#        # Create textbox
#        self.textbox = QLineEdit(self)
#        self.textbox.move(20, 20)
#        self.textbox.resize(280,40)
 
#        # Create a button in the window
#        self.button = QPushButton('Show text', self)
#        self.button.move(20,80)
         
#        # connect button to function on_click
#        self.button.clicked.connect(self.on_click)
#        self.show()
#    @pyqtSlot()
#    def on_click(self):
#        textboxValue = self.textbox.text()
#        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
#        self.textbox.setText("")
         
#if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    ex= App()
#    sys.exit(app.exec_())






import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This s an example button')
        button.move(100,70) 
        button.clicked.connect(self.on_click)

        self.show()
        
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())  
