num = int(input("Enter a int Number :"))
print("You Have entered a number ->",str(num))

match num:
    case 0:
        print("You have entered 0")
    case num if num > 0:
        print("You have entered +ve number")
    case num if num < 0:
        print("You Have Entered -ve number")
    case _:
        print('No Idea')