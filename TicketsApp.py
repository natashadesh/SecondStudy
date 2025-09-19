#!/usr/bin/env python3

"""
The ticket app shows the price for one ticket based on user's age. 
After in offers to buy tickets and counts the final price.
"""
KIDS_PRICE = 16
ADULT_PRICE = 32
SENIOR_PRICE= 25
def validate_user_input(age: str) -> bool:
    """
    Check the user input if it is in digit form.
    """
    if age.isdigit():
        return True
    else:
        print("incorrect input, please check your answer")
        return False
def ticket_price(the_age: int) -> str:
    """
    Determine the price for the ticket based on the user age.
    """
    if the_age < 14:
        return "Ticket price is $16"
    elif the_age < 60:
        return "Ticket price is $32"
    else:
        return "Ticket price is $25"
def agrement_to_buy(message: str) -> bool:
    """
    Ask for agrement to buy tickets.
    """
    if message == "y":
        return True
    else:
        print("See you next time.")
        return False
def ask_user_input(message: str) -> int:
    """
    Ask for user input and validate it.
    """
    while True:
        user_input = input(message).strip()
        if validate_user_input(user_input):
            break
    return int(user_input)
def main():
    print("Welcome to our place. We have 3 types of tickets:"
    " for our little guests, adults and seniors.")
    user_age_int = ask_user_input("Please, provide your age:  ")
    print(ticket_price(user_age_int))
    agrement_to_buy(input("Do you want to buy tickets now? Please, choose Y or N:  ").strip())
    kids_ticket= ask_user_input("Please, choose the number of kids tickets:  ")
    adults_ticket= ask_user_input("Please, choose the number of adult tickets:  ")
    seniors_ticket= ask_user_input("Please, choose the number of senior tickets:  ")
    total_price = kids_ticket * KIDS_PRICE + adults_ticket * ADULT_PRICE + seniors_ticket * SENIOR_PRICE
    print(f"Your total price is: ${total_price}")

if __name__ == "__main__":
    main()