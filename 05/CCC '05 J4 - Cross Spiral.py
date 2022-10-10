width, height, cutwidth, cutheight, steps = int(input()), int(input()), int(input()), int(input()), int(input())

board = []

# MOVE PRIO
# RIGHT --> DOWN --> LEFT --> UP
for x in range(height):
    board += [[0] * width]

for x in range(cutheight):
    for y in range(cutwidth):
        board[x][y] = 2
        board[x][-(y+1)] = 2

        board[-(x+1)][y] = 2
        board[-(x+1)][-(y+1)] = 2

r, c = 0, cutwidth

board[r][c] = 2

last_move = "right"

while steps >= 1:
        steps -= 1
        
        if last_move == "right":
            #MOVE UP
            if r-1 < height and r-1 > 0 and board[r-1][c] != 2:
                board[r-1][c] = 2
                r, c = r-1, c
                last_move == "up"
            #MOVE RIGHT
            elif c+1 < width and board[r][c+1] != 2:
                board[r][c+1] = 2
                r, c = r, c+1
                last_move = "right"
            #MOVE DOWN
            elif r+1 < height and board[r+1][c] != 2:
                board[r+1][c] = 2
                r, c = r+1, c
                last_move = "down"
            else:
                break
        
        elif last_move == "down":
            #MOVE RIGHT
            if c+1 < width and board[r][c+1] != 2:
                board[r][c+1] = 2
                r, c = r, c+1
                last_move = "right"
            #MOVE DOWN
            elif r+1 < height and board[r+1][c] != 2:
                board[r+1][c] = 2
                r, c = r+1, c
                last_move = "down"
            #MOVE LEFT
            elif c-1 >= 0 and board[r][c-1] != 2:
                board[r][c-1] = 2
                r, c = r, c-1
                last_move = "left"
            else:
                break
        
        elif last_move == "left":
            #MOVE DOWN
            if r+1 < height and board[r+1][c] != 2:
                board[r+1][c] = 2
                r, c = r+1, c
                last_move = "down"

            #MOVE LEFT
            elif c-1 >= 0 and board[r][c-1] != 2:
                board[r][c-1] = 2
                r, c = r, c-1
                last_move = "left"
            
            #UP
            elif r-1 < height and r-1 > 0 and board[r-1][c] != 2:
                board[r-1][c] = 2
                r, c = r-1, c
                last_move = "up"
            
            else:
                break
            
        else:
            #MOVE LEFT
            if c-1 >= 0 and board[r][c-1] != 2:
                board[r][c-1] = 2
                r, c = r, c-1
                last_move = "left"
            
            #MOVE UP
            elif r-1 < height and r-1 > 0 and board[r-1][c] != 2:
                board[r-1][c] = 2
                r, c = r-1, c
                last_move == "up"

            #MOVE RIGHT
            elif c+1 < width and board[r][c+1] != 2:
                board[r][c+1] = 2
                r, c = r, c+1
                last_move = "right"
            
            else:
                break

        # print(f"r {r} c {c}")
        # print(last_move)
        # print(board[r])
        # for x in board:
        #     print(
        #         " ".join([str(y) for y in x])
        #         )
        
        # print()
        
print(c+1)
print(r+1)

# for x in board:
#             print(
#                 " ".join([str(y) for y in x])
#                 )