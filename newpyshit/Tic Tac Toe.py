#python tic tac toe lol

import time,os

def game():
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    s6 = 0
    s7 = 0
    s8 = 0
    s9 = 0
    end = True
    markcount = 1

    os.system('cls')

    print("tic tac toe lol\n\njust enter the position you want your marker to go to. Let the game do the rest XD")

    os.system('pause')

    screen =  [[s1, s2, s3],
               [s4, s5, s6],
               [s7, s8, s9]]

    while end:
        os.system('cls')
        # print("  0  1  2")
        #
        for row in screen:
            print(row)

        if markcount % 2 == 0:
            print("Your turn 2's")

        else:
            print("Your turn 1's")
        cap = input("where do you want to mark\n\n$ ")
        #input should look like 1 2 1

        if cap == "1":
            x = 0
            y = 0
        if cap == "2":
            x = 1
            y = 0
        if cap == "3":
            x = 2
            y = 0
        if cap == "4":
            x = 0
            y = 1
        if cap == "5":
            x = 1
            y = 1
        if cap == "6":
            x = 2
            y = 1
        if cap == "7":
            x = 0
            y = 2
        if cap == "8":
            x = 1
            y = 2
        if cap == "9":
            x = 2
            y = 2


        # def split(word):
        #     return [char for char in word]
        # capture = (split(cap))

        # x = int(capture[1])
        # y = int(capture[0])
        # mark = int(capture[2])

        if markcount % 2 == 0:
            mark = 2
        else:
            mark = 1

        screen[y][x] = mark
        markcount = markcount + 1
        if cap == "exit":
            main()



def main():

    os.system('cls')

    print ("who wants to play tic tac toe?\n\n")

    opt = input("$ ")

    if opt == "y":
        game()
    else:
        main()




main()
gameloop()