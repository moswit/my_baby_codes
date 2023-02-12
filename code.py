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

user_selection = int(input( "what do you choose?\nType 0 for rock, 1 for paper, 2  for scissors:\n"))


images = [rock, paper, scissors]

if user_selection>=3 or user_selection<0:
  print("You chose incorrect number, you fucked up!!!")
else:
  print(images[user_selection])

comp_selection = random.randint(0,2)

print(images[comp_selection])


if comp_selection == 2 and user_selection == 0:
  print("You win")
elif comp_selection > user_selection:
  print("You lost")
elif user_selection == 2 and comp_selection ==0:
  print("You lost")
elif user_selection > comp_selection:
  print("You win")
elif user_selection == comp_selection:
  print("Draw")
