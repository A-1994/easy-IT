
import paramiko


ip='192.168.30.25'
port=22
username='root'
password='123'
cmd='cd /lib/python2.7/site-packages/yum  && cat callbacks.py ' 

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,password)

stdin,stdout,stderr=ssh.exec_command(cmd)
outlines=stdout.readlines()
resp=''.join(outlines)
f= open("GG.txt","w+")
f.write(resp)
f.close() 

stdin,stdout,stderr=ssh.exec_command('some really useful command')
outlines=stdout.readlines()
resp=''.join(outlines)
