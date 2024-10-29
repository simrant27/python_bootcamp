import random
from art import logo, vs

from game_data import data

print(logo)


#function to Get the random value from game_data
def get_value():
    data_fetched= random.choice(data)
    # print(f"{data_fetched['name']}, a {data_fetched['description']}, from {data_fetched['country']}.")
    return data_fetched

def print_description(insta_user):
    return f"{insta_user['name']}, a {insta_user['description']}, from {insta_user['country']}."

#function to compare to value and return the highest
def compare(user_1, user_2):
    if user_1['follower_count'] > user_2['follower_count']:
        return "A"
    else:
        return "B"

# start the game


def game():
    player_1 = get_value()
    continue_play = True
    score = 0
    while continue_play:
        player_2 = get_value()
        if player_1 == player_2:
            player_2 = get_value()
        print(f"Compare A: {print_description(player_1)}")
        print(vs)
        print(f"Against B: {print_description(player_2)}")
        ans = input("Who has more followers, type A or B? ").upper()

        print("\n" * 20)
        print(logo)

        if compare(player_1,player_2) == ans:
            score +=1
            print(f"You are right!, Current score: {score}")
            continue_play = True
            player_1 = player_2

        else:
            # print("\n" * 30)
            print(f"Sorry that's wrong, Final score:{score}")
            continue_play = False

game()



