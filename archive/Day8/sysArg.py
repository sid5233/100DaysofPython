# Python Sys Module
# while running your python code if you want to interact with python interpreter  then sys module is helpful.

# provides functions and varibales to manipulate different parts of python runtime env

from ast import arg
import sys
print("hello")
# will print all command line arguments passed
#gives list 
# print(sys.argv)
# ['sysArg.py', 'asdf', 'asdf', 'e', 'fs54']
argv = sys.argv
print(argv)
print(argv[0])