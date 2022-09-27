unit = "Hours"
calUnit = 24

def calHours(inTDays):
    return f"{inTDays} Days are :  {inTDays * calUnit} {unit}"


def validate():
    if days.isdigit():
        inTDays = int(days)
        if inTDays > 0:
            ans = calHours(inTDays)
            print(ans)
        else:
            print("Please dont enter zero")
    else :
        print("Bhai dont enter string")

days = input(f"Hey Please input number : \n")
validate()