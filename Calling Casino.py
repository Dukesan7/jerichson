import time
import os
from threading import Thread
import random
def black():
    Ace = 1
    Face = 10
    print("Dealer deals cards")
    time.sleep(1)
    hand = [Ace, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, Face]
    deal = [Ace, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, Face]
    hit = [Ace, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, Face]
    var = random.choice(hand)
    var2 = random.choice(hand)
    var3 = random.choice(deal)
    var4 = random.choice(deal)
    var5 = random.choice(hit)
    cards = var, var2
    hit = var5
    dealer = var3, var4
    
    print ("You have", (cards))
    time.sleep(1)
    print("Would you like to hit or stand?")
    option=input(":")
    if option == "stand":
        if (dealer) >= (cards):
            print ("You lose, dealers hand", (dealer))
            time.sleep(1)
            a()
        elif (dealer) <= (cards):
            print("You win!")
            time.sleep(1)
            a()
    if option == "hit":
        cards = var, var2, var5
        if var+var2+var5 > 21:
            print("You lose, your value was over 21! your cards were", cards)
            time.sleep(1)
            a()
        print ("You took a stand your cards are", cards)
        if var3+var4+var5 > 21:
            print ("you win, the dealers hand was over 21", dealer)
            time.sleep(1)
            a()
        if (dealer) >= (cards):
            print ("You lose, dealers hand", (dealer))
            time.sleep(1)
            a()
        elif (dealer) <= (cards):
            print("You win! Dealers hand", dealer, "Your hand", cards)
            time.sleep(1)
            a()
def slots():
    slot = ["cat", "cat", "cat", "dog", "dog", "dog", "bird", "bird", "bird"]
    chanc = random.choice(slot)
    chanc2 = random.choice(slot)
    chanc3 = random.choice(slot)
    if chanc == chanc2 == chanc3:
        print (chanc, chanc2, chanc3, "You won!")
        time.sleep(1)
        a2()
    else:
        print (chanc, chanc2, chanc3, "You lost, surely next time!")
        time.sleep(1)
        a2()
def a():
    print ("Would you like to play again, or go to main menu - Play again - Menu")
    choice=input(":")
    if choice == "Play again":
        black()
    else:
        menu()
def a2():
    print ("Would you like to play again, or go to main menu - Play again - Menu")
    choice=input(":")
    if choice == "Play again":
        slots()
    else:
        menu()
def a3():
    print ("Would you like to play again, or go to main menu - Play again - Menu")
    choice=input(":")
    if choice == "Play again":
        Mill()
    else:
        menu()
def Mill():
    print("Welcome to Who Wants To Be A Millionaire!")
    time.sleep(1)
    print("You will be asked a series of variouse questions to determine your intellegince, and if your worthy enough, you get the ultimate prize!")
    time.sleep(6)
    print("1 MILLION DOLLARS")
    time.sleep(2)
    def q():
        print("First Question!")
        time.sleep(1)
        print("What is the airspeed velocity of an unladen swallow? only one question becuase I have a 0.5c budget :D")
        a=input(":")
        if a == "African or European?":
            print("CONGRATULATIONS You just won 1 MILLION DOLLARS")
            a3()
        else:
            print ("Incorrect, next time surely")
            a3()
    q()
print ("Hello! and welcome to the Callers Casino!\nThis is an wondeful place where all your dreams come true, if you know how to play")
os.system('pause')
print ("Here are the rules:\n*No counting cards!")
time.sleep(1)
print ("*No loopholing around rules")
time.sleep(1)
print ("*And always have fun!")
time.sleep(1)
print ("Lets begin")
time.sleep(2)
def menu():
    print ("Which game would you like to play?")
    time.sleep(1)
    print ("*BlackJack?")
    time.sleep(2)
    print ("*Slots?")
    time.sleep(2)
    print ("*Who wants to be a Millionair! just type Mill for short!")
    game=input(":")
    if game == "BlackJack":
        time.sleep(1)
        print("BlackJack it is!")
        black()
        menu()
    if game == "Slots":
        time.sleep(1)
        print("slots it is")
        slots()
        menu()
        os.system('pause')
    if game == "Mill":
        time.sleep(1)
        Mill()
        menu()
        os.system('pause')
    else:
        os.system('pause')
menu()
