import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QCoreApplication
from PyQt5 import QtGui
import time
import paramiko


gmail = "abduallah.ibrahim.gouda@gmail.com"


class window(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.title = 'First'
        self.top = 100
        self.left = 200
        self.width = 600
        self.height = 600
        self.InitWindow()
        

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon('77.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top, self.width, self.height)
        #===============================
        self.b1 = QPushButton('Find',self)
        self.b1.resize(200,100)
        self.b1.move(200,350)
        self.b1.clicked.connect(self.SSH_MAIN)
        #================================
        self.ip_get = QLineEdit(self)
        self.ip_get.move(200,200)
        self.ip_get.resize(200,100)
        self.ip_get.text()
        self.show()


    @pyqtSlot()
    def SSH_MAIN(self):
      self.ip=self.ip_get.text()
      self.port=22
      self.username='brown'
      self.passwordssh='123456' 
      self.cmd='cd project && python3 Time.py' 
      self.ssh=paramiko.SSHClient()
      self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      self.ssh.connect(self.ip, self.port, self.username, self.passwordssh)
      self.stdin, self.stdout, self.stderr = self.ssh.exec_command(self.cmd)
      self.outlines = self.stdout.readlines()
      self.resp=''.join(self.outlines)
      textboxValue = self.resp
      QMessageBox.question(self, 'Message - Unix-1', "You Files: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
      #self.textbox.setText("")
      #self.f = open("GG.txt","rw")
      #self.f.write('new line  \n')
      #self.f.write(self.resp)
      #self.f.close() 
     


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = window()
    sys.exit(app.exec_())  