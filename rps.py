import random

POSSIBLE_CHOICES = ["rock", "paper", "scissors"]

def rps(user_choice, computer_choice):
    if user_choice == computer_choice:
        return f"It's a Draw! You both chose {computer_choice}."
    
    if (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return f"User wins! Computer chose {computer_choice}."
    else:
        return f"Computer wins! Computer chose {computer_choice}."

def validate_input(user_input):
    while user_input.lower() not in POSSIBLE_CHOICES:
        print("Please choose a valid option (rock, paper, or scissors).")
        user_input = input("Rock, Paper, or Scissors: ")
    return user_input.lower()

def play_game():
    input_data = []
    
    while len(input_data) < 20:
        user_input = input("Rock, Paper, or Scissors: ")
        user_choice = validate_input(user_input)
        computer_choice = random.choice(POSSIBLE_CHOICES)
        
        input_data.append(user_choice)
        print(rps(user_choice, computer_choice))
    
    print("Your inputs so far are:")
    print(input_data)

play_game()