# String Operation
name = input("Enter Your name :")
age = input("Enter Your Age : ")
print(" ----- Formatting 1----")
print(f"Hello,{name}. Your Age is :{age} ")     # f means Formatting , Without f the value is not printing.
print("-----Formatting 2------")
print("Hello,{}. Your age is :{}".format(name, age))
print("-------Formatting 3------")
print("Hello, %s, Your Age is :%s" %(name,age))

print("# String Concatination 1")
print("Hello" + str(31))
print("# String Concatination 2")
print(int("31") +10)