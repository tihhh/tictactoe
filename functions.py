from os import system, name
import random


def clear():
    if name == 'nt':
        _ = system('cls')


def board(a):
    clear()
    b = [[a[1], a[2], a[3]], [a[4], a[5], a[6]], [a[7], a[8], a[9]]]
    for i in b:
        print(*i)


def players():
    p = ''

    while p is not 'X' or p is not 'O':
        p = input("Pick X or O").upper()

        if p == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')


def board_input(brd, txt, pos):
    brd[pos] = txt


def check(brd, txt):
    return (
            (brd[7] and brd[8] and brd[9] == txt) or
            (brd[4] and brd[5] and brd[6] == txt) or
            (brd[1] and brd[2] and brd[3] == txt) or
            (brd[7] and brd[4] and brd[1] == txt) or
            (brd[8] and brd[5] and brd[2] == txt) or
            (brd[9] and brd[6] and brd[9] == txt) or
            (brd[7] and brd[5] and brd[3] == txt) or
            (brd[9] and brd[5] and brd[1] == txt)
    )


def flip():
    r = random.randint(0, 1)

    if r == 0:
        return 'P1'
    else:
        return 'P2'


def space(brd, pos):
    return brd[pos] == ' '


def full_check(brd):
    for i in range(1, 10):
        if space(brd, i):
            return False
    return True


def player_input(brd):
    p = 0

    while p not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space(brd, p):
        p = input("Input board position (1-9): ")

    return p


def replay():
    choice = input("Play again? (Y or N): ")
    return choice == 'Y'

