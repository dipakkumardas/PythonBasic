# Enter Input From the User
input_string = (input("Enter Number of a list separated by space: "))
number_list = input_string.split()

# print List
print('list:',number_list)

# convert each item to Interger Type
for i in range(len(number_list)):
    # convert each type o int type
    number_list[i] = int(number_list[i])

print("Maximum of Inputter no:",max(number_list))
print("Minimum of Inputted No :",min(number_list))
print("Sum of all List Number :",sum(number_list))

# Declare Multipication List
multiplied = []
for number in number_list:
    multiplied.append(number*2)
print("Multiply of the List :",multiplied)







