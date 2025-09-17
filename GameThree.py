import random

possible_choices = ["paper", "scissors", "rock"]
player1_win_dict = {
    "paperrock": True ,"paperscissors": False,
    "rockpaper": False,"rockscissors": True,
    "scissorsrock": False,"scissorspaper": True
} 

def check_user_input(user_input: str) -> bool:
    if user_input in possible_choices:
        print("Great, your choice is: ", user_input, ". Let's see what I will choose.")
        return True
    return False

# Might be a function 1
agree_for_game = input( "Do you want to play today? Choose: Y or N:  ").lower().strip()
if agree_for_game != "y":
    print("Okay, Bye!")
    exit()
###

print("Let's play well-known old game. Try to win me.")
for i in range (50):
    # Migth be a function
    while True:
        user_choice = input("So, rock, paper or scissors: Choose one:  ").lower().strip()
        if check_user_input(user_choice):
            break
        else:
            print("Input is incorrect, try again.")
    ####

    computer_choice = random.choice(possible_choices)
    print("My choice is:  ", computer_choice)
    game_combination = user_choice + computer_choice

    # Might be a function
    if user_choice == computer_choice:
        print("Wow! We think alike. We have a draw.")
    else:
        if player1_win_dict[game_combination] is True:
            print("Congratulations! You're a winner!")
        else:
            print("Ha-ha! I won! But you can try again to beat me.")
    ####

    # Might be a reuse of the fuctioin 1 see line 16
    agree_for_game = input("Do you want to play again? Choose Y or N:  ").lower().strip()
    if agree_for_game != 'y':
        print("Okay, Bye!")
        break
    ##
    
print("Thank you for the game! See you soon.")