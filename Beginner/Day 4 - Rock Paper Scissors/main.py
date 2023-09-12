# Project Day 4 : Paper, Rock, Scissors

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

#Write your code below this line :
print("*---------------------*")
str_list = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(str_list[user_choice])

print("Computer choice : ")
# Computer side choice
computer_choice = random.randint(0,2)
print(str_list[computer_choice])

if (user_choice == 0):
    if(computer_choice == 1):
        print("You lose")
    elif(computer_choice == 2):
        print("You win")
    else:
        print("Draw")
elif (user_choice == 1):
    if(computer_choice == 0):
        print("You win")
    elif(computer_choice == 2):
        print("You lose")
    else:
        print("Draw")
elif (user_choice == 2):
    if(computer_choice == 0):
        print("You lose")
    elif(computer_choice == 1):
        print("You win")
    else:
        print("Draw")
else:
    print("Not alowed value! Attempt of hacking...")

print("*---------------------*")



