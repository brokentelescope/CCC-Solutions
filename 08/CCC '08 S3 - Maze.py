def valid(x,y):
    if x >= 0 and x <= r-1 and y >= 0 and y <= c-1:
        return True
    return False

def p(board):
    print()
    for x in board:
        print(" ".join(x))
    print()

def solve(board):
    queue = [[0,0]]
    visited = [[0,0]]
    steps = 1

    if board[r-1][c-1] == "*":
        return -1
        
    while queue:
        for x in range(len(queue)):
            node = queue.pop(0)

            if node == [r-1,c-1]:
                return steps

            x,y = node

            symbol = board[x][y]

            if symbol == "+":
                #up
                if [x-1,y] not in visited:
                    if valid(x-1,y):
                        queue.append([x-1,y])
                        visited.append([x-1,y])
                
                #down
                if [x+1,y] not in visited:
                    if valid(x+1,y):
                        queue.append([x+1,y])
                        visited.append([x+1,y])
                
                #left
                if [x,y-1] not in visited:
                    if valid(x,y-1):
                        queue.append([x,y-1])
                        visited.append([x,y-1])
                
                #right
                if [x,y+1] not in visited:
                    if valid(x,y+1):
                        queue.append([x,y+1])
                        visited.append([x,y+1])

            elif symbol == "|":
                #up
                if [x-1,y] not in visited:
                    if valid(x-1,y):
                        queue.append([x-1,y])
                        visited.append([x-1,y])
                
                #down
                if [x+1,y] not in visited:
                    if valid(x+1,y):
                        queue.append([x+1,y])
                        visited.append([x+1,y])
            
            elif symbol == "-":
                #left
                if [x,y-1] not in visited:
                    if valid(x,y-1):
                        queue.append([x,y-1])
                        visited.append([x,y-1])
                
                #right
                if [x,y+1] not in visited:
                    if valid(x,y+1):
                        queue.append([x,y+1])
                        visited.append([x,y+1])
        
        steps += 1
    return -1

output = []
for x in range(int(input())):
    r = int(input())
    c = int(input())

    board = []

    for x in range(r):
        board.append(list(input()))

    output.append(solve(board))
    
for x in output:
    print(x)
    