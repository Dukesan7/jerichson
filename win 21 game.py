import time
import os

def win():
   to = input("oponent number ")
   if (to) == "1":
      print("add 3")
      os.system('pause')
      os.system('cls')
      win()
   if (to) == "2":
      print("add 2")
      os.system('pause')
      os.system('cls')
      win()
   if (to) == "3":
      print("add 1")
      os.system('pause')
      os.system('cls')
      win()
win()
