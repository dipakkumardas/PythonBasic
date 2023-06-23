def square_me(a):
    return pow(2,a)

numbers = [2,3,4]
result = list(map(square_me,numbers))
print(result)     # It will Print Map Object
print(type(result))

for i in result:
    print("Smart For Loop:",i)
# or I can do below

r = []
for i in numbers:
    temp = square_me(i)
    r.append(temp)

print ("For Loop Printing Value :", r)



