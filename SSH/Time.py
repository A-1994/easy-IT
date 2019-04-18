
import time
import Gmail

a = time.asctime()
day, month, daynumber, timee, year = a.split(' ')
hr, mi, sc = timee.split(':')
if int (hr) > 22:
    Gmail.mailsent('Time to sleep/n  - You')
else:
    Gmail.mailsent('Time LIVERRRR  - You')
    print("bad timing")
print(a)
print(timee)
