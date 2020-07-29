
board=["-","-","-","-","-","-","-","-","-"]
current_player='X'
game_is_on=True
winner=None
print('WELCOME')
print("Let's  play Tic Tac Toe")
print('Plz give the reqiured detail')
player1=input('Player 1 name:')
player2=input('Player 2 name:')
current_name=player1
print(player1 + ' has been assigned with X')
print('AND')
print(player2 + ' has been assigned with 0')
b=True
def display_board():
    print(board[0] + '|'+ board[1]+'|'+ board[2])
    print(board[3] + '|'+ board[4]+'|'+ board[5])
    print(board[6] + '|'+ board[7]+'|'+ board[8])
def position_input(player,name):
    print(name+"'s turn:")
    position=input('Plz Choose a Position from 1-9:')
    valid = True
    while valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
             position = input("Choose a position from 1-9: ")
        position = int(position) - 1
        if board[position] == "-":
            valid = False
        else:
            print("You can't go there. Go again.")
    board[position] = player
    display_board()
def give_turn():
    global current_player
    global current_name
    if current_player=='X':
        current_player='0'
    elif current_player=='0':
        current_player='X'
    if current_name == player1:
        current_name=player2
    elif current_name == player2:
        current_name=player1

def check_if_game_over():
    check_win()
    check_if_tie()

def check_win():
    global winner
    row_done=check_row()
    vertical_done=check_vertical()
    diagonal_done=check_diagonal()
    if row_done :
        winner=row_done
    elif vertical_done :
        winner=vertical_done
    elif diagonal_done :
        winner=diagonal_done
    else:
        winner=None
def check_row():
    global game_is_on
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_is_on = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    else:
        return None

def check_vertical():
    global game_is_on
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_is_on = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None
def check_diagonal():
     global game_is_on
     diagonal_1 = board[0] == board[4] == board[8] != "-"
     diagonal_2 = board[2] == board[4] == board[6] != "-"
     if diagonal_1 or diagonal_2:
         game_is_on=False
     if diagonal_1:
         return board[0]
     elif diagonal_2:
         return board[2]
     else:
         return None


def check_if_tie():
    global game_is_on
    if "-" not in board:
        game_is_on = False
        return True
    else:
        return False
def play():
    global b
    global current_player
    #global winner
    print('Are You Ready')
    print("Let's start the game")
    display_board()
    while game_is_on:
        position_input(current_player,current_name)
        check_if_game_over()
        give_turn()
    print('\n')
    if winner=='X' :
        print('CONGRATULATIONS!')
        print(player1 +' won \n' )
        print(player2 +' Better luck next time.')
    elif winner=='0' :
        print('CONGRATULATIONS!')
        print(player2 +' won \n')
        print(player1 +' Better luck next time.')
    elif winner==None:
        print("It's a tie")
#start thw game
play()
