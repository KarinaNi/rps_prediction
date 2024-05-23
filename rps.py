import random

POSSIBLE_CHOICES = ["rock", "paper", "scissors"]

# Function to determine the winner
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

# Function to create transition matrix from markov chain
def create_transition_matrix(user_input):
    transition_matrix = np.zeroes(3,3)
    name_to_number = {"rock":0, "paper":1, "scissors":2}
    for i, ele in enumerate(user_input):
        if i != len(user_input)-1:
            current_choice = name_to_number[ele]
            next_choice = name_to_number[user_input[i+1]]
            transition_matrix[current_choice][next_choice] += 1
    row_sum = np.sum(transition_matrix, axis = 1)
    transition_matrix = transition_matrix/row_sum
    return transition_matrix
    
# To check if the user actually put good input
def validate_input(user_input):
    while user_input.lower() not in POSSIBLE_CHOICES:
        print("Please choose a valid option (rock, paper, or scissors).")
        user_input = input("Rock, Paper, or Scissors: ")
    return user_input.lower()

# Continously ask data, call learning method, and test if it got right
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
    print("Please wait few minutes while I can learn..")
    

play_game()
