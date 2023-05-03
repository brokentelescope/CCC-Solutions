# please forgive me for this disgusting code

# if there are two values in a row/col, u can fill that row/col 
# this can solve most grids
# only cases to look out for is 3 cells filled in and 5 cells filled in 
# i just wrote code for every single case
# surely this can be made more elegant

board = []

for x in range(3): board.append(input().split())

n = 0
for x in range(3):
    for y in range(3):
        if board[x][y] != 'X':
            n += 1
            board[x][y] = int(board[x][y])
def p():
    for x in board:
        print(" ".join([str(x) for x in x]))

# function to fill any rows/cols with two squares filled in 
def fill():
    global n
    for x in range(3):
        nums = 0 
        for y in range(3):
            if board[x][y] != 'X': nums += 1
        if nums == 2:
            if board[x][0] == 'X': board[x][0] = 2 * board[x][1] - board[x][2]
            elif board[x][1] == 'X': board[x][1] = (board[x][0] + board[x][2])//2 
            else: board[x][2] = 2 * board[x][1] - board[x][0]
            n += 1

    # check all the columns 

    for x in range(3):
        nums = 0
        for y in range(3):
            if board[y][x] != 'X': nums += 1
        if nums == 2:
            if board[0][x] == 'X': board[0][x] = 2 * board[1][x] - board[2][x]
            elif board[1][x] == 'X': board[1][x] = (board[0][x] + board[2][x])//2
            else: board[2][x] = 2 * board[1][x] - board[0][x]
            n += 1

fill(); fill()

if n != 9:
    if n == 0:
        for x in range(3): board[x] = [0, 0 ,0]

    if n == 1:
        for x in range(3):
            for y in range(3):
                if board[x][y] != 'X': ans = board[x][y]
        for x in range(3): board[x] = [ans, ans, ans]   

    if n == 2:
        xcord = [0, 1, 2]
        ycord = [0, 1, 2]

        for x in range(3):
            for y in range(3):
                if board[x][y] != 'X': xcord.remove(x); ycord.remove(y); val = board[x][y]

        board[xcord[0]][ycord[0]] = val
        n += 1

    if n == 3:
        # case 1: 1 row/col filled
        # then we can duplicate the row/col twice
        if board[0].count('X') == 0:
            board[1] = board[2] = board[0]
        elif board[1].count('X') == 0:
            board[0] = board[2] = board[1]
        elif board[2].count('X') == 0:
            board[0] = board[1] = board[2]
        
        elif board[0][0] != 'X' and board[1][0] != 'X' and board[2][0] != 'X':
            board[0][1] = board[0][2] = board[0][0]
            board[1][1] = board[1][2] = board[1][0]
            board[2][1] = board[2][2] = board[2][0]
        elif board[0][1] != 'X' and board[1][1] != 'X' and board[2][1] != 'X':
            board[0][0] = board[0][2] = board[0][1]
            board[1][0] = board[1][2] = board[1][1]
            board[2][0] = board[2][2] = board[2][1]
        elif board[0][2] != 'X' and board[1][2] != 'X' and board[2][2] != 'X':
            board[0][0] = board[0][1] = board[0][2]
            board[1][0] = board[1][1] = board[1][2]
            board[2][0] = board[2][1] = board[2][2]

        # case 2: no rol/col filled
        # then we can fill in one square and solve

        elif board[0][0] != 'X':
            if board[1][1] != 'X':
                # a X X
                # X b X
                # X X c
                board[1][0] = board[1][1]; fill(); fill()
            elif board[1][2] != 'X':
                # a X X    
                # X X b    
                # X c X 
                board[1][1] = board[2][1]; fill(); fill()
        elif board[0][1] != 'X':
            # X a X         X a X
            # b X X    or   X X b
            # X X c         c X X
            board[1][1] = board[0][1]; fill(); fill()
        elif board[0][2] != 'X':
            if board[1][0] != 'X':
                # X X a
                # b X X
                # X c X
                board[1][1] = board[2][1]; fill(); fill()
            elif board[1][1] != 'X':
                # X X a
                # X b X
                # c X X      
                board[1][2] = board[1][1]; fill(); fill()
    if n == 5:
        if board[1][1] == 'X' and board[1][2] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
            # a b c 
            # d X X
            # e X X
            board[1][1] = 2 * board[0][1] - board[0][0]; fill(); fill()
        elif board[1][0] == 'X' and board[1][1] == 'X' and board[2][0] == 'X' and board[2][1] == 'X':
            # a b c 
            # X X d
            # X X e
            board[1][1] = 2* board[0][1] - board[0][2]; fill(); fill()
        elif board[0][0] == 'X' and board[0][1] == 'X' and board[1][0] == 'X' and board[1][1] == 'X':
            # X X a 
            # X X b
            # e d c
            board[1][1] = 2 * board[2][1] - board[2][2]; fill(); fill()
        elif board[0][1] == 'X' and board[0][2] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
            # a X X 
            # b X X
            # c d e
            board[1][1] = 2 * board[2][1] - board[2][0]; fill(); fill()
        elif board[0][1] == 'X' and board[0][2] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
            # a X X 
            # b c d
            # c x x
            board[0][1] = 2 * board[1][1] - board[1][0]; fill(); fill()
        elif board[0][0] == 'X' and board[0][1] == 'X' and board[2][0] == 'X' and board[2][1] == 'X':
            # X X b 
            # c d e
            # X X f
            board[0][1] = 2 * board[1][1] - board[1][2]; fill(); fill()
        elif board[0][0] == 'X' and board[0][2] == 'X' and board[1][0] == 'X' and board[1][2] == 'X':
            # X a X 
            # X b X
            # c d e
            board[1][2] = 2 * board[1][1] - board[1][1]; fill(); fill()
        elif board[1][0] == 'X' and board[1][2] == 'X' and board[2][0] == 'X' and board[2][2] == 'X':
            # a b c 
            # X b X
            # X e X
            board[1][2] = 2 * board[1][1] - board[0][1]; fill(); fill()
        elif board[0][0] == 'X' and board[0][2] == 'X' and board[2][0] == 'X' and board[2][2] == 'X':
            # x a x 
            # b c d
            # X e X
            board[0][0] = 2 * board[1][0] - board[1][1]; fill(); fill()
p()
            
