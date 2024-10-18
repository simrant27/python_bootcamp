import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def is_black_jack(user_card, computer_card):
    if ({10,11}).issubset(computer_card):
        print(computer_card)
        print("You lose 1")
        return True

    elif ({10,11}).issubset(user_card):
        print(f"{user_card} hehe")
        print("You win 2")
        return True
    else:
        return False
#
def game_end(user_card):
    print(user_card)
    if sum(user_card)> 21:
        if 11 in user_card:
            index = user_card.index(11)
            user_card[index] = 1
            if sum(user_card) > 21:
                print(f"{user_card} greater than 21")

                return True
            else:
                return False
        else:
            print(f"{user_card} greater than 21.")


            return True
    else:
        return False

choice_to_play = input("Do you want to play a game of Blackjack? Type 'y or 'n: ").lower()
user_card = [random.choice(cards), random.choice(cards)]
computer_card = [random.choice(cards), random.choice(cards)]

# total_computer = 0
# total_user = 0
while choice_to_play == "y":

    total_user = sum(user_card)
    total_computer = sum(computer_card)

    print(f"Your cards:{user_card}, current score:{total_user}")
    print(f"Computer's first card:{computer_card[0]}")
    if len(user_card) == 2:
        if is_black_jack(user_card,computer_card):
            print("Game over 3")
            exit()

    if game_end(user_card):
        print("You lose")
        print("Game end 4")
        exit()
    choice_to_play = input("Type 'y' to get another card, type 'n' to pass: ")
    if choice_to_play == "y":
        user_card.append(random.choice(cards))
    else:
        print("here")
        print(total_computer)
        while total_computer < 17:

            computer_card.append(random.choice(cards))
            total_computer = sum(computer_card)
        if sum(computer_card) > 21:
            print(f"{computer_card} {sum(computer_card)} is greater than 21")

            print("You win 5")
        else:
            print(f"{user_card} Your total: {total_user}")
            print(f"{computer_card} computer total: {total_computer}")
            if total_user > total_computer:
                print("You win 6")
            elif total_user < total_computer:
                print("you lose 7")
            else:
                print("Draw")

