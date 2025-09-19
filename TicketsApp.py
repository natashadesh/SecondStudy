kids_price = int(16) 
adult_price = int(32)
senior_price = int(25)
def validate_user_input(age: str) -> bool:
    """
    Check the user input if it is in digit form.
    """
    if age.isdigit():
        return True
    else:
        print("incorrect input, please check your answer")
        return False
def ticket_price(the_age):
    """
    Determine the price for the ticket based on the user age.
    """
    if the_age < 14:
        return("Ticket price is $16")
    elif the_age < 60:
        return("Ticket price is $32")
    else:
        return("Ticket price is $25")    

def agrement_to_buy(message: str) -> bool:
    if message == "y":
        return True
    else:
        print("See you next time.")
        return False
    
def collecting_user_information(message_2: int) -> int:
    """
    Collecting information - how many tickets the user chose.
    """
    while True:
        ticket_number = message_2
        if validate_user_input(ticket_number):
            break
        print(f"Tickets numbers:  {ticket_number}")
        return ticket_number
    
def user_ticket_number_input(message_3):
    """
    Requst for user to input tickets number.
    """
    z = input(f"Please, choose the number of {message_3}:  ").strip()
    return z


print("Welcome to our place. We have 3 types of tickets:"
" for our little guests, adults and seniors.")
while True:
    user_age = input("Please, provide your age:  ").strip()
    if validate_user_input(user_age):
        break
user_age_int = int(user_age)
one_ticket_price = ticket_price(user_age_int)
print(one_ticket_price)
agrement_to_buy(input("Do you want to buy tickets now? Please, choose Y or N:  ").strip())

kids_tickets = user_ticket_number_input("kids tickets")
a = collecting_user_information(kids_tickets)
adult_tickets = user_ticket_number_input("adult tickets")
b = collecting_user_information(adult_tickets)
senior_tickets = user_ticket_number_input("senior tickets")
c = collecting_user_information(senior_tickets)
total_price = a * kids_price + b * adult_price + c * senior_price
print(f"Your total price is: {total_price}")
