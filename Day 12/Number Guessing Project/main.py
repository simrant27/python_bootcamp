import  random
from  art import logo
EASY_LEVEL_ATTEMPT = 10
HARD_LEVEL_ATTEMPT = 5

def check(guessed, number_picked):
    if number_picked == guessed:
        return True
    elif number_picked > guessed:
        print("Too low")
        return False
    else:
        print("Too high")
        return False

print(logo)
def game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard':")
    number_picked = random.choice(range(101))
    # print(number_picked)

    attempt = 0
    if level == "easy":
        attempt = EASY_LEVEL_ATTEMPT
    elif level == "hard":
        attempt = HARD_LEVEL_ATTEMPT
    else:
        print("error")


    # for i in range(attempt,0,-1):
    while attempt > 0:
            print(f"You have {attempt} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if check(guess, number_picked):
                print(f"You got it! The answer was {number_picked}")
                return
            else:
                attempt -= 1

    print("You've run out of guesses, you lose")

game()





