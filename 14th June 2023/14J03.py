# Write  a program
#If user enter positive or negative number
print("Start of the program, outside the loop")

name = "Dipak"

match name :
    case "Dipak":
        print("This is Dipak")
    case "Deepak":
        print("Deepak")
    case _:
        print("No Match, default")

print("End of the program, outside the loop")
