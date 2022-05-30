from replit import clear
#HINT: You can call clear() to clear the output in the console.
print("Welcom to the secret auction programm")
bool = True
bids = {}

#max bid function
def max_bid(bet):
  max_key = ""
  max_bet = 0
  
  for key in bet:
    if bet[key] > max_bet:
      max_bet = bet[key]
      max_key = key

  return max_key
    

while bool:
  #add bid
  name = input("What is your name: ").capitalize()
  bid = int(input("Your bid: $"))
  bids[name] = bid
  #more participants
  more = input("Other bidders y/n: ")
  if more == 'y':
    clear()
    continue
  else:
    clear()
    winner = max_bid(bids)
    print(f"The winner is {winner} with bid: ${bids[winner]}")
    break