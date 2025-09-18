import random
possible_words = ["star", "book", "game", "tree", "love", "walk", "snow", "moon", "gold", "time"]

#[('g', False), ('o', False)]
def ask_user_readiness(message:str) -> None:
    """
    Verification if user want to play.
    """
    x = input(message).lower().strip()
    if x != "y":
        print("See you next time.")

#def hide_the_chosen_word(the_word:str) ->bool:
 #   guessed = [False]*len(the_word)
#    print(guessed)

#def reveal_the_word(hidden_word):

#def check_user_letters(the_letter):
#    the_letter != chosen_word:
 #   print("this is a wrong letter")


print("Welcome to the game. Guess, what word I thought of.")
ask_user_readiness("Do you want to continue? Choose Y or N:  ")
computer_choice = random.choice(possible_words)
word_state = convert_word_to_game_state(computer_choice)
for attempt in range(10):
    user_choice = get_user_choice()
    check_user_choice(word_state, user_choice)
    show_game_state_to_user(word_state)
user_win = check_if_user_win(word_state)
if user_win:
    print()
else:
    print()