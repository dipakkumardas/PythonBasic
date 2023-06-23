# List Built In Function

my_list = [1,2,3]

#Index
print(my_list[0])

#Slicing
print(my_list[0:3])
print(my_list[0:2])
print(my_list[2:])
print(my_list[:-1])
print(my_list[:-2])

# Extends My List
my_list.extend([4,5])
print(my_list)

#Pop = Removed and Item
i = my_list.pop(1)
print(i)
print(my_list) # List can Mutable in nature , Tht means it changeable
my_list.append(1)
print(my_list)
print(my_list.count(1))
my_list.reverse()
print(my_list)

my_list.pop()   # If we not mentioned any thing it's removed for the last
print(my_list)


