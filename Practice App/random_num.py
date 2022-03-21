import random

answer = random.randint(1, 10)
attempt = 0

print("Welcome to my guessing number challenge!")
try:
    while True:
        user_input = int(input("Guess a number from 1 - 10 : "))
        if user_input > answer:
            print("You are above the number!")
            attempt += 1
        elif user_input == answer:
            print("You got it !")
            attempt += 1
            break
        else:
            print("You are below the number!")
            attempt += 1
    print(f"Congratulation! You got it in {attempt} tries.")

except ValueError:
    print("Wrong input!")

