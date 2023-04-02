import random

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Choose rock, paper, or scissors (or quit to exit): ")

    if user_choice == "quit":
        break

    elif user_choice not in options:
        print("Invalid choice. Choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(options)

    print(f"You chose {user_choice}. The computer chose {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose. Try again.")
