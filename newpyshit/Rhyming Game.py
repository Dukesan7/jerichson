#introducing, Erich's python game!.

import time, os
from random_word import RandomWords


def game():
    os.system('cls')
    r = RandomWords()

    randword = str(r.get_random_word())
    randword = randword + "\n\n"
    word = input(randword)
    game()

    if word == "exit":
        main()

def main():
    os.system('cls')

    print("Erich's rhyming game\n\n")

    objective = input("start? $")

    if objective == "y":
        game()

    else:
        main()


main()

