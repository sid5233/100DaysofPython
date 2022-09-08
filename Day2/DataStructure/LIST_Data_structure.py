
myList = []
mList = [1,1,1, 2, 1.5, "string also"]

print(bool(myList))  # Returns false because its empyt
bool(mList)  # Returns True and it contains data

#we will try access element of string 
print(f"mylist is {*mList[-1][0:],}")
print(f"mylist is {*mList,}")

#we are able to modify list value 
#List are mutable you can modify the value

print(dir(mList))
print(mList.count(1))
mList.append(455)
print(mList)
mList.insert(0,"hello")
print(mList)
newList = [11,22,33]

mList1 = mList.copy()
print(f"mlist 1 is {mList1}")

#append will add as list at end
mList.append(newList)
print(f"appended list {mList}")

#extend will add data at end as element
mList1.extend(newList)
print(f"extended list {mList1}")

#remove will reomve the data we need to pass the data not the index
#pop will remove last element. or we can pass the index
print(mList1.pop())
print(mList1.pop(1))
print(mList1)

list1= [1,5,6,0,11,4,99,12,38,100]
# sort will perform ascending order and then you can use reverse or
list2 = list1

print(list1)
list1.sort()
print(f"sorted list {list1}")
print(f"list 2 {list2}")
list2.sort(reverse=True)
print(f"list two with reverse sorting {list2}")