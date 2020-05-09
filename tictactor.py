import random


def define_current_letter(who_turn):
    if who_turn:
        return 'X'
    else:
        return 'O'


def input_player_letter():
    return ['X', 'O']


def draw_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])


def who_goes_first(playerLetter):
    if playerLetter == 'X':
        return 'player'
    else:
        return 'computer'

def get_board_copy(board):
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy

def find_possible_moves(board, moves_list):
    moves = []
    for move in moves_list:
        if is_space_free(board, move):
            moves.append(move)
    return moves

def make_move(board, letter, move):
     board[move] = letter
    
def get_computer_move(board,player_letter,comp_letter):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    possible_moves = find_possible_moves(board, numbers)
    for i in possible_moves:
        board_copy = get_board_copy(board)
        make_move(board_copy,comp_letter,i)
        if is_winner(board_copy,comp_letter):
            return i
    return choose_random_move_from_board(board, numbers)


def choose_random_move_from_board(board, movesList):
    possible_moves = []
    for move in movesList:
        if is_space_free(board, move):
            possible_moves.append(move)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_player_move(board, turn):
    place = ''
    while place not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(place)):
        input_str = 'куда ставить то? (9-1) %s' % turn
        place = (input(input_str))
    return int(place)


def is_space_free(board, move):
    return board[move] == ' '


def switch_player(turn):
    if turn == 'player':
        return 'comp'
    else:
        return 'player'


def is_winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # Across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # Across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # Across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # Down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # Down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # Down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # Diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # Diagonal


def is_board_full(board):
    # Return True if every space on the board has been taken. Otherwise,return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


def isSpaceFree(board, move):
    return board[move] == ' '


print('прив как дела?\n Это мои крестики нолики')
while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = input_player_letter()
    turn = who_goes_first(playerLetter)
    print('The ' + turn + ' will go first.')
    game_is_playing = True
    while game_is_playing:
        is_player_turn = turn == 'player'
        draw_board(theBoard)
        workingLetter = define_current_letter(is_player_turn)
        move = 0
        if is_player_turn:
            move = get_player_move(theBoard, turn)
        else:
            move = get_computer_move(theBoard,playerLetter, computerLetter )
        theBoard[move] = workingLetter
        # Computer's turn
        if is_winner(theBoard, workingLetter):
            draw_board(theBoard)
            print('The %s won!' % turn)
            game_is_playing = False
        else:
            if is_board_full(theBoard):
                draw_board(theBoard)
                print('The game is a tie!')
                break
            else:
                turn = switch_player(turn)
    play_again = input('хочешь ли сыграть снова?\n(yes or no)').lower()
    if not play_again.startswith('y'):
        print('game over')
        break
