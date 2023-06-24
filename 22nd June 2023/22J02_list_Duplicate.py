# Remove Duplicate from the list

my_list = [33, 23,23,44,56]
non_dup = []

# non_dup = [33, 23, 44, 56]

# Normal Logic
# Go through the all items if item is present in the list, add to new non_dup_list
for i in my_list:
    if i not in non_dup:
        non_dup.append(i)
print(non_dup)

#Set Function
print("This is the List with duplicate value :", my_list)
non_dup2 = list(set(my_list))
print("This is the list  after removing duplicate value :",non_dup2)
