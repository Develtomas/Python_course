from art import logo
print(logo);

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#shifted alphabet
def alpabet_modifier(list, gap):
  if gap > len(alphabet):
    if gap % len(alphabet) == 0:
      gap = len(alphabet)
    else: 
      gap = (gap%len(alphabet))
  return list[gap:]+list[0:gap]

#crypto fn
def crypt(message, sh, work):
  plain_list=[]
  #encode\decode
  if work == "encode":
    curr_alph = alphabet
    alt_alph = alpabet_modifier(alphabet, sh)
  elif work == "decode":
    curr_alph = alpabet_modifier(alphabet, sh)
    alt_alph = alphabet
  #main function
  for let in message:
    if let in curr_alph:
      num = curr_alph.index(let)
      plain_list.append(alt_alph[num])
    else:
      plain_list.append(let)
  #print res
  # print("Result: ")
  print("Result: ", *plain_list, sep='')

#initial
while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = abs(int(input("Type the positive shift number:\n")))
  crypt(text, shift, direction)
  resume = input("Type 'y' to continue, nothing otherwise: ")
  if resume.lower() != 'y':
    print("Good bye")
    break;