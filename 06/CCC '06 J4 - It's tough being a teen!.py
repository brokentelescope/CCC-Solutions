c = [[] for x in range(8)]

c[1] = [2]
c[4] = [1, 3]
c[5] = [3]
c[7] = [1]

while 1:
    a, b = int(input()), int(input())

    if a == 0 and b == 0: break 

    c[b].append(a)

for x in range(1, 8):
    c[x].sort()

ans = []

for _ in range(7):
    for x in range(1, 8):
        if str(x) not in ans:
            if not c[x]:
                ans.append(str(x))
                for y in range(1, 8):
                    if x in c[y]:
                        c[y].remove(x)
                break

if len(ans) == 7:
    print(" ".join(ans))
else:
    print("Cannot complete these tasks. Going to bed.")
