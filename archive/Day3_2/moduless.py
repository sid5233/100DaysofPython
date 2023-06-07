

import os

def calHours(inTDays, convUnit):
    if convUnit == "hours":
        return f"{inTDays} Days are :  {inTDays * 24} hours"
    elif convUnit == "minutes":
        return f"{inTDays} Days are :  {inTDays * 24 * 60 } minutes"
    else:
        return "unsupported Unit"


def validate(daysAndUnitDict):
     print("OSS ", os.name)
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

messg ="Hey Please input number : \n"