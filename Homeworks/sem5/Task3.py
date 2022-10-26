#начал я разбирать tkinter, штука конечно интересная,
#но времени может потребоваться немного больше,
#чем я рассчитывал (основная работа не дает)
import random
import os


def check_num(min_val, max_val):
    while True:
        try:
            num_init = int(
                input(f'Input integer number from {min_val} to {max_val}: '))
        except ValueError:
            print("It's must be number")
        else:
            if min_val <= num_init <= max_val:
                return num_init
                break
            print(f'Number must be from {min_val} to {max_val}')


game_dict = {a: a for a in range(1, 10)}
hod = random.randint(0, 1)
first_player = 'X'
second_player = 'O'
print(' 1st player -> X \n 2nd player -> O')
for i in range(10):
    os.system('cls')
    print(f' ------- \n |{game_dict[1]}|{game_dict[2]}|{game_dict[3]}|\
     \n ------- \n |{game_dict[4]}|{game_dict[5]}|{game_dict[6]}|\
      \n ------- \n |{game_dict[7]}|{game_dict[8]}|{game_dict[9]}|\
       \n ------- \n')
    if i == 9:
        print("It's draw")
        break
    if hod:
        print('1st player turn: ')
        hod -= 1
    else:
        print('2nd player turn: ')
        hod += 1
    while True:
        try:
            pos_of_turn = check_num(1, 9)
        finally:
            if game_dict[pos_of_turn] == pos_of_turn:
                if not hod:
                    game_dict[pos_of_turn] = first_player
                    break
                else:
                    game_dict[pos_of_turn] = second_player
                    break
        print("This cell is full")
    # пытался придумать варианты, чтоб не было столько рукописного кода,
    # но все остальные варианты также кажутся громоздким 
    if ((game_dict[1] == 'X' and game_dict[2] == 'X' and game_dict[3] == 'X') or
        (game_dict[4] == 'X' and game_dict[5] == 'X' and game_dict[6] == 'X') or
        (game_dict[7] == 'X' and game_dict[8] == 'X' and game_dict[9] == 'X') or
        (game_dict[1] == 'X' and game_dict[4] == 'X' and game_dict[7] == 'X') or
        (game_dict[2] == 'X' and game_dict[5] == 'X' and game_dict[8] == 'X') or
        (game_dict[3] == 'X' and game_dict[6] == 'X' and game_dict[9] == 'X') or
        (game_dict[1] == 'X' and game_dict[5] == 'X' and game_dict[9] == 'X') or
            (game_dict[3] == 'X' and game_dict[5] == 'X' and game_dict[7] == 'X')):
        print("1st player win")
        break
    if ((game_dict[1] == 'O' and game_dict[2] == 'O' and game_dict[3] == 'O') or
        (game_dict[4] == 'O' and game_dict[5] == 'O' and game_dict[6] == 'O') or
        (game_dict[7] == 'O' and game_dict[8] == 'O' and game_dict[9] == 'O') or
        (game_dict[1] == 'O' and game_dict[4] == 'O' and game_dict[7] == 'O') or
        (game_dict[2] == 'O' and game_dict[5] == 'O' and game_dict[8] == 'O') or
        (game_dict[3] == 'O' and game_dict[6] == 'O' and game_dict[9] == 'O') or
        (game_dict[1] == 'O' and game_dict[5] == 'O' and game_dict[9] == 'O') or
            (game_dict[3] == 'O' and game_dict[5] == 'O' and game_dict[7] == 'O')):
        print("2nd player win")
        break
