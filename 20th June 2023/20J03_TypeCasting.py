num1 = int(input("Enter a Number :"))
num2 = int(input ("Enter second Number :"))
r = num1 + num2
print("The Total Number is :",r) # if we use comma the conversion was not required
print ("The Total Value is :"+str(r)) # In Print is string so we need to convert int to string

#int + int = ok
#int + str = not ok
#str +str = ok

bool_val = str(True)
print(bool_val)