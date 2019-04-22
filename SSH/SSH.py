
import paramiko
import module1
import time
from PyQt5.QtCore import pyqtSlot


gmail = "abduallah.ibrahim.gouda@gmail.com"
pasword = "1223456"
ip='192.168.43.182'
port=22
username='brown'
passwordssh='123456'

@pyqtSlot()
def SSH_MAIN(self):
      cmd='ls- ltrh' 
      try:
          ssh=paramiko.SSHClient()
          ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
          ssh.connect(GUI.ip,module1.port,module1.username,module1.passwordssh)
          time.sleep(3)
      except:
          pass
      stdin,stdout,stderr=ssh.exec_command(cmd)
      outlines=stdout.readlines()
      resp=''.join(outlines)
      f= open("GG.txt","a+")
      f.write('\n')
      f.write(resp)
      f.close() 
      stdin,stdout,stderr=ssh.exec_command('some really useful command')
      outlines=stdout.readlines()
      resp=''.join(outlines)
      sys.exit()

