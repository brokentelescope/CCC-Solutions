word = input()

n = int(input())
m = int(input())

board = []

# list to keep track of each location of the starting letter
pos = []

for x in range(n):
    line = input().split()
    for y in range(m):
        if line[y] == word[0]:
            pos.append((x,y))
    board.append(line)

# r: row number
# c: col number
# dir: ex. (1, -1) --> move 1 row forward, 1 col backward
# idx: which letter are you at in the word
# switch: if you can switch directions or not, i.e if you haven't switched directions yet

def solve(r, c, dir, idx, switch=True):
    ans = 0 

    if idx == len(word):
        return 1 
    
    # continue on original direction
    r1 = r + dir[0]
    c1 = c + dir[1]

    if r1 >= 0 and r1 < n and c1 >= 0 and c1 < m:
        if board[r1][c1] == word[idx]:
            ans += solve(r1, c1, dir, idx+1, switch)
        
    # switch directions 
    # you can't switch on the first move because that would just generate duplicate paths
    # i ran into this problem during the actual ccc 
    # instead of fixing it i just kept track of the paths
    # and added them to a set and returned the length of the set
    if switch and idx != 1:
        dir2 = (dir[1], -dir[0])
        r2 = r + dir2[0]
        c2 = c + dir2[1]

        if r2 >= 0 and r2 < n and c2 >= 0 and c2 < m:
            if board[r2][c2] == word[idx]:
                # make sure to pass the new directions into function

                # make sure to change switch to False to indicate
                # that you can  no longer switch directions

                ans += solve(r2, c2, dir2, idx+1, False)

        dir3 = (-dir[1], dir[0])
        r3 = r + dir3[0]
        c3 = c + dir3[1]

        if r3 >= 0 and r3 < n and c3 >= 0 and c3 < m:
            if board[r3][c3] == word[idx]:
                ans += solve(r3, c3, dir3, idx+1, False)
        
    return ans 

# for each position of the starting letter,
# loop through each of the 8 directions

ans = 0
for r, c in pos:
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0: 
                continue 
            ans += solve(r, c, (x,y), 1, True)

print(ans)