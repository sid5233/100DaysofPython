import os
from re import T
from traceback import print_tb

str = input("Enter your string : ")
print(str)

s_t= os.get_terminal_size().columns
print(s_t)

print(str.center(s_t).title())
print(str.ljust(s_t).title())
print(str.rjust(s_t).title())