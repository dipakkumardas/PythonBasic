# True is Similier to 1 and False is similar to 0
bool_val = int(True)
print(bool_val)

#String to Integer
string_num = int("10")
print(string_num)
print(type(string_num))

binary = int("1010",2) # Binary Will Base - 2
print(binary)

octal = int ("12",8)
print(octal)

hex_de = int("A",16)
print(hex_de)

ran_val = int("@!24") # ValueError: invalid literal for int() with base 10: '@!24'
print(ran_val)