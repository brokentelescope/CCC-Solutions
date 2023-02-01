n = int(input())
t = int(input())

trees = []

for x in range(t):
    trees.append([int(x) for x in input().split()])

ans = 0

trees.append([0, 0])
trees.append([n+1,n+1])

t += 2

for a in range(t):
    x1, y1 = trees[a]
    for b in range(t):
        if a == b: continue
        x2, y2 = trees[b]
        if x1 >= x2 or y1 >= y2: continue 
        
        maxsize = min(n-x1, y2-1)
        # print(trees[a], trees[b], maxsize)

        for c in range(t):
            if a == c or b == c: continue
            x3, y3 = trees[c]
            if x3 <= x1 or y3 >= y2: continue

            maxsize = min(maxsize, 
                max(x3 - x1 - 1, y2 - y3- 1)
            )

        if maxsize > ans: ans = maxsize 
        # print(trees[a], trees[b], maxsize)
print(ans)

