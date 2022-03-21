import random

user_score = 0
computer_score = 0

x = ["rock", "paper", "scissors"]

while True:
    user = input("Rock/Paper/Scissors? : ").lower()
    if user not in x:
        print("Wrong input!")
        continue

    computer = x[random.randrange(0, len(x))]

    if user == computer:
        print(f"{user.capitalize()} vs {computer.capitalize()}")
        print("Tie!")

    elif user == "rock" and computer == "scissors":
        print(f"{user.capitalize()} vs {computer.capitalize()}")
        print("You win!")
        user_score += 1

    elif computer == "scissors" and user == "paper":
        print(f"{user.capitalize()} vs {computer.capitalize()}")
        print("You win!")
        user_score += 1

    elif user == "paper" and computer == "rock":
        print(f"{user.capitalize()} vs {computer.capitalize()}")
        print("You win!")
        user_score += 1

    else:
        print(f"{user.capitalize()} vs {computer.capitalize()}")
        print("You lose!")
        computer_score += 1

    if user_score == 3 or computer_score == 3:
        if user_score > computer_score:
            print(f"Congratulation! you won with {user_score} to {computer_score}")
            quit()
        else:
            print(f"Too bad! you lose with {user_score} to {computer_score}")
            quit()
