import bs4
import requests
from bs4 import BeautifulSoup as soup
import lxml
import re
import time
import os
import webbrowser
import re

def webscrape():
	res = requests.get('https://github.com/Dukesan7/jerichson') #Chooses which website to copy down for BeautifulSoup.
	soup = bs4.BeautifulSoup(res.text, 'lxml') #Its going into parsing mode. This mean its ready to read it and find elements.
	files_list = soup.select('tr.js-navigation-item > td.content') #I selected the tags were are projects are listed under.
	files_list_text = [f.text.strip() for f in files_list] # removing unwanted tags.
	print(files_list_text) #printing final result.
	time.sleep(1)
	print ("\n1. Main Menu: 1")
	print ("2. exit?: 2")
	op = input (":")
	if op == "2":
		exit()
	else:
		MainMenu()


def op1():

	os.system('cls')
	webbrowser.open('https://github.com/Dukesan7/jerichson') #Opens our github page using webbrowser module.
	time.sleep(1)
	print ("1. Main Menu: 1")
	print ("2. exit?: 2")
	op = input (":")
	if op == "2":
		exit()
	else:
		MainMenu()




def MainMenu():

	os.system('cls')
	print ("Erichs amazing github program list!")
	print ("------------------------------------")
	print ("Option 1: Go to github page: 1")
	print ("Option 2: List files on page: 2")
	print ("Option 3: exit: 3")
	op = input (":")
	if op == "1":
		op1()
	elif op == "2":
		webscrape() #Calls the webscraping function
	if op == "3":
		exit()

#Calls The Menu function above.
MainMenu()



 
