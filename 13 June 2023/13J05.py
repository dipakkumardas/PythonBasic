# Lucky no with 3 tries
# 0 to 10
import random
lucky_no = random.randint(1,10)
no_tries = 3
guess_no = None

while guess_no != lucky_no:
    guess_no = int(input("Enter the number 1 to 10 :"))
    if guess_no < lucky_no:
        print("Too Low")
    elif guess_no > lucky_no:
        print("Too High")
print("Found the Lucky Number :"+str(lucky_no))


