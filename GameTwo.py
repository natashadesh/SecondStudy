import random
riddles_dict = {
    "I have keys but no locks. I have space but no room. You can enter but can't go outside. What am I?": "keyboard",
    "What has hands but can't clap?": "clock",
    "I'm tall when I'm young and short when I'm old. What am I?": "candle",
    "What has a face and two hands but no arms or legs?": "clock",
    "I fly without wings, I cry without eyes. Whenever I go, darkness flies. What am I?": "cloud",
    "What has a neck but no head?": "bottle",
    "I'm full of holes but still hold water. What am I?": "sponge",
    "What belongs to you but other people use it more than you do?": "name",
    "I run all around the backyard, yet I never move. What am I?": "fence",
    "What gets wetter the more it dries?": "towel",
    "I have a tail and a head but no body. What am I?": "coin",
    "What has to be broken before you can use it?": "egg",
    "I go up but never come down. What am I?": "age",
    "I'm light as a feather, yet the strongest person can't hold me for five minutes. What am I?": "breath",
    "The more of me you take, the more you leave behind. What am I?": "footsteps"
}
y = input("Hello, let's play riddles game. Are you ready? Type  " + "Y " + "or " + "N "+":  ")
for i in range(15): 
    if y.lower() == "y":
        question, answer = random.choice(list(riddles_dict.items())) 
        print(question)
        x = input("Guess the answer (write only one word, all letters are small):  ")
        if x.lower() == answer.lower():
            print("You're right! Great job! Want to play again?")
        else:
            print(f"Sorry, wrong answer. My answer was : {answer}")
        y = input("Want to play again? Type  Y or N:  ")
    else:
        print("Okay. Bye!")
        break
print ("Thank you for playing with us. See you soon.")


