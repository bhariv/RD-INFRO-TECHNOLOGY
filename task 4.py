import random
options = ("rock", "paper", "scissors")
running = True
while running:

    player = None
    computer = random.choice(options)

    win_conditions = {
        "rock" : "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    while player not in options:
        player = input("Enter a choice(rock, paper, scissors): ").lower()
        if player not in options:
            print("Invalid choice.Please try again.")



    print(f"player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif win_conditions[player] == computer:
        print("You Win!")
    else:
        print("You lose!")

    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        running = False

print("Thanks for playing!")

