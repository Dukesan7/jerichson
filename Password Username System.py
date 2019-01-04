while True:
    print ("Enter your Username")
    print ("\nIf you dont have an a account type 'r' to register")
    inp = input(":")
    if inp == "r":
              print ("Enter your desired Username")
              usr = input(":")
              print ("Enter your desired Password")
              pas = input(":")

              print("Enter your Username")
              us = input(":")
              if us == usr:
                        print ("Enter your Password")
                        pus = input(":")
              elif us != usr:
                        print("Incorrect Username")
                        import os
                        os.system('pause')
                        break
              if pus == pas:
                        print ("Succesfully logged in")
                        import os
                        os.system('pause')
                        break
              elif pus != pas:
                        print("Incorrect Password")
                        import os
                        s.system('pause')
                        break
              if inp == usr:
                        print ("Enter your Password")
                        inp = input(":")
              elif inp != usr:
                        print ("Incorrect Username")
                        import os
                        os.system('pause')
                        break
              if inp == pas:
                        print (" Succesfully logged in")
              elif inp != pas:
                        print ("Incorrect Password")
                        import os
                        os.system('pause')
                        break
