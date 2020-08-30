#Erichs hangman thing


import time, os
from random_word import RandomWords


def split(word):
    return [char for char in word]

def game():
    os.system('cls')
    gun = "         *======"
    handle = "             ||"
    gunls = (split(gun))
    x = 0
    y = 9
    r = RandomWords()
    randword = str(r.get_random_word())
    randword = randword.lower()
    lword = (split(randword))
    #print (lword)
    guesses = [" "]

    fadedlist = (split(randword))


    while x < len(fadedlist):
        for items in fadedlist:
            fadedlist[x] = "_"
            x = x + 1

    while True:
        os.system('cls')

        print("")
        print (" ".join(map(str,fadedlist)), "\n\n", "".join(map(str,guesses)))
        print ("\n\n ")
        print ("   ( )", "".join(map(str,gunls)))
        print("  __|__", handle)
        print ("    |")
        print ("   | |")

        guess = input("\n\nguess a word\n\n$ ")
        #print(gunls)
        #print(fadedlist)

        if gunls == ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '=', '=', '=', '=', '=', '=']:
            os.system('cls')
            print("Oh shit! You failed the game, and Timmy died :(\n\n The real word was", randword, "\n\n Exit or Main Menu? (e or m)\n\n")
            dec = input("$ ")
            if dec == "e":
                quit()
            else:
                main()



        if guess in lword:

            av = 0

            for items in lword:
                if av >= len(lword):
                    break
                if lword[av] == guess:
                    fadedlist[av] = guess
                    av = av + 1
                else:
                    av = av + 1


        elif guess not in lword:
            gunls[y] = "-"
            y = y - 1
            guesses.append(guess)
            print("wrong!")
            os.system('pause')

        if lword == fadedlist:
            os.system('cls')
            print("Congradulations! You've won the game Nigga!\n\n The word was", randword, "\n\n Quit or Main Menu? (e or m)\n\n")
            dec = input("$ ")
            if dec == "e":
                quit()
            else:
                main()


def main():

    os.system('cls')

    cap = input("who wants to play hangman kiddies!!\n\n$ ")
    if cap == "y":
        game()
    else:
        main()



main()