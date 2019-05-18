import time, os, random

#imports neccesary libraries/modules

print ("Welcome to Rock paper scissors.\nR = Rock\nP = Paper\nS = Scissors")
time.sleep(3)
os.system('cls')
print ("Rock")
time.sleep(0.5)
os.system('cls')
print ("Paper")
time.sleep(0.5)
os.system('cls')
print ("scissors")
time.sleep(0.5)
os.system('cls')
users_choice = input(str("shoot!\n:"))

s = ("Rock", "Paper")
r = ("Scissors", "paper")
p = ("Scissors", "Rock")

ops = ("scissors", "Rock", "Paper")

if users_choice in ("scissors", "Scissors"):
	print (random.choice(s))
	os.system('pause')

if users_choice in ("Rock", "rock"):
	print (random.choice(r))
	os.system('pause')

else:
	print (random.choice(p))
	os.system('pause')
