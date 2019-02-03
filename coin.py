from random import randint
repeat = True
while repeat:
    print("0=heads 1=tails and You rolled",randint(0,1))
    print("roll again? y or n")
    repeat = ("y" or "yes") in input().lower()