import os, time, random, re
def main():
    os.system('cls')
    chars = int(input("How many characters do you want for your password?\n:"))
    os.system('cls')
    chars1 = str(input("Are there any specific characters you wish the password to be made of?\ntype r for random characters\ntype s for specific characters\n:"))
    os.system('cls')
    if chars1 == "r":
        ops = ("%", "#", "f", "F", "b", "9", "@", "2", "L", "s", "a", "A", "k", "K", "?", "7", "g", "v", "V", "x", "X", "Z", "T", "c", "0", "!", "!", " ")

        var = 0

        chars = chars - 1

        passs = random.choice(ops)

        while var != chars:
            passs = passs + random.choice(ops)
            var = var + 1
        print (passs)
        os.system('pause')
        main()

    elif chars1 == "s":
        chars1=input("Which characters do you wish your password to be made of?\n:")
        os.system('cls')
        chars1 = list(chars1)
        var = 0

        chars = chars - 1

        passs = random.choice(chars1)

        while var != chars:
            passs = passs + random.choice(chars1)
            var = var + 1
        print (passs)
        os.system('pause')
        main()
main()


















