#Creating a String Tuple and String Both are IMMUTABLE when String value is same at that time it's refer same memory location
# If I chnage the String then only it's update the Memory Id
name_1 = "Varun"
name_2 = "Varun"
name_3 = "Varun1"
print("id of name_1 = ", id(name_1))
print("id of name_2 = ", id(name_2))
print("id of name_2 = ", id(name_3))
print("Both d value of name is same ")