"""
set does not allow duplicate value
UNORDERED AND UNCHANGEBLE
items in set do not have a defined order
item cannot be referred to by index
item cannot be changed, only added or removed
can access only in loop  
"""

mySet = {"jan", "feb", "mar"}

for  mon in mySet:
    print(mon)

mySet.add("April")
print(mySet)