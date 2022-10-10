board = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

x, y = 5, 5

# start = int(input())
# stop = int(input())

start = 10
stop = 27

# last_move = "up"
# last_move = "down"
# last_move = "left"
last_move = "right"

for j in range(stop + 1 - start):
    if j == 0:
        board[x][y] = start
    else:
        if last_move == "up":
            if board[x][y+1] == 0:
                board[x][y+1] = start
                last_move = "right"
                x, y = x, y+1
            else:
                board[x-1][y] = start
                x, y = x-1, y
                
        elif last_move == "right":
            if board[x+1][y] == 0:
                board[x+1][y] = start
                last_move = "down"
                x, y = x+1, y
            else:
                board[x][y+1] = start 
                x, y = x, y+1
                
        elif last_move == "down":
            if board[x][y-1] == 0:
                board[x][y-1] = start
                last_move = "left"
                x, y = x, y-1
            else:
                board[x+1][y] = start
                x, y = x+1, y
                
        elif last_move == "left":
            if board[x-1][y] == 0:
                board[x-1][y] = start
                last_move = "up"
                x, y = x-1, y
            else:
                board[x][y-1] = start
                x, y = x, y-1
                
    start += 1 

for x in board:
    if [str(y) for y in x if y != 0]:
        print(" ".join([str(y) for y in x if y != 0]))

