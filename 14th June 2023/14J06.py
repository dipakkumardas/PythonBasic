password = input("Enter Password:")

match password:
    case password if len(password) < 6:
        print("Too short !! It is a Weak password !!!!")
    case password if password.isnumeric():
        print("Weak Password !! Only Numeric!!")
    case password if password.islower():
        print("Weak Password !! Lower case only!!")
    case password if password.isupper():
        print("Weak Password !! Upper case only!!")
    case _:
        print("Strong Password !!")


