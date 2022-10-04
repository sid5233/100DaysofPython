'''
design pattern that allows us to add new functionality to an existing code without modifying its structure. The decorator acts as wrapper.
It is also called metaprogramming because a part of the program tries to modify another part of the program at compile time.

Use cases 
Authorization in python  web framework such as flask and django
Logging and execution time tracking
'''

def formatGreet(func):
    def innerFunc(name):
        print("----------")
        func(name)
        print("----------")
    return innerFunc

@formatGreet
def greetFirstName(name):
    print("hey Decorator Here: ", name)

# callingGreet= formatGreet(greetFirstName)
# callingGreet("Ohhhhh")

greetFirstName("thats coool")