import moduless as m



days=""
while days != "exit":
    days = input(m.messg)
    noOfDays = days.split(":")
    daysAndUnitDict = {"days": noOfDays[0], "unit": noOfDays[1]}
   
    m.validate(daysAndUnitDict)