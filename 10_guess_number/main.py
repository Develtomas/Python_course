# Guess the number

#var
from random import randint

HARD = 5
EASY = 10

#init
print('Guess the number between 1 and 100 game!')


def chose_difficulty():
    diff = input(
        f'Please choose difficulty hard({HARD} attempts) - 0, easy({EASY} attempts) - 1: '
    )
    if int(diff):
        return EASY
    else:
        return HARD


def start_new():
    again = input('Try again y/n: ')
    if again.lower() == 'y':
        return main_game()
    else:
        return print('bye')


def main_game():
    number = randint(1, 101)
    att = chose_difficulty()
    while att > 0:
        pl_num = int(input('Choose number between 1 and 100: '))
        if pl_num == number:
            print(f'You guessed right, it is {number}')
            return start_new()
        elif pl_num > number:
            print(f'guessed number less than {pl_num}')
            att -= 1
            print(f'{att} attempts left')
            continue
        elif pl_num < number:
            print(f'guessed number greater than {pl_num}')
            att -= 1
            print(f'{att} attempts left')
            continue
    print('No attempts left. You lose')
    return start_new()


main_game()
