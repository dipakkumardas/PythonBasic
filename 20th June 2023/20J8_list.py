# List
# Store the Elements
# Differnt data type
# List item can be changeable

# Create List

my_marks = []
#my_marks2 = list()
print(type(my_marks))
#print(type(my_marks2))
my_marks.insert(0,91)
my_marks.insert(1,98)
my_marks.insert(1,77)
print(my_marks)
my_marks.append(89)  # It's always add to last
print(my_marks)
print(len(my_marks))
my_marks.remove(77)
print(my_marks)
print(len(my_marks))
my_marks.clear()
print(my_marks)

nested_list = [[1,2,3],[2,2,4],[4,5,6]]
print(nested_list[0])
print(nested_list[1])
print(nested_list[2])

# Change the value
nested_list[0]=["abc","david","peter"]
print(nested_list)

dup_list = [1,1,1,1,1,1,1,1,1,1,1]
print(dup_list)

mix_list = ["apple",123,True]
print(mix_list)

# Create Range
sq = [i**2 for i in range (10)]
print(sq)

num = list (range(1,10))
print(num)