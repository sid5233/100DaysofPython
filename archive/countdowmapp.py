from dataclasses import dataclass
import datetime

userInput = input("enter your goal with dealdline sep by column\n")
inputList = userInput.split(":")

goal= inputList[0] 
deadline = inputList[1]

deadlinDate = datetime.datetime.strptime(deadline, "%d.%m.%Y")

today = datetime.datetime.today()

print(deadlinDate - today)