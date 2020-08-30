#Encryptor Decrypter.

import time, os

def main():
    os.system('cls')
    nig = input("Decrypt or Encrypt\n\n$")

    if nig == "e":
        encrypt()
    else:
        decrypt()

def encrypt():
    os.system('cls')
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '.', ',', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    alph2 = ['x', 'v', '4', 'z', '1', '2', 'j', 'h', 'i', 'l', 'm', '.', ',', 'w', '=', '-', '9', 'f', 'n', 'b', '@', '#', 's', 'u', 'o', '0', '>', '+', '!', '(', ')', '%', '^', '~', '`', '*', '$', '&', '[', ']', '{', '}', '|', '"', '_', 'Y', 'G', 'E', 'J', 'Z', 'L', 'P', 'X', 'D', 'H']


    x = 0
    poo = []
    booven = input("Encryption:\n\n$")



    def split(word):
        return [char for char in word]
    hooven = (split(booven))



    for niggerpoo in hooven:
        bob = hooven[x]
        fag = alph.index(bob)
        charlie = alph2[fag]
        poo.append(charlie)
        x = x + 1

    print ("".join(map(str,poo)))
    os.system('pause')
    main()

def decrypt():
    os.system('cls')

    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '.', ',', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    alph2 = ['x', 'v', '4', 'z', '1', '2', 'j', 'h', 'i', 'l', 'm', '.', ',', 'w', '=', '-', '9', 'f', 'n', 'b', '@', '#', 's', 'u', 'o', '0', '>', '+', '!', '(', ')', '%', '^', '~', '`', '*', '$', '&', '[', ']', '{', '}', '|', '"', '_', 'Y', 'G', 'E', 'J', 'Z', 'L', 'P', 'X', 'D', 'H']


    x = 0
    poo = []
    booven = input("Decryption:\n\n$")

    def split(word):
        return [char for char in word]

    hooven = (split(booven))

    for niggerpoo in hooven:
        bob = hooven[x]
        fag = alph2.index(bob)
        charlie = alph[fag]
        poo.append(charlie)
        x = x + 1

    print("".join(map(str, poo)))
    os.system('pause')
    main()

main()


