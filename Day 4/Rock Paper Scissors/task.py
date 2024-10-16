import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#
# def choice_done(input_received):
#
#     if input_received == 0:
#         print(rock)
#     elif input_received== 1:
#         print(paper)
#     elif input_received== 2:
#         print(scissors)
#     else:
#         print("Invalid input")
#         exit()

game_choice = [rock, paper, scissors]

input_by_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper abd 2 for Scissors\n"))
if input_by_user >= 3 or input_by_user < 0:
    print("Invalid input, You lose")
    exit()
print(game_choice[input_by_user])
computer_choice = random.randint(0,2)

# choice_done(input_by_user)

print(f"Computer chose: {game_choice[computer_choice]}")

# choice_done(computer_choice)

if input_by_user == 0 and computer_choice == 2:
    print("You win")
elif input_by_user == 2 and computer_choice == 0:
    print("You lose")
elif input_by_user < computer_choice:
    print("You lose")
elif input_by_user == computer_choice:
    print("draw")
else:
    print("You win")



