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
    for num in days.split():
        validate()