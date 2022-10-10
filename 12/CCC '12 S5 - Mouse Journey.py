rows, columns = [int(x) for x in input().split(" ")]
    
board = []

board += [[1] * columns]

for x in range(rows-1):
    board += [[-1] * columns]

for x in range(rows):
    board[x][0] = 1

cats = []
for x in range(int(input())):
    cr, cc = [int(x) for x in input().split(" ")]

    if cr == 1:
        for x in range(cc, columns):
            board[0][x] = 0
    if cc == 1:
        for x in range(cr, rows):
            board[x][0] = 0    

    board[cr-1][cc-1] = 0

    # for x in board:
    #     print(" ".join([str(y) for y in x]))
    # print()

for r in range(1,rows):
    for c in range(1,columns):
        if board[r][c] != 0:
            board[r][c] = board[r-1][c] + board[r][c-1]
            # for x in board:
            #     print(" ".join([str(y) for y in x]))
            # print()

print(board[-1][-1])
# input
#3 4

#output if i use board1
# 1 1 1 1
# 1 2 -1 -1
# 1 -1 -1 -1

# 1 1 1 1
# 1 2 3 -1
# 1 -1 -1 -1

# 1 1 1 1
# 1 2 3 4
# 1 -1 -1 -1

# 1 1 1 1
# 1 2 3 4
# 1 3 -1 -1

# 1 1 1 1
# 1 2 3 4
# 1 3 6 -1

# 1 1 1 1
# 1 2 3 4
# 1 3 6 10

# input
# 3 4

#output when i use board          
# 1 1 1 1
# 1 2 -1 -1
# 1 2 -1 -1

# 1 1 1 1
# 1 2 3 -1
# 1 2 3 -1

# 1 1 1 1
# 1 2 3 4
# 1 2 3 4

# 1 1 1 1
# 1 3 3 4
# 1 3 3 4

# 1 1 1 1
# 1 3 6 4
# 1 3 6 4

# 1 1 1 1
# 1 3 6 10
# 1 3 6 10