import time, os

code = input("Speak, my son\n")

x = 0
y = 0

def split(word):
    return [char for char in word]


myballs = (split(code))

fruits = []

for nut in myballs:
    ipman = myballs[x] + "ooven"
    x = x + 1
    if ipman == " ooven":
        ipman = "shmooven"
    if ipman == ".ooven":
        ipman = "."
    if ipman == ",ooven":
        ipman = ","
    fruits.append(ipman)


print (" ".join(map(str,fruits)))


os.system('pause')
#print (ipman)




