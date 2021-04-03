def DisplayBoard(board):
    print('\n' * 100)

    print(' ' + board[1] + '| ' + board[2] + ' |' + board[3])
    print('__|___|__')
    print(' ' + board[4] + '| ' + board[5] + ' |' + board[6])
    print('__|___|__')
    print(' ' + board[7] + '| ' + board[8] + ' |' + board[9])
    print('  |   |  ')


def give_input():
    player1 = int(input("Enter the Box number: "))

    return player1


def start_game(board, move_number):
    if move_number % 2 != 0:
        move = give_input()
        board[move] = 'X'
    else:
        move2 = give_input()
        board[move2] = 'O'
    DisplayBoard(board)


def winner(board):
    win = False

    if board[1] == board[2] == board[3] and board[1] != ' ':
        win = True
    elif board[4] == board[5] == board[6] and board[4] != ' ':
        win = True
    elif board[7] == board[8] == board[9] and board[7] != ' ':
        win = True
    elif board[1] == board[4] == board[7] and board[7] != ' ':
        win = True
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        win = True
    elif board[3] == board[6] == board[9] and board[3] != ' ':
        win = True
    elif board[1] == board[5] == board[9] and board[1] != ' ':
        win = True
    elif board[3] == board[5] == board[7] and board[7] != ' ':
        win = True
    return win


Game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
a = 0
while not winner(Game_board):
    a += 1
    DisplayBoard(Game_board)
    start_game(Game_board, a)
if winner(Game_board):
    print("Game OVER")
    if a % 2 != 0:
        print("Player One wins")
    else:
        print("Player Two wins")
