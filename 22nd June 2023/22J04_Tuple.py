my_list = [52, 21, 56]
print(my_list)
my_list[0] = 31
print(my_list)

# List is - Mutable in nature , That means i can be change

# Tuple - Tuple is imputable that means the value  not be change
car = ("i10","XUV700","Safari")
print(car)
print(car[0:2])
print(car[:])
print(car[:-1])
print(car[::-1])
print(len(car))

list1 = [1,2,3,4,5,6]
print("\nTuple using List:")
print(tuple(list1))

Tuple1 = tuple('Dipak')
print("\nTuple with the use of function: ")
print(Tuple1)

# Unpack
tuple1 = (3, 4, 5)
a, b, c = tuple1
print(a)
print(b)
print(c)

# Duplicate is allowed?
dup = [33, 33, 44, 55, 55]
t_dup = tuple(dup)
print(t_dup)

del t_dup
#print(t_dup)