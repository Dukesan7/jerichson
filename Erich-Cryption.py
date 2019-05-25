import time, os # imports modules
def main():
    os.system('cls')
    inp=input("Encoder or Decoder: E or D.\n\npython@user$ ") #Asks which  tool they want to use (Encoder/Decoder)
    
    if inp in ("E", "e"): #Sees if user chooses encoder.
        os.system('cls') # clears the screen.
        encode() #Goes to 'encode' function.
        
    else: 
        decode() #goes to 'decode' function.

        
def encode():
    
    inp=input ("What do you wish to encode? - Must be a sentence\n\npython@user$ ") # Retrievs what the user wants to translate.
    
    list_of_inp = list(inp) #turns inputted string value into a list where every character is an item.
    
    list_of_inp[1], list_of_inp[5], = list_of_inp[5], list_of_inp[1]
    list_of_inp[0], list_of_inp[3], = list_of_inp[3], list_of_inp[0]
    list_of_inp[2], list_of_inp[8], = list_of_inp[8], list_of_inp[2]


    reversed_list = (list_of_inp[::-1]) #Reverses the list.
                                                                            #--|
    reversed_list[2], reversed_list[6] = reversed_list[6], reversed_list[2] #  |
    reversed_list[1], reversed_list[9] = reversed_list[9], reversed_list[1] #   ---- Switches values of the list to make it more rnadom.
    reversed_list[7], reversed_list[4] = reversed_list[4], reversed_list[7] #  |
                                                                            #--|
    
    for item in reversed_list:
        print (item, end = "") #Prints every character in list and removes unwanted spaces.
        
    print()    

    os.system('pause') #Press ant key to continue.
    
    time.sleep(1) #waits one second.
    
    main()
    
def decode():

    
    inp=input ("What do you wish to decode?\n\npython@user$ ") # Retrievs what the user wants to translate.
    
    list_of_inp = list(inp) #turns inputted string value into a list where every character is an item.

                                                                    #--|                            
    list_of_inp[2], list_of_inp[6] = list_of_inp[6], list_of_inp[2] #  |
    list_of_inp[1], list_of_inp[9] = list_of_inp[9], list_of_inp[1] #   ---- Switches back the items.
    list_of_inp[7], list_of_inp[4] = list_of_inp[4], list_of_inp[7] #  |
                                                                    #--|
    
    reversed_list = (list_of_inp[::-1]) #Reverses the list to normal.

    reversed_list[1], reversed_list[5], = reversed_list[5], reversed_list[1]
    reversed_list[0], reversed_list[3], = reversed_list[3], reversed_list[0]
    reversed_list[2], reversed_list[8], = reversed_list[8], reversed_list[2]


    for ch in reversed_list:
        print (ch, end = "") #Prints every character in list and removes unwanted spaces.

    print()

    os.system('pause') #Press any key to continue.
    
    time.sleep(1) #Waits 1 second.
    
    main() #returns to 'main' function.

main() #calls main function to start the program.


