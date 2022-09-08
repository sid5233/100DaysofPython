dict = {'one':1, 'two': 2, "float":1.4}
print(dict, type(dict))
print(dir(dict))

#print(dict['there']) will throw error. so use get method
print(dict.get('there'))

print(dict)
#if key is there key  will be updated. if key is not there it will create new key value presentation.
dict['one']=111
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())