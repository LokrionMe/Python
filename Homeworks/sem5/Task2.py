import random


def check_num(min_val, max_val):
    while True:
        try:
            numb = int(input(f'Input number from {min_val} to {max_val}: '))
        except ValueError:
            print('It must be number')
        else:
            if min_val <= numb <= max_val:
                return numb
            print(f'Number must be from {min_val} to {max_val}')


def bot_game(difficult, hod, sweets):
    while sweets > 0:
        if hod:
            print("Player's turn")
            take_sweets = check_num(1, 28)
            hod -= 1
        else:
            percent_win = random.randint(1, difficult)
            print("Computer's turn:", end=" ")
            if percent_win == 1:
                take_sweets = random.randint(1, 28)
            else:
                if sweets > 28:
                    if sweets % 29 != 0:
                        take_sweets = sweets % 29
                    else:
                        take_sweets = sweets - 1
                else:
                    take_sweets = sweets
            hod += 1
            print(f'Sweets taken: {take_sweets}')
        sweets -= take_sweets
        print(f'\033[31m {sweets}\033[0m remained')
    return hod


print(' 1. Human vs Human\n 2. Human vs Computer')
game_mode = check_num(1, 2)
sweets = 2021
hod = random.randint(0, 1)
if game_mode == 1:
    while sweets > 0:
        if hod:
            print('1st player turn')
            hod -= 1
        else:
            print('2nd player turn')
            hod += 1
        take_sweets = check_num(1, 28)
        sweets -= take_sweets
        print(f'\033[31m {sweets}\033[0m remained')
    if not hod:
        print('Congratulations!\033[31m 1st\033[0m player winner')
    else:
        print('Congratulations!\033[31m 2nd\033[0m player winner')
if game_mode == 2:
    print(' 1. Easy\n 2. Normal\n 3. Hard')
    diffic = check_num(1, 2)
    winner = bot_game(diffic, hod, sweets)
    if not winner:
        print('Player win')
    else:
        print('Computer win')
