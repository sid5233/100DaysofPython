'''
Python Closures are these nested/inner functions that are enclosed within the outer function. Closure can variable present in the outer function scope. It can access these  variables even after the outer function  has completed its execution`
'''
def greet(name):
    def greetFirstName():
        print("Hello",name)
    
    return greetFirstName

printFirstname = greet("Sudya")
printFirstname();