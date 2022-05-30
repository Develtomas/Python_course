import hangman_art
import hangman_words
import random as r

#logo print 
print(hangman_art.logo)
#varibles
word_list = hangman_words.word_list
word = list(r.choice(word_list))
secret = []
lives = len(hangman_art.stages)
letter = input("Choose a letter: ").lower()

#word init
for i in range(0, len(word)):
  secret.append("_")

#try word
while "_" in secret:
  #is/not correct letter
  if letter in word:
    #replace '_' to letters
    for j in range(0, len(word)):
      if word[j] == letter:
        secret[j] = letter
    print(*secret, sep=" ")
  else:
    #stages drawing
    print(*secret, sep=" ")
    lives -=1
    print(hangman_art.stages[lives])
    #lost or further
    if lives == 0:
      print("You lose :(")
      break

  #win or further
  if "_" in secret:
    letter = input("Choose a new letter: ").lower()
  else:
    print('You win!')
    break;