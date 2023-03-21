board_numbers = [" 1 "," 2 "," 3 ",
         " 4 "," 5 "," 6 ",
         " 7 "," 8 "," 9 "]

board = ["   ","   ","   ",
         "   ","   ","   ",
         "   ","   ","   "]

global game_on
game_on = True
winner = False

def display_board_numbers():
    print(board_numbers[0] + " | " + board_numbers[1] + " | " + board_numbers[2])
    print("--" + "--" + "|-" + "--" + "--" + "|-" + "--" + "-")

    print(board_numbers[3] + " | " + board_numbers[4] + " | " + board_numbers[5])
    print("--" + "--" + "|-" + "--" + "--" + "|-" + "--" + "-")

    print(board_numbers[6] + " | " + board_numbers[7] + " | " + board_numbers[8])
    print("--" + "--" + "|-" + "--" + "--" + "|-" + "--" + "-")


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--" + "--" + "|-"+"--" + "--" + "|-"+ "--" + "-")

    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--" + "--" + "|-"+"--" + "--" + "|-"+ "--" + "-")

    print(board[6] + " | " + board[7] + " | " + board[8])
    print("--" + "--" + "|-"+"--" + "--" + "|-"+ "--" + "-")


def pick_player():
    global first_player
    global second_player
    first_player = input("Pick a symbol X or O: ").upper()
    if first_player == 'X':
        second_player = 'O'
    elif first_player == 'O':
        second_player = 'X'
    else:
        print('Wrong input!')
        pick_player()
    return first_player, second_player

def check_for_win(player):
     #Matching rows
    if board[0] == board[1] == board[2] and board[0] != "   " or board[3] == board[4] == board[5] and board[3] != "   " or board[6] == board[7] == board[8] and board[6] != "   ":
        print(f'WE HAVE A WINNER: player"{player}"!')
        game_on = False
        display_board()
        quit()
    #Matching columns
    elif board[0] == board[3] == board[6] and board[0] != "   " or board[1] == board[4] == board[7] and board[1] != "   " or board[2] == board[5] == board[8] and board[2] != "   ":
        print(f'WE HAVE A WINNER: player"{player}"!')
        game_on = False
        display_board()
        quit()
    #Matching diagonals
    elif board[0] == board[4] == board[8] and board[0] != "   " or board[2] == board[4] == board[6] and board[2] != "   ":
        print(f'WE HAVE A WINNER: player"{player}"!')
        display_board()
        game_on = False
        quit()
    else:
        return

def check_position(position):
    if board[position] == ' X ':
        print("Wrong input!")
        return False
    elif board[position] == ' O ':
        print('Wrong input!')
        return False
    else:
        return True

def make_move(player):
    position = input('Choose a position from 1-9: ')
    position = int(position) - 1
    if position not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        print('Wrong position number')
        make_move(player)

    elif check_position(position):
        board[position] = f' {player} '
        check_for_win(player)
        display_board()

    else:
        make_move(player)

def play_game():
    turn = 1
    while game_on and turn < 11:
        if turn == 10:
            print('Tie game! Try again!')
            break
        if turn % 2 != 0:
            print(f'{first_player} move: ')
            make_move(first_player)
        elif turn % 2 == 0:
            print(f'{second_player} move: ')
            make_move(second_player)
        turn += 1




display_board_numbers()
#display_board()
pick_player()
play_game()