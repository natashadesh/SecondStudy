import random

POSSIBLE_CHOICES = ["paper", "scissors", "rock"]
MAX_GAME_NUMBER = 50
P1_WIN_DICT = {
    "paperrock": True ,"paperscissors": False,
    "rockpaper": False,"rockscissors": True,
    "scissorsrock": False,"scissorspaper": True
} 

def agree_for_game(message: str) -> None:
    """
    Verify if user agree to play
    """
    answer = input(message).lower().strip()
    if answer != "y":
        print("See you soon!")
        exit()

def get_the_user_choice() -> str:
    """
    Identify and verify user choice
    """
    while True:
        choice = input("So, rock, paper or scissors: Choose one:  ").lower().strip()
        if choice in POSSIBLE_CHOICES:
            print("Your choice is:  ", choice)
            return choice
        print(f"Your input is incorrect, correct input are {", ".join(POSSIBLE_CHOICES)}")

print("Let's play well-known old game. Try to win me.")
agree_for_game("Do you want to play? Choose Y or N:  ")
for game in range(MAX_GAME_NUMBER):
    user_choice = get_the_user_choice()
    computer_choice = random.choice(POSSIBLE_CHOICES)
    print("My choice is:  ", computer_choice)
    game_combination = user_choice + computer_choice
    if user_choice == computer_choice:
        print("Wow! We think alike. We have a draw.")
    else:
        if P1_WIN_DICT[game_combination] is True:
            print("Congratulations! You're a winner!")
        else:
            print("Ha-ha! I won! But you can try again to beat me.")
    agree_for_game("Do you want to play again? Choose Y or N:  ")

print("Thank you for the game! See you soon.")