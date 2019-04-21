
import paramiko
import module1
import time


 
cmd='cd project  && python3 Time.py ' 
print ('Creating connection , please wait.')
time.sleep(3)
print ('................')

time.sleep(3)
print (' .................')
time.sleep(3)
print (' ....................')
try:
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(module1.ip,module1.port,module1.username,module1.passwordssh)
    time.sleep(3)
    print ('Getting you script ready , please wait .......')
except:
    print('try again ...')

stdin,stdout,stderr=ssh.exec_command(cmd)
outlines=stdout.readlines()
resp=''.join(outlines)
f= open("GG.txt","a+")
f.write('\n')
f.write(resp)
f.close() 
print ('Done check you GG file .')

stdin,stdout,stderr=ssh.exec_command('some really useful command')
outlines=stdout.readlines()
resp=''.join(outlines)
