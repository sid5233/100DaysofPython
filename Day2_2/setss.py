"""
set does not allow duplicate value
UNORDERED AND UNCHANGEBLE
items in set do not have a defined order
item cannot be referred to by index
item cannot be changed, only added or removed
can access only in loop  
"""



unit = "Hours"
calUnit = 24

def calHours(inTDays):
    return f"{inTDays} Days are :  {inTDays * calUnit} {unit}"


def validate():
    try:
        inTDays = int(num)
        if inTDays > 0:
            ans = calHours(inTDays)
            print(ans)
        elif inTDays == 0:
            print("Please dont enter zero")
        else:
            print("you entered negative value")
    except ValueError:
        print("Bhai dont enter string")

days= ""
while days != "exit":
    days = input(f"Hey Please input number : \n")
    for num in set(days.split()):
        validate()