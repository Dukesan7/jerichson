import bs4, requests, lxml, re, time, os
import requests
from bs4 import BeautifulSoup as bs

def basic():
	os.system('cls')
	build = input("What is your choice, mortal?\n\nThief?\nAssassin?\nMage?\nWarrior?\nPaladin?\nLooter?\nArhcer?\nKnight?\nDragonBourn?\nRoyalty?\nOverpowered?\n\nChoice:")
	if build == "Theif":
		print ("Choose Khajiit!\nThese big cats are excellent at unarmed combat, and they're naturals at sneaking and stealth!")
		choice = input("Back to main menu y or n.\n:")
		if choice == "y":
			main()
		else:
			os.system('pause')	
	elif build == "Assassin":
		print ("Choose Bosmer (Wood Elves)\nBosmer can resist disease, resist poison, and receive a +10 archery bonus!")
		choice = input("Back to main menu y or n.\n:")
		if choice == "y":
			main()
		else:
			os.system('pause')
	elif build == "Mage":
		print ("Altmer (High Elves)\nThese adept magic-users receive a +50 Magicka (MP / mana) bonus!")
		choice = input("Back to main menu y or n.\n:")
		if choice == "y":
			main()
		else:
			os.system('pause')
	elif build == "Warrior":
		print ("Orcs (Orsimer)\nOrcs wear heavy armor with ease (and get a small bonus for doing so), and can enter Orc strongholds unchallenged!")
		choice = input("Back to main menu y or n.\n:")
		if choice == "y":
			main()
		else:
			os.system('pause')
	elif build == "Paladin":
		print ("Imperials\nImperials are great at finding extra gold, and they're particularly effective at healing their injuries!")
		choice = input("Back to main menu y or n.\n:")
		if choice == "y":
			main()
		else:
			os.system('pause')
	elif build == "Archer":
		print ("Bosmer (Wood Elves)\nBosmer can resist disease, resist poison, and receive a +10 archery bonus!")
		choice = input("Back to main menu y or n.\n:")
		if choice == "y":
			main()
		else:
			os.system('pause')
	elif build == "DragonBourn":
		print ("Nords\nSkyrim's native race (well, one of them) enjoy natural resistance to frost magic. They also receive a bonus when wielding heavy two-handed weapons!")
		choice = input("Back to main menu y or n.\n:")
		if choice == "y":
			main()
		else:
			os.system('pause')
	elif build == "Royalty":
		print ("Altmer (High Elves)\nThese adept magic-users receive a +50 Magicka (MP / mana) bonus!")
		choice = input("Back to main menu y or n.\n:")
		if choice == "y":
			main()
		else:
			os.system('pause')
	elif build == "Overpowered":
		print ("Dunmer (Dark Elves)\nDunmer enjoy 50% resistance against fire attacks. They also receive small bonuses when casting Destruction magic!")
		choice = input("Back to main menu y or n.\n:")
		if choice == "y":
			main()
		else:
			os.system('pause')
	elif build == "Looter":
		print ("Imperials\nImperials are great at finding extra gold, and they're particularly effective at healing their injuries!")
		choice = input("Back to main menu y or n.\n:")
		if choice == "y":
			main()
		else:
			os.system('pause')
	elif build == "Knight":
		print ("Nords\nSkyrim's native race (well, one of them) enjoy natural resistance to frost magic. They also receive a bonus when wielding heavy two-handed weapons!")
		choice = input("Back to main menu y or n.\n:")
		if choice == "y":
			main()
		else:
			os.system('pause')
	else:
		print("You typed something incorrectly!")
		time.sleep(1)
		os.system('pause')
		main()

def all():
	os.system('cls')
	race_info = scrape()
	print (race_info)
	print ("")
	choice = input("Back to main menu y or n.\n:")
	if choice == "y":
		main()
	else:
		os.system('pause')


def scrape():
	r = requests.get('https://www.usgamer.net/articles/15-11-2017-skyrim-guide-for-xbox-one-and-ps4-which-races-and-character-builds-are-the-best')
	soup = bs(r.content, 'lxml')
	race_info = [ (item.text, item.next_sibling) for item in soup.select('ul strong')]
	race_info = dict(race_info)
	return race_info

def main():
	os.system('cls')
	build = input("Type 1 for character selection and 2 for all races and their abilities.\n:")
	if build == "1":
		basic()
	else:
		all()

main()





