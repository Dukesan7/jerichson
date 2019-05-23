import os, time, sys, random

def menu():
		os.system('cls')
		choicee = input("Do you want to play again? y or n")
		if choicee == "y":
				main()
		else:
				os.system('pause')

def game():
		os.system('pause')
		var = 1
		while var != 20:
				why = (1, 2, 3)
				choicee = input("users number: ")
				choicee = int(choicee)
				ran = random.choice(why)
				time.sleep(1)
				choicee = str(choicee)
				if choicee == "20":
						var = 20
						print ("you won!")
						time.sleep(1)
						os.system('pause')
						menu()
				elif choicee in ("17", "18", "19"):
						print ("20\nYou lost!")
						time.sleep(1)
						os.system('pause')
						menu()
				choicee = int(choicee)
				if choicee > 20:
						os.system('cls')
						op = input("CHEATER! - THAT IS NOT ALLOWED!\nEXIT - 1\nPLAY AGAIN - 2\n:")
						if op == 2:
								os.system('pause')
								menu()
						else:
								quit()
				print ("Computor: ", ran + choicee)

def menu():
		os.system('cls')
		choicee = input("Welcome to better 21's, I've reduced the code by more than 250 lines!\nDo you want to start the game? y or n\n:")
		if choicee == "y":
				game()
		elif choicee == "n":
				why = (1, 2, 3)
				ran = random.choice(why)
				print("Computor: ", ran)
				time.sleep(1)
				game()
		else:
				print ("You typed something incorrectly!")
				time.sleep(1)
				os.system('pause')
				menu()

				
menu()
