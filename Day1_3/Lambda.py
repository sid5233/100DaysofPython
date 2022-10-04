'''
Doc string - Used to describe what the function does

Anonymous Function / Lambda Function
Lambda is good for single line expresssion. And only one expression can be used
'''

'''
doSum = lambda a,b: a + b
print(doSum(10,20))
'''

myList = [1,2,34,5,56,87,6,4,8,6]
myFilList = list(filter(lambda x: (x>5) , myList))
print(myFilList)

#Using Lambda To manipulate data
anotherList = [1,2,3,4,5,6,7,8]
updatedList = list(map(lambda x: x+x, anotherList))
print(updatedList)