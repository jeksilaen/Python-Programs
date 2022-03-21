print("Welcome to my mini-game quiz !")

score = 0
question = ["Whats CPU stands for?", "Whats GPU stands for?", "Whats RAM stands for?"]
answers = ["Central Processing Unit", "Graphic Processing Unit", "Random App Memory"]
temp = 0

playing = input("Do you want to play? ").lower()

if playing.lower() != "yes":
    print("Ok bye :(")
    quit()

print("Okay, lets play!")

for que in question:
    answer = input(f"{que} ")
    if answer != answers[temp].lower():
        print("Incorrect")
        temp = temp + 1
    else:
        print("Correct !")
        temp = temp + 1
        score = score + 1

print(f"Your score total is {score} / {len(question)}")
print(f"Congratulations you got {int(score/len(question)*100)} %")
