
def add(x ,y):
    sum=x+y
    return sum

def substract(x, y):
    substra=x-y
    return substra


def multiply(x, y):
    multi=x*y
    return multi


def divide(x, y):
    divid=x/y
    return divid

menu = ""
print("*********************Select Operation.********************")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
print("*********************Select Operation.********************")
""
choice = int(input("Enter choice 1/2/3/4:"))

user_input_1 = int(input("Enter First Number :"))
user_input_2 = int(input("Enter Second Number :"))
print(menu)

while choice != 0:
    if choice == 1:
        print("You have Chosen 1  For - Adding Number")
        print("The Sum of Two Number is :",add(user_input_1,user_input_2))
        break
    elif choice == 2:
        if user_input_1 > user_input_2:
            print("You have Chosen 2  For - Substract Number")
            print("The Subtract of Two Number is :",substract(user_input_1,user_input_2))
        elif user_input_2 > user_input_1:
            print("The Subtract of Two Number is  :", substract(user_input_2, user_input_1))
        break
    elif choice == 3:
        print("You have Chosen 3  For - Multiply Number")
        print("The Multiply of Two Number is :",multiply(user_input_1,user_input_2))
        break
    elif choice == 4:
        if user_input_1 > user_input_2:
            print("You have Chosen 4  For - Dividing Number")
            print("The Divide of Two Number is :", divide(user_input_1, user_input_2))
        elif user_input_2 > user_input_1:
            print("You have Chosen 4  For - Dividing Number")
            print("The Divide of Two Number is :", divide(user_input_2, user_input_1))
        break
    else:
        print("Invalid Choice ")
        break
