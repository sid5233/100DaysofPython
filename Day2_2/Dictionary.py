
calUnit = 24

def calHours(inTDays, convUnit):
    if convUnit == "hours":
        return f"{inTDays} Days are :  {inTDays * calUnit} hours"
    elif convUnit == "minutes":
        return f"{inTDays} Days are :  {inTDays * calUnit * 60 } minutes"
    else:
        return "unsupported Unit"



def validate():
    try:
        inTDays = int(daysAndUnitDict["days"])
        if inTDays > 0:
            ans = calHours(inTDays, daysAndUnitDict["unit"])
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
    noOfDays = days.split(":")
    daysAndUnitDict = {"days": noOfDays[0], "unit": noOfDays[1]}
    validate()