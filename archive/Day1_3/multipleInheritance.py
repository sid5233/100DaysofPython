

class Animal:
    def kind(self):
        print("this is animal")
        
class cat:
    def subDomain(self):
        print("she is a cat type")
        
class tiger(Animal,cat):
    pass

tigerObject = tiger()
tigerObject.kind()
tigerObject.subDomain()

# TO check the base class of child class
print(tigerObject.__class__.__base__)