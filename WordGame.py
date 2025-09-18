import random
possible_words = ["star", "book", "game", "tree", "love", "walk", "snow", "moon", "gold", "time"]

def ask_user_readiness(message:str) -> None:
    """
    Verification if user want to play.
    """
    x = input(message).lower().strip()
    if x != "y":
        print("See you next time.")
def hide_the_chosen_word(the_word):
    for letter in the_word:
        print(letter,end= " ")

print("Welcome to the game. Guess, what word I thought of.")
ask_user_readiness("Do you want to continue? Choose Y or N:  ")
computer_choice = random.choice(possible_words)
hide_the_chosen_word(computer_choice)