from unicodedata import name

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# We can define a new class  with some more functionalities that inherits the properties of previously defined class. and the class from which new class inherits the properties is call parent class or base class . and the new class which we created is called child class.

#super function ()
# super fn will help to inherits its all the method and properties from its parent class. such that we dont need to use the same name of parent element super fn will automatically inherit the methods and properties from its parent class.


class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    
    def personDetails(self):
        print("His name is : " + self.name)
        print("And his age is : ", self.age)

# class programmer(Person):
#     def __init__(self,name,age,prefession):
#         Person.__init__(self,name,age)
#         self.prefession = prefession
#     def kind(self):
#         print(f"He is {self.prefession} programmer")
        
# instPro = programmer("Bond", 40,"Python")
# instPro.personDetails()
# instPro.kind()


# Using SUPER() function
class programmer(Person):
    def __init__(self,name,age,prefession):
        super().__init__(name,age)
        self.prefession = prefession
    def kind(self):
        print(f"He is {self.prefession}")
        
instPro = programmer("James Bond", 40,"Detective")
instPro.personDetails()
instPro.kind()