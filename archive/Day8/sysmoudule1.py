# usr_str = input("Entr your string")
# usrAction = input("Enter your action")
import sys
usrAction = sys.argv[2]
usr_str = sys.argv[1]

if len(sys.argv) != 3:
    sys.exit()
else:
    if usrAction == "lower":
        print(usr_str.lower())
    elif usrAction == "upper":
        print(usr_str.upper())
    elif usrAction == "title":
        print(usr_str.title())
    else:
        print("your option is invalid")
    

 