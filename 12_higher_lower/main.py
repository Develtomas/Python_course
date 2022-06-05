from random import choice
from replit import clear
from game_data import data
import art

#functions
def get_rand_data():
  """get rand data for A"""
  return choice(data)

def format_str(dt):
  """string out"""
  return f"{dt['name']}, a {dt['description']}, from {dt['country']}"

def compare(var,a,b):
  """compare a and b followers"""
  if var == 'a' and (a['follower_count'] > b['follower_count']):
    return [True, 'a']
  elif var == 'b' and (a['follower_count'] < b['follower_count']):
    return [True,'b']
  else:
    return [False]

def main_game():
  """main logic"""
  points = 0
  game = True
  dataA = get_rand_data()
  
  while game:
    dataB = get_rand_data()
    # check same
    while dataB == dataA:
      dataB = get_rand_data()
    strA = format_str(dataA)
    strB = format_str(dataB)
    
    print(art.logo)
    print(f'You have {points} scores')
    print(f'variant A: {strA}')
    print(art.vs)
    print(f'variant B: {strB}')
    
    choise = str(input('Which is more popular A\B: ')).lower()
    # compare result
    res = compare(choise, dataA, dataB)
  
    if res[0]:
      points +=1
      if res[1] == 'b':
        dataA = dataB
      clear()
    else:
      clear()
      print(art.logo)
      print(f'Game over. You got {points} scores.')
      game = False

# init
main_game()