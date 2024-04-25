import random

def rock_paper_scissors():
    # Define the choices
    choices = ["rock", "paper", "scissors"]
    
    # Initialize scores
    user_score = 0
    computer_score = 0
    
    # Game loop
    while True:
        # Prompt the user for their choice
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        
        # Validate user input
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        # Generate a random choice for the computer
        computer_choice = random.choice(choices)
        
        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            user_score += 1
            result = "You win!"
        else:
            computer_score += 1
            result = "You lose!"
        
        # Display the result
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        print(result)
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        
        # Ask the user if they want to play another round
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

# Call the game function
rock_paper_scissors()
