import time
import os

def start():
   name = input("what is your name ")
   if name.isalpha() == False:
      print((name)+(" is not a eligible name"))
      time.sleep(2)
      os.system('pause')
      os.system('cls')
      start()
   else:
       age = input("what is your age ")
       if age.isdigit() == False:
           print((age)+(" is not a eligible age"))
           time.sleep(2)
           os.system('pause')
           os.system('cls')
           start()
       else:
           print(("your name is ")+(name)+(" and you are ")+(age)+(" years old"))
           time.sleep(2)
           os.system('pause')
           os.system('cls')
           start()
start()
