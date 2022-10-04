#factorial

from weakref import ref


def recFn(num):
    if  num == 1:
        return 1
    else:
        return (x * recFn(num -1))

x = 5
fac = recFn(x)
print(fac)