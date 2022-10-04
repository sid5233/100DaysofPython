from unicodedata import name


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    
    def personDetails(self):
        print("His name is : " + self.name)
        print("And his age is : ", self.age)

inst = Person("Bond", 40)
inst.personDetails()