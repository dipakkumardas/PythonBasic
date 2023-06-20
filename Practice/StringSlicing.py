# Python program to demonstrate
# string slicing

# String Slicing
my_string = "123456789"
print(my_string[0]) # Print First Char

print(my_string[0:4]) # Print First 3 char  [0, n-1]  # output This

print("The Length of My String is :",len(my_string))

print(my_string[0:7:2])
# Start from 0 , then Akip 2 ,

my_string2 = "123456789"
print(my_string2[1:7:1])

print(my_string2[0:4:2])
print("The Length of My String :",len(my_string2))
print(my_string2[7:5:-1])

# Split of string

print(my_string2[0:5])

print(my_string2[::-1])