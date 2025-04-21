import random

you = int(input("Enter what you take\n 1 for Snake\n 2 for Water\n 3 for Gun\nWhat you take: "))
youdict = {1: "Snake", 2: "Water", 3: "Gun"}

if you in youdict:
    print(f"You have taken: {you} ({youdict[you]})")
    
    computer = random.choice([1, 2, 3])
    print(f"Computer has taken: {computer} ({youdict[computer]})")

    if you == computer:
        print("It's a draw ;/ \nShit you both picked the same thing! \nAre you cheating?")
    # Winning conditions
    elif (you == 1 and computer == 2) or (you == 2 and computer == 3) or (you == 3 and computer == 1):
        print("You Won!!! :)")
        if you == 1:
            print("Snake drinks the Water :)")
        elif you == 2:
            print("Water ruins the Gun :0")
        else:
            print("Gun kills the Snake, you're safe now!")
    else:
        print("You Lose!! :/")
        if you == 1:
            print("Snake is killed by the Gun!!!")
        elif you == 2:
            print("Snake drank your Water!!")
        else:
            print("You can't kill Water!!")
else:
    print(f"Something went wrong :/\nYou entered the wrong number!!! {you}")
