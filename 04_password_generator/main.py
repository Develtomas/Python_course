#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
pas = []
for i in range(0, int(nr_letters)):
  pas.append(letters[random.randint(0, len(letters)-1)])

while nr_symbols > 0 or nr_numbers > 0:
  num = random.randint(0, int(nr_letters)-1)
  if pas[num] not in numbers and pas[num] not in symbols:
    if bool(random.getrandbits(1)) and nr_symbols > 0:
      pas[num] = symbols[random.randint(0, len(symbols)-1)]
      nr_symbols-=1
    elif bool(random.getrandbits(1)) and nr_numbers > 0:
      pas[num] = numbers[random.randint(0, len(numbers)-1)]
      nr_numbers-=1
  else: continue;
strpas = ''.join(pas)
print(f'Your pass is:\n{strpas}')