import random
from game_data import data
from art import logo, vs

account_b = random.choice(data)
score = 0
game_should_continue = True
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_b == account_a:
        account_b = random.choice(data)

    def format_data(account):
        account_name = account["name"]
        account_desc = account["description"]
        account_country = account["country"]
        return f"{account_name} a {account_desc} from {account_country}"

    def check_answer(guess, a_followers, b_followers):
        if a_followers > b_followers:
            return guess == "a"
        else:
            return guess == "b"

    print(logo)

    print(f"Compare A: {format_data(account_a)} ")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ".lower())

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    print(logo)
    if is_correct:
        print(f"You are right!! The current score is {score}")
        score += 1
    else:
        print(f"Thats wrong, Your final score is {score}")
        game_should_continue = False
    