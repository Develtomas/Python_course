############### Blackjack Project #####################
import random
from art import logo
from replit import clear

#variables
DECK = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#functions
def deal_card(list):
  """Take a card from deck"""
  return random.choice(DECK)

def restart():
  """Begin/restart game"""
  begin = input("\nDo you want to play a Blackjack game? y/n: ")
  if begin == 'y':
    clear()
    print(logo)
    us_ca = []
    ai_ca = []
    for _ in range(2):
      us_ca.append(deal_card(DECK))
      ai_ca.append(deal_card(DECK))
    check_winner(us_ca, ai_ca)

def score_calc(cards):
  """score counting"""
  res = sum(cards)
  if res == 21:
    return 1
  elif res > 21:
    if 11 in cards:
      cards.remove(11)
      cards.append(1)
      score_calc(cards)
    else: return 0
  else: return res

def score_calc_ai(cards):
  """score counting for AI turn"""
  res = sum(cards)
  if res > 21 and (11 in cards):
    cards.remove(11)
    cards.append(1)

def compare(user, ai):
  """comparing results if not blackjack"""
  if sum(ai) > 21:
    print(f" Your final cards: {user},\n AI cards: {ai},\n AI overrun {sum(ai)} - you WIN!!")
    restart()
  elif sum(user) > sum(ai):
    print(f" Your final cards: {user},\n AI cards: {ai},\n AI have {sum(ai)} points,\n You have {sum(user)} - you WIN!!")
    restart()
  elif sum(user) < sum(ai):
    print(f" Your final cards: {user},\n AI cards: {ai},\n AI have {sum(ai)} points,\n You have {sum(user)} - you LOSE!!")
    restart()
  else:
    print(f" AI have {sum(ai)} points,\n You have {sum(user)} - DRAW!!")
    restart()
    
def ai_play(us,ai):
  """AI turn"""
  score_calc_ai(ai)
  if sum(ai) < 17:
    ai.append(deal_card(DECK))
    ai_play(us,ai)
  else:
    compare(us,ai)
    
def check_winner(user_c, ai_c):
  """main logic"""
  if score_calc(user_c) == 1:
    if score_calc(ai_c) == 1:
      print("Both players has 21 points, NO winner - DRAW!")
      restart()
    else: 
      print(f"Your cards: {user_c},\n computer cards: {ai_c},\n you have {sum(user_c)} points - BLACKJACK!!")
      restart()
  elif score_calc(ai_c) == 1:
    print(f"Your cards: {user_c},\n computer cards: {ai_c},\n AI have {sum(ai_c)} points you LOSE!!")
    restart()
  elif score_calc(user_c) == 0:
    print(f" Your cards: {user_c},\n computer cards: {ai_c},\n you have {sum(user_c)} points - went over, you LOSE!!")
    restart()
  else:
    print(f" Your cards: {user_c},\n Computer card: [{ai_c[0]}],\n You have {sum(user_c)} point")
    more = input("Take one more card y/n: ")
    if more == 'y':
      user_c.append(deal_card(DECK))
      check_winner(user_c, ai_c)
    else:
      print("AI is taking cards...")
      ai_play(user_c, ai_c)

#init program
restart()









