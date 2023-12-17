import random

#  the choice from the user
def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in choices:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
  #  determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

#  game function
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)


if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    play_again = 'yes'
    while play_again.lower() == 'yes':
        play_game()
        play_again = input("Do you want to play again? (yes/no): ")
    print("Thanks for playing!")
