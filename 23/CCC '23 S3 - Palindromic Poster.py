n, m, r, c = [int(x) for x in input().split()] 

# https://dmoj.ca/problem/ccc23s3/editorial 

flag = True 

rotated = False 

if c == 0 or c == m:
    n, m, r, c = m, n, c, r 
    rotated = True 

board = [['a'] * m for x in range(n)]

if r == 0:
    for x in range(n):
        board[x][m-1] = 'b'
    for x in range(m-c):
        board[n-1][m-1-x] = chr(ord(board[n-1][m-1-x])+1)
                
elif r == n:
    if c % 2 != m % 2:
        if m % 2 == 0: 
            print("IMPOSSIBLE")
            flag = False
        else:
            for x in range(m):
                board[0][x] = 'b'

            for x in range(1, c//2+1):
                board[0][m//2-x] = 'a'
                board[0][m//2+x] = 'a'

            board[0][m//2] = 'b'

    else:
        for x in range((m-c)//2):
            board[0][x] = 'b'
            board[0][m-1-x] = 'b'

else:
    for x in range(r, n):
        for y in range(c, m):
            board[x][y] = 'b'

if flag:
    if rotated:
        for x in zip(*board[::-1]):
            print("".join(x))
    else:
        for x in board:
            print("".join(x))


