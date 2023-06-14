# Substring
if "x" in "xyz" :
    print(True)

    string = input("Enter String:")
    subString = "D"

    match string:
        case string if subString in string:
            print("Present")
        case _:
            print("Not Present")
