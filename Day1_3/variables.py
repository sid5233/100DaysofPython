#global variable Local Variable and nonlocal variable

x = "this is global"

def myfun():
    x = "this is local now"
    print(x)
    def anotherFn():
        nonlocal x 
        x = "hey nestet x"
        print(x)
    anotherFn()

myfun()
print(x)