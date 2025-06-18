


import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    return "computer"

def main():
    user_score = 0
    computer_score = 0
    while True:
        print("\nRock Paper Scissors Game")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == "4":
            print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")
            break
        elif choice not in ["1", "2", "3"]:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue
        choices = ["rock", "paper", "scissors"]
        user_choice = choices[int(choice) - 1]
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        winner = determine_winner(user_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")
            break

if __name__ == "__main__":
    main()
