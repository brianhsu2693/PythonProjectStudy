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

import random
data = [rock, paper, scissors]

ask_user = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))
if ask_user in [0, 1, 2]:
    user = data[ask_user]
    print(f'you：{user}')
else:
    print('Input errors, please re-enter')
    exit()

npc = random.choice(data)
print(f'npc；{npc}')

if user == npc:
    print('It is a draw')
elif user == rock and npc == scissors:
    print('you win')
elif user == paper and npc == rock:
    print('you win')
elif user == scissors and npc ==paper:
    print('you win')
else:
    print('you lose')