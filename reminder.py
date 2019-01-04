import datetime 
import time
var = 1
remind = 1
print ("What is the name of this event")
event = input(":")
et = datetime.datetime.now()
(event) += " is due"
print ("When would you like to be reminded? in seconds")
remind = input(":")
stop = int(remind)
while stop >= var:
    var +=1
    print (var)
    time.sleep (1)
import easygui
import winsound
duration = 2000
freq = 990
winsound.Beep(freq, duration)

easygui.msgbox (event),("is due")
