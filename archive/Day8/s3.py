from datetime import datetime

import datetime

userInput = input("Enter your goal with deadline seperated by colon\n")

inputList = userInput.split(":")

goal = inputList[0]

deadline = inputList[1]

deaddate = datetime.datetime.strptime(deadline, "%d.%m.%Y")

current_date = datetime.datetime.today()

tillDate = deaddate - current_date 

print(f"dear user time remainng for your goal is {goal} is {tillDate.days} days ")