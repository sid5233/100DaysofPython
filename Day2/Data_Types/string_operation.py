import string


string1 = "Hey I'm Python"
print(f"printing your string {string1}")
print("let go for some string operations")
print(f" now see first char {string1[0]}\n")
print(f" now see last char {string1[-1]}\n")
print("REMEMBER : String are immutable This means that elements of a string cannot be changed once it has been assigned. We can simply reassing different string to the same name\n")
print(f"length of your string is {len(string1)}\n")
#ab concatenation bhi dekh lo
string2 = "I'm loving python"
str3 = string1+ " " + string2
print(str3)

#String are immuatable whaterver operation you are going to perform are until for that operation only. They wont chagne the original string.

print(f"in Lowercase -> {string1.lower()}")

print(f"in Uppercase -> {string1.upper()}")

print(f"Operations available on your string : {dir(str3)}")

#some of this operations returns boolean value

print("*".join(str3))
print(str3.center(50))
print(str3.zfill(50))

strr= "           extra space added           "
print(strr.strip())
strr1 = "easy Python is intersting and easy"
print(strr1.strip('easy'))
print(strr1.strip('e').rstrip('y'))
