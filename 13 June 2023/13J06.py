'''
Please Choose Your Option:
1. Say Hello
2. Do Nothing
3. Quit
'''

choice = ''
while choice != '3':
    print("1. Say Hello \n 2.Do Nothing \n 3.Quit")
    choice = input("Choice 1 -3 :")
    if choice == '1':
        print("Say Hello")
    elif choice == '2':
       print("Do Nothing")
    elif choice == '3':
        print("Quit")
        break
    else:
        print("Invalid Option")
print("End")
