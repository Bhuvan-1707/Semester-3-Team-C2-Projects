import math
import random

size = 8

player = 1
AI = -1


p1 = 1
p2 = -1

'''
def create_board():
    k = [[0 for _ in range(size)] for _ in range(size)]
    k[3][3] = p2
    k[4][4] = p2
    k[3][4] = p1
    k[4][3] = p1
    return k
'''

def create_board():
    k = [[0 for _ in range(size)] for _ in range(size)]
    k[3][3] = AI
    k[4][4] = AI
    k[3][4] = player
    k[4][3] = player
    return k

'''
def view_board(board):
    print(" 0  1  2  3  4  5  6  7")
    for r, row in enumerate(board):
        view = f"{r}"
        for i in row:
            if i==p1:
                view += "🟢 "
            elif i==p2:
                view += "🔴 "
            else:
                view += "⚪ "
        print(view)
    print()
'''    


def view_board(board):
    print(" 0  1  2  3  4  5  6  7")

    for r, row in enumerate(board):
        view = f"{r}"
        for i in row:
            if i==player:
                view += "🟢 "
            elif i==AI:
                view += "🔴 "
            else:
                view += "⚪ "
        print(view)
    print()


'''
Here, in directions (x,y) denotes row and column respectivly.
    For, x :
       -1  -> move up by 1
        1  -> move down by 1
        0  -> no change
    
    For, y :
       -1  -> move left by 1
        1  -> move right by 1
        0  -> no change
'''

# for checking if placed piece is valid
directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

'''
def place_valid_piece(board,row,col,piece):
'''

def is_valid_move(board,row,col,piece):

    if board[row][col] != 0:
        return False
    
    opp_piece = -piece
    #valid = False

    for dr, dc in directions:

        r, c = row + dr, col + dc
        found_opp_piece = False

        while 0 <= r < size and 0 <= c < size and board[r][c] == opp_piece:
            r += dr
            c += dc
            found_opp_piece = True

        if found_opp_piece and 0 <= r < size and 0 <= c < size and board[r][c] == piece:
            # valid = True
            return True
    
    # return valid
    return False
            

def get_valid_moves(board,piece):

    valid_moves = []

    for r in range(size):
        for c in range(size):
            if is_valid_move(board,r,c,piece):
                valid_moves.append((r,c))
    return valid_moves


def flip_move(board,row,col,piece):
    board[row][col] = piece
    opp_piece = -piece

    for dr, dc in directions:
        r, c = row + dr, col + dc
        flips = []

        while 0 <= r < size and 0 <= c < size and board[r][c] == opp_piece:
            flips.append((r,c))
            r += dr
            c += dc

        if flips and 0 <= r < size and 0 <= c < size and board[r][c] == piece:
            for flip_r, flip_c in flips:
                board[flip_r][flip_c] = piece


def score_board(board,piece):
    k = 0

    for row in board:
        k += row.count(piece)
    
    return k


def is_game_over(board):
    return not get_valid_moves(board,player) and not get_valid_moves(board,AI)


def MinMax(board,depth,alpha,beta,Maximizing):

    if depth == 0 or is_game_over(board):
        return None, score_board(board,AI) - score_board(board,p1)
    
    if Maximizing:
        piece = p2
    else:
        piece = p1

    moves = get_valid_moves(board,piece)


    if not moves:
        return MinMax(board,depth-1,alpha,beta,not Maximizing)
    
    best_move = None

    if Maximizing:
        value = -math.inf

        for move in moves:
            temp = [r.copy() for r in board]
            flip_move(temp,move[0],move[1],piece)
            _, score = MinMax(temp,depth-1,alpha,beta,False)
            if score > value:
                value = score
                best_move = move
            alpha = max(alpha,value)
            if alpha >= beta:
                break
        return best_move, value
    
    else:
        value = math.inf

        for move in moves:
            temp = [r.copy() for r in board]
            flip_move(temp,move[0],move[1],piece)
            _, score = MinMax(temp,depth-1,alpha,beta,True)
            if score < value:
                value = score
                best_move = move
            beta = min(beta,value)
            if alpha >= beta:
                break
        return best_move, value
    
'''                  Game Loop               '''


board = create_board()
turn = player
game_over = False


try:
    while not game_over:
        view_board(board)
        if turn == player:
            moves = get_valid_moves(board,player)
            if moves:
                print("Valid Moves : ", [(r, c) for r, c in moves])
                print("Enter -1 -1 to skip your turn")
                try:
                    #r, c = map(int, input("Enter row(0-7) and col(0-7) : ").split())
                    r = int(input("Enter Row : "))
                    c = int(input("Enter COlumn : "))

                    if r == -1 and c == -1:
                        print("Player chooses to skip turn")
                        turn = AI
                    elif (r,c) in moves:
                        flip_move(board,r,c,player)
                        turn = AI
                    else:
                        print("Invalid move")
                except ValueError:
                    print("Enter a valid row(0-7) and col(0-7)")
            else:
                print("Player passes turn to AI")
                turn = AI
        else:
            moves = get_valid_moves(board,AI)
            if moves:
                print("AI is Thinking....")
                move, _ =  MinMax(board,10,-math.inf,math.inf,True)
                if move:
                    flip_move(board,move[0],move[1],AI)
                turn = player
            else:
                print("AI passes turn to Player")
                turn = player
        
        if is_game_over(board):
            game_over = True
except KeyboardInterrupt:
    print("\nGame Interrupted by User. Exiting...")
    exit()


'''
board = create_board()
turn = p1
game_over = False

try:
    while not game_over:
        view_board(board)
        if turn == p1:
            moves = get_valid_moves(board,p1)
            if moves:
                print("Valid Moves : ", [(r, c) for r, c in moves])
                print("Enter -1 -1 to skip your turn")
                try:
                    r, c = map(int, input("Enter row(0-7) and col(0-7) : ").split())
                    if r == -1 and c == -1:
                        print("Player chooses to skip turn")
                        turn = p2
                    elif (r,c) in moves:
                        flip_move(board,r,c,p1)
                        turn = p2
                    else:
                        print("Invalid move")
                except ValueError:
                    print("Enter a valid row(0-7) and col(0-7)")
            else:
                print("Player passes turn to AI")
                turn = p2
        else:
            moves = get_valid_moves(board,p2)
            if moves:
                print("Valid Moves : ", [(r, c) for r, c in moves])
                print("Enter -1 -1 to skip your turn")
                try:
                    r, c = map(int, input("Enter row(0-7) and col(0-7) : ").split())
                    if r == -1 and c == -1:
                        print("Player chooses to skip turn")
                        turn = p1
                    elif (r,c) in moves:
                        flip_move(board,r,c,p2)
                        turn = p1
                    else:
                        print("Invalid move")
                except ValueError:
                    print("Enter a valid row(0-7) and col(0-7)")
            else:
                print("Player passes turn to AI")
                turn = p1
        
        if is_game_over(board):
            game_over = True
except KeyboardInterrupt:
    print("\nGame Interrupted by User. Exiting...")
    exit()
'''

'''
view_board(board)
P_score = score_board(board,p1)
AI_score = score_board(board,p2)
'''

view_board(board)
P_score = score_board(board,player)
AI_score = score_board(board,AI)

print(f"Final Score : Player {P_score} - AI {AI_score}")

if P_score > AI_score:
    print("Player Won the Mathch")
elif AI_score > P_score:
    print("AI Won the Mathch")
else:
    print("It's a Draw")
