import math
import random
import copy

r=6
c=7
player=1
AI=-1
empty=0
win_l=4

def create_board(x,y):
    return [[0 for _ in range(y)] for _ in range(x)]
'''
def view_board(board):
    for row in reversed(board):
        print(row)
'''
'''
def view_board(board):
    for row in reversed(board):
        display_row = []
        for cell in row:
            if cell == 1:
                display_row.append('1')
            elif cell == -1:
                display_row.append('-1')
            else:
                display_row.append(' ')
        print(display_row)
'''

def view_board(board):
    for row in reversed(board):
        visual_row = ""
        for cell in row:
            if cell == player:
                visual_row += "🟢 "
            elif cell == AI:
                visual_row += "🔴 "
            else:
                visual_row += "⚪ "
        print(visual_row)
    print(" 0  1  2  3  4  5  6") 


def place_piece(board,row,col,piece):
    board[row][col]=piece

def is_valid(board,col):
    return board[r-1][col]==0

def next_available_row(board,ccol):
    for row in range(r):
        if board[row][ccol]==0:
            return row
    return None
        

def win_move(board,piece):

    # horizontal check
    for i in range(c-win_l+1):                       
        for j in range(r):
                if all(
                    board[j][i+k]==piece
                    for k in range(win_l)
                ):
                    return True
                
    # vertically
    for i in range(c):
        for j in range(r-win_l+1):
                if all(
                    board[j+k][i]==piece
                    for k in range(win_l)
                ):
                    return True
                
    # positive slope in reversed board
    for i in range(c-win_l+1):
        for j in range(r-win_l+1):
                if all(
                    board[j+k][i+k]==piece
                    for k in range(win_l)
                ):
                    return True

    # negetive slope in reversed board
    for i in range(c-win_l+1):
        for j in range(win_l-1,r):
                if all(
                    board[j-k][i+k]==piece
                    for k in range(win_l)
                ):
                    return True
    
    return False


def check_for_sutiable_move(set_4,piece):
    score=0
    if piece==AI:
        opp_piece = player
    else:
        opp_piece = AI
    
    if set_4.count(piece)==4:
        score+=1000
    elif set_4.count(piece)==3 and set_4.count(empty)==1:
        score+=100
    elif set_4.count(piece)==2 and set_4.count(empty)==2:
        score+=10
    elif set_4.count(opp_piece)==3 and set_4.count(empty)==1:
        score-=1000
        
    return score


def position_score(board,piece):
    
    score = 0

    middle_array = [board[row][c//2] for row in range(r)]
    middle_count = middle_array.count(piece)
    score += middle_count*3

    # Horizontal Score
    for i in range(r):
        for j in range(c-win_l+1):
            set_4 = board[i][j:j+4]
            score += check_for_sutiable_move(set_4,piece)

    # Vertical Score
    for i in range(c):
        for j in range(r-win_l+1):
            set_4 = [board[j+k][i] for k in range(win_l)]
            score += check_for_sutiable_move(set_4,piece)

    # Positive Diagnoal Score
    for i in range(r-win_l+1):
        for j in range(c-win_l+1):
            set_4 = [board[i+k][j+k] for k in range(win_l)]
            score += check_for_sutiable_move(set_4,piece)

    # Negative Diagnoal Score
    for i in range(c-win_l+1):
        for j in range(win_l-1,r):
            set_4 = [board[j-k][i+k] for k in range(win_l)]
            score += check_for_sutiable_move(set_4,piece)

    return score



def get_valid_locations(board):
    return [col for col in range(c) if is_valid(board,col)]
    
def is_terminal_node(board):
    return win_move(board,player) or win_move(board,AI) or len(get_valid_locations(board)) == 0
    
def MinMax(board,depth,alpha,beta,Maximizing_Player):

    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)

    if depth ==0 or is_terminal:
        if is_terminal:
            if win_move(board,AI):
                return (None, 10000)
            elif win_move(board,player):
                return (None, -10000)
            else:
                return (None, 0)
        else:
            return (None, position_score(board,AI))
        
    if Maximizing_Player:
        value = -math.inf
        best_col = random.choice(valid_locations)

        for col in valid_locations:
            row = next_available_row(board,col)
            temp_board = copy.deepcopy(board)
            place_piece(temp_board,row,col,AI)
            new_score = MinMax(temp_board,depth-1,alpha,beta,False)[1]
            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha,value)

            if alpha >= beta:
                break
        return best_col, value
    else:
        value = math.inf
        best_col = random.choice(valid_locations)

        for col in valid_locations:
            row = next_available_row(board,col)
            temp_board = copy.deepcopy(board)
            place_piece(temp_board,row,col,player)
            new_score = MinMax(temp_board,depth-1,alpha,beta,True)[1]
            if new_score < value:
                value = new_score
                best_col = col
            beta = min(beta,value)

            if alpha >= beta:
                break
        return best_col, value

'''
                Game Loop
'''


board = create_board(r,c)
game_over = False

# human = 1 ; AI = -1
turn = 1

view_board(board)

while not game_over:
    if turn == 1:
        try:
            col = int(input("Player , choose from 0-6 : "))

            if 0 <= col < c and is_valid(board,col):
                row = next_available_row(board,col)
                place_piece(board,row,col,player)

                if win_move(board,player):
                    print('Player Won the Game')
                    game_over = True
            else:
                print('Invalid column, only from 0 to 6')
                continue
        
        except ValueError:
            print('Enter a valid number from 0 to 6')
            continue
    
    elif turn == -1:
        print('AI Thinking...')
        col, _ = MinMax(board,10,-math.inf,math.inf,True)
        if col is not None and is_valid(board,col):
            row = next_available_row(board,col)
            place_piece(board,row,col,AI)
            if win_move(board,AI):
                print('AI Won the Game')
                game_over = True

    view_board(board)
    if len(get_valid_locations(board)) == 0 and not game_over:
        print('Its a draw')
        game_over = True
    turn *=-1