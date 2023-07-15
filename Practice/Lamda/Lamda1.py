# One Argument
result = lambda a : a+10
print(result(10))

# Multiple Argument
result2 = lambda a,b,c : a+b+c
print(result2(2,3,4))

# Lamda Function
def myfunc(n):
    return lambda a : a*n

doubleupvalue = myfunc(2)
print(doubleupvalue(11))