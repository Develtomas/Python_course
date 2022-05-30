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

#Write your code below this line 👇
import random as r
list = [rock, paper, scissors]

# Your turn
# Check correct enter
while True:
  pl_turn = int(input('Type 0 for Rock, 1 for paper, 2 for scissors\n'))
  if pl_turn in [0,1,2]:
    break
  else:
    print('wrong number!')
# Graphics    
print(list[pl_turn])

# Pc turn
print('Computer choise:')
ai_turn = r.randint(0,2)
print(list[ai_turn])

# Logic
if pl_turn == 0:
  if ai_turn == 0:
    print('draw')
  elif ai_turn == 1:
    print('pc win')
  else:
    print('you win')
elif pl_turn == 1:
  if ai_turn == 0:
    print('you win')
  elif ai_turn == 1:
    print('draw')
  else:
    print('pc win')
elif pl_turn == 2:
  if ai_turn == 0:
    print('pc win')
  elif ai_turn == 1:
    print('you win')
  else:
    print('draw')