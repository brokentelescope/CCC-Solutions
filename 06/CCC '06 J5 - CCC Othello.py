def moveWhite(row, column):
    change = [[row,column]]
    #topleft
    r = row
    c = column
    hold = []
    while True:
        try:
            if board[r-1][c-1] == 2:
                hold.append([r-1,c-1])
                r -= 1 
                c -= 1
            elif board[r-1][c-1] == 1:
                for x in hold:
                    change.append(x)
                break
            else:
                break
            
        except:
            break
    
    #top
    r = row
    c = column
    hold = []
    while True:
        try:
            if board[r-1][c] == 2:
                hold.append([r-1,c])
                r -= 1 
            elif board[r-1][c] == 1:
                for x in hold:
                    change.append(x)
                break
            else:
                break
        except:
            break
    
    #topright
    r = row
    c = column
    hold = []
    while True:
        try:
            if board[r-1][c+1] == 2:
                hold.append([r-1,c+1])
                r -= 1 
                c += 1
            elif board[r-1][c+1] == 1:
                for x in hold:
                    change.append(x)
                break
            else:
                break
        except:
            break

    #right
    r = row
    c = column
    hold = []
    while True:
        try:
            if board[r][c+1] == 2:
                hold.append([r,c+1])
                c += 1
            elif board[r][c+1] == 1:
                for x in hold:
                    change.append(x)
                break
            else:
                break
        except:
            break
    
    #botright
    r = row
    c = column
    hold = []
    while True:
        try:
            if board[r+1][c+1] == 2:
                hold.append([r+1,c+1])
                r += 1 
                c += 1
            elif board[r+1][c+1] == 1:
                for x in hold:
                    change.append(x)
                break
            else:
                break
        except:
            break
    
    #bot
    r = row
    c = column
    hold = []
    while True:
        try:
            if board[r+1][c] == 2:
                hold.append([r+1,c])
                r += 1
            elif board[r+1][c] == 1:
                for x in hold:
                    change.append(x)
                break
            else:
                break
        except:
            break
    
    #botleft
    r = row
    c = column
    hold = []
    while True:
        try:
            if board[r+1][c-1] == 2:
                hold.append([r+1,c-1])
                r += 1 
                c -= 1
            elif board[r+1][c-1] == 1:
                for x in hold:
                    change.append(x)
                break
            else:
                break
        except:
            break
    
    #left
    r = row
    c = column
    hold = []
    while True:
        try:
            if board[r][c-1] == 2:
                hold.append([r,c-1])
                c -= 1
            elif board[r][c-1] == 1:
                for x in hold:
                    change.append(x)
                break
            else:
                break
        except:
            break
    
    for x in change:
        r, c = x 
        board[r][c] = 1
        
def moveBlack(row, column):
    change = [[row,column]]
    #topleft 
    r = row
    c = column
    hold = []
    while True:
        try:
            if board[r-1][c-1] == 1:
                hold.append([r-1,c-1])
                r -= 1 
                c -= 1
            elif board[r-1][c-1] == 2:
                for x in hold:
                    change.append(x)
                break
            else:
                break
        except:
            break
    
    #top
    r = row
    c = column
    hold = []
    while True:
        try:
            if board[r-1][c] == 1:
                hold.append([r-1,c])
                r -= 1 
            elif board[r-1][c] == 2:
                for x in hold:
                    change.append(x)
                break
            else:
                break
        except:
            break
    
    #topright
    r = row
    c = column
    hold = []
    while True:
        try:
            if board[r-1][c+1] == 1:
                hold.append([r-1,c+1])
                r -= 1 
                c += 1
            elif board[r-1][c+1] == 2:
                for x in hold:
                    change.append(x)
                break
            else:
                break
        except:
            break

    #right
    r = row
    c = column
    hold = []
    while True:
        try:
            if board[r][c+1] == 1:
                hold.append([r,c+1])
                c += 1
            elif board[r][c+1] == 2:
                for x in hold:
                    change.append(x)
                break
            else:
                break
        except:
            break
    
    #botright
    r = row
    c = column
    hold = []
    while True:
        try:
            if board[r+1][c+1] == 1:
                hold.append([r+1,c+1])
                r += 1 
                c += 1
            elif board[r+1][c+1] == 2:
                for x in hold:
                    change.append(x)
                break
            else:
                break
        except:
            break
    
    #bot
    r = row
    c = column
    hold = []
    while True:
        try:
            if board[r+1][c] == 1:
                hold.append([r+1,c])
                r += 1
            elif board[r+1][c] == 2:
                for x in hold:
                    change.append(x)
                break
            else:
                break
        except:
            break
    
    #botleft
    r = row
    c = column
    hold = []
    while True:
        try:
            if board[r+1][c-1] == 1:
                hold.append([r+1,c-1])
                r += 1 
                c -= 1
            elif board[r+1][c-1] == 2:
                for x in hold:
                    change.append(x)
                break
            else:
                break
        except:
            break
    
    #left
    r = row
    c = column
    hold = []
    while True:
        try:
            if board[r][c-1] == 1:
                hold.append([r,c-1])
                c -= 1
            elif board[r][c-1] == 2:
                for x in hold:
                    change.append(x)
                break
            else:
                break
        except:
            break
    
    for x in change:
        r, c = x 
        board[r][c] = 2
        
def printboard():
    for x in board:
        print(" ".join([str(y) for y in x]))
    print()
a = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

b = [
    [2, 0, 0, 0, 0, 0, 0, 1],
    [0, 2, 0, 0, 0, 0, 1, 0],
    [0, 0, 2, 0, 0, 1, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 1, 0, 0, 2, 0, 0],
    [0, 1, 0, 0, 0, 0, 2, 0],
    [1, 0, 0, 0, 0, 0, 0, 2],
]

c = [
    [0, 0, 2, 2, 1, 1, 0, 0],
    [0, 0, 2, 2, 1, 1, 0, 0],
    [0, 0, 2, 2, 1, 1, 0, 0],
    [0, 0, 2, 2, 1, 1, 0, 0],
    [0, 0, 2, 2, 1, 1, 0, 0],
    [0, 0, 2, 2, 1, 1, 0, 0],
    [0, 0, 2, 2, 1, 1, 0, 0],
    [0, 0, 2, 2, 1, 1, 0, 0],
]

info = input().split(" ")
config = info[0]
hm_moves = int(info[1])
moves = []
counter = 2
for x in range(hm_moves):
    moves.append([int(info[counter]), int(info[counter+1])])
    counter += 2

if config == "a":
    board = a
elif config == "b":
    board = b
else:
    board = c

counter = 0
for x in range(hm_moves//2): 
    r = moves[counter][0]
    c = moves[counter][1]
    counter += 1
    moveBlack(r-1,c-1)
    
    # printboard()
    
    r = moves[counter][0]
    c = moves[counter][1]
    moveWhite(r-1,c-1)
    counter += 1
    # printboard()
    
if hm_moves % 2 != 0:
    r = moves[-1][0]
    c = moves[-1][1]
    colour = 1
    moveBlack(r-1,c-1)
    
    # printboard()

black = 0
white = 0

for x in board:
    for y in x:
        if y == 1:
            white += 1
        elif y == 2:
            black += 1

print(black, white)