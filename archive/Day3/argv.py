import sys
usr_str = sys.argv[1]
opr= sys.argv[2]

if opr== 'lower':
    print(usr_str.lower())
elif  opr=='upper':
    print(usr_str.upper())
else:
    print("enter valid operation")