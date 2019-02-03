import time 
print (time)
count = 1
var = (" \n")
print ("What is your subject:\nEnglish\nMaths\nScience\nGeography\nElective\nHistory\n")
sub=input(":")
print ("Give Brief Description of Homework task")
des=input(":")
print ("When is due in Hours")
Hour=input(":")
stop = int(Hour)
while stop >= count:
    count += 1
    print (count) 
    time.sleep(3600)
sub = (sub) + (" is due")
import easygui
import winsound
duration = 2000
freq = 990
winsound.Beep(freq, duration)
kar = (var) + (des)
pr = (sub) + (kar)
easygui.msgbox (pr),("Is due")

"""
above outputs msgbox which displays the subject, which is due, then below the description of homework task
"""

