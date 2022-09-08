empty_tuple = ()
my_tuple = (1,2,3)

print(my_tuple)

tuple1 = (11,61,5, [1,38,4,0])
print(tuple1[3])
print(tuple1[3][1])

#you cannot modify the tuple  value or item of tuple.
# tuple are immutable. But entire tuple can be modified.
#typeError: 'tuple' object does not support item assignment

tuple1[1]=0
print(tuple1)
