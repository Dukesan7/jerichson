legal = 18
print("what is your age?")
age=input(":")
if not age.isdigit():
    print ("You entered an incorrect value")
    import sys
    sys.exit()
var = int(age)
if var < legal:
    print ("You are not allowed to vote")

elif var > legal:
    print ("you elligable to vote : )")

   
