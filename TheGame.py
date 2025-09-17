import random
numbers = [1,2,3,4,5,6,7,8,9]
x = random.choice(numbers)
for attempt in ["3 attempts", "2 attempts", "1 attempt"]:
    print(f"Your have {attempt} left") 
    y = input("Guess which number I chose from 1 to 9. Your number is: ")
    y = int(y)
    if y == x:
       print("congratulations! You won")
       break
    else:
        if attempt == "1 attempt":
            print(f"Sorry, you lose. My number was: {x}")
        else:
            print(f"nope, you're wrong, try again.")
