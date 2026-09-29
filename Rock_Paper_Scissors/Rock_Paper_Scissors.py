# Rock Paper Scissors

# Import random + define art choices
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

rps = [rock, paper, scissors]

# Step 1: Get the user input and display their choice
user_input = int(input('What do you choose? Type "0" for Rock, "1" for Paper or "2" for Scissors.\n'))

if user_input >= 0 and user_input <= 2:
    print(rps[user_input])

# Step 2: Generate a random computer choice and display it
computer_choice = random.randint(0, 2)
print("The computer chose:")
print(rps[computer_choice])

# Step 3: Determine the winner
if user_input >= 3 or user_input < 0:
    print("You typed an invalid option, try again!")

elif user_input == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_input == 2:
    print("You lose!")

elif computer_choice > user_input:
    print("You lose!")
elif computer_choice < user_input:
    print("You win!")
elif computer_choice == user_input:
    print("You draw!")