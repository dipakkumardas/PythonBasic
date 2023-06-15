user_input_1 = int(input("Enter Num 1 :"))
user_input_2 = int(input("Enter Num 2:"))

def multiply(n1 ,n2):
    return n1*n2

def adding(n1,n2):
    return n1+n2

def substract(n1,n2):
    return n1-n2

result1 = multiply(user_input_1,user_input_2)
result2 = adding(user_input_1,user_input_2)
result3 = substract(user_input_1,user_input_2)

print("The Multiply Value of two Number is",result1)
print("The Adding Value of two Number is",result2)
print("The substract Value of two Number is",result3)