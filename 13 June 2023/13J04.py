print("start")
while True:
    user_input = input("Please Enter a number 0 to 10, If You match My Number I will exit")
    print("You have entered the :"+user_input)
    user_input = int(user_input)
    # exit from Infinite Loop
    if user_input == 5:
        print("You Found the Lucky Number")
        break
    print("end")

