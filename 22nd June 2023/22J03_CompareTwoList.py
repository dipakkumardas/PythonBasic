# Check if two lists are identical.
# If all elements are present in the list
# len and sort - values will same


lis1 = [1, 43, 23]  # First list
lis2 = [1, 2, 3]  # Second list

if len(lis1) == len(lis2):
    lis1 = sorted(lis1)
    print("After Sorting of list 1:",lis1)
    lis2 = sorted(lis2)
    print("After Sorting of list 2:", lis2)
    if lis1 == lis2:
        print("List are identical")
    else:
        print("List are not Identical")
