#  How to check the list is empty
my_list = []
non_list = [2, 3, 4, 5, 6]



def check_list(temp_list):
    if len(temp_list) == 0:
        print("List is empty ")
    else:
        print("list is not empty")


check_list(my_list)
check_list(non_list)
