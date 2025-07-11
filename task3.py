"""
This task aims to develop rock, paper and scissors game
"""
import random

def human_choice():
    while True:
        user_input = input("Pick your item (rock, paper, or scissors): ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Seems you didn't read the instruction: Please pick 'rock', 'paper', or 'scissors'.")

def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])



def winner(user_choice, computer_choice):
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win this round!"
    else:
        return "The computer wins this round!"



def play_game():
    user_score = 0
    computer_score = 0

    print("---")
    print("Welcome to Rock, Paper, Scissors! Let's see who's luck is working properly")
    print("---")

    while True:
        user_choice = human_choice()
        comp_choice = computer_choice()
        result = winner(user_choice, comp_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "computer wins" in result: 
            computer_score += 1

        print(f"---")
        print(f"Current Score scenario: You - {user_score} | Computer - {computer_score}")
        print(f"---")

        play_again = input("Press Y to continue the game and Press N to end the game: ").lower()
        if play_again != 'y':
            print("---")
            print("Thanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("Congratulations, you're the overall winner!")
            elif computer_score > user_score:
                print("Better luck next time! The computer won overall.")
            else:
                print("It's an overall tie! Well played!")
            print("---")
            break
play_game()