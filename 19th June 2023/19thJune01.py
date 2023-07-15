# final_result = lambda num: num * 3
# print(final_result(9))

user_input = input("Enter Number to Multiple :")
user_input = int(user_input)


# def power_by_2(num):
#     return pow(2, num)
#
#
# result = power_by_2(user_input)
# print(result)

result = lambda num: pow(2, num)
print(result(user_input))