from functions import *

print("Tic Tac Toe")

while True:
    brd = [' '] * 10
    p1, p2 = players()

    t = flip()
    print(t + ' goes first')

    play = input("Ready to play? (Y or N)")

    if play == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if t == 'P1':
            board(brd)
            position = player_input(brd)
            board_input(brd, p1, position)

            if check(brd, p1):
                board(brd)
                print("Player 1 has won")
                game_on = False
            else:
                if full_check(brd):
                    board(brd)
                    print("Tie!")
                    game_on = False
                else:
                    t = 'P2'
        else:
            board(brd)
            position = player_input(brd)
            board_input(brd, p2, position)

            if check(brd, p2):
                board(brd)
                print("Player 2 has won")
                game_on = False
            else:
                if full_check(brd):
                    board(brd)
                    print("Tie!")
                    game_on = False
                else:
                    t = 'P1'
    if not replay():
        break
