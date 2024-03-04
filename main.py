import random
from game_data import data
from art import logo, vs

still_playing = True
while still_playing:
    print(logo)
    print("Welcome to the Higher or Lower Game!")
    print("Your aim is to bet the correct answer.")
    print("You will compare the amount of followers on Instagram of famous people.")
    print("\n")
    still_guessing = True
    score = 0
    position2 = random.choice(data)
    while still_guessing:
        position1 = position2
        position2 = random.choice(data)
        print("Which of this has more Insta followers?")
        print(f"The {position1['name']} which is {position1['description']} from {position1['country']}")
        print(vs)
        print(f"The {position2['name']} which is {position2['description']} from {position2['country']}")
        # input the guess
        bet = input("Make a bet. 'A' for first position, 'B' for second: ".lower())
        # compare the followers
        if position1["follower_count"] > position2["follower_count"]:
            winner = "a"
        else:
            winner = "b"
        # make score variable and rules to score
        if bet == winner:
            print("You proceed to the next round.")
            score += 1
        else:
            still_guessing = False
        print("\n")
        print("You lose!")
        print(f"Your score is {score}")
    another_round = input("Do You want to play another round? type 'y' or 'n': ")
    if another_round == 'n':
        still_playing = False
