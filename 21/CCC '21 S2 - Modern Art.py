m = int(input())
n = int(input())

hm_moves = int(input())

rows = [1] * m
cols = [1] * n
gold = 0

for x in range(hm_moves):
    move = input().split()
    dir = move[0]
    num = int(move[1])

    if dir == "R":
        rows[num-1] += 1
    
    if dir == "C":
        cols[num-1] += 1
    
for x in range(m):
    for y in range(n):
        if (rows[x] + cols[y]) % 2 != 0:
            gold += 1

print(gold)


