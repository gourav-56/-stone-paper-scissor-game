from random import randint

t = ["stone", "paper", "scissor"]

while True:
    computer = t[randint(0, 2)]
    player = input("stone, paper, scissor? (or 'exit'): ").lower()

    if player == "exit":
        print("Game Over")
        break

    if player not in t:
        print("Invalid input")
        continue

    if player == computer:
        print("Tie!")
    elif player == "stone":
        if computer == "paper":
            print("You lose! Computer chose", computer)
        else:
            print("You win!")
    elif player == "paper":
        if computer == "scissor":
            print("You lose! Computer chose", computer)
        else:
            print("You win!")
    elif player == "scissor":
        if computer == "stone":
            print("You lose! Computer chose", computer)
        else:
            print("You win!")