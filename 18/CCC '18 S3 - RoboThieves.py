# this is bfs hard mode
# so many implementation details

from collections import deque
import sys; input = sys.stdin.readline 

n, m = [int(x) for x in input().split()]

graph = []

cams = []

convs = []

for x in range(n):
    line = input()
    graph.append(line)
    for y in range(m):
        if line[y] == 'S':
            start = (x,y)
        elif line[y] == 'C':
            cams.append((x,y))
        elif line[y] in ('L', 'R', 'U', 'D'):
            convs.append((line[y], x, y))

q = deque([start])

vis = [[-1] * m for x in range(n)]

vis[start[0]][start[1]] = 0

cnt = 1

cammed = [[0] * m for x in range(n)]

# CAMERAS
# for each camera, loop in all 4 directions
# mark everything is cammed until u hit a wall

for curx, cury in cams:
    cammed[curx][cury] = 1
    for x in range(-1, 2):
        for y in range(-1, 2):

            if (x != 0 and y != 0) or (x == 0 and y == 0): continue

            newx = curx+x ; newy = cury+y

            while (newx >= 0 and newx < n and newy >= 0 and newy < m):
                if graph[newx][newy] == 'W': break 
                if graph[newx][newy] in ('.', 'S'): cammed[newx][newy] = 1

                newx += x ; newy += y 

key = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

# CONVEYORS
# if the conveyor leads into a wall or an infinte loop, return -1
# otherwise return the coords of where the conveyor drops u
# to deal with infinite loops create a visited array to store 
# visited conveyors

# can definitely optimize by memoizing, but im too lazy

def solve(curx, cury, x, y, vis):

    vis.add((curx, cury))

    newx = curx+x ; newy = cury+y

    if not (newx >= 0 and newx < n and newy >= 0 and newy < m): return -1 

    if graph[newx][newy] in ('W', 'C'): return -1

    if graph[newx][newy] in ('L', 'R', 'U', 'D'):
        if (newx, newy) not in vis: return solve(newx, newy, key[graph[newx][newy]][0], key[graph[newx][newy]][1], vis)
        else: return -1

    if graph[newx][newy] in ('.', 'S'): return (newx, newy)

while q:
    for _ in range(len(q)):
        curx, cury = q.popleft()

        if cammed[curx][cury]: continue

        for x in range(-1, 2):
            for y in range(-1, 2):

                if (x != 0 and y != 0) or (x == 0 and y == 0): continue

                newx = curx+x ; newy = cury+y 

                if not (newx >= 0 and newx < n and newy >= 0 and newy < m): continue

                if vis[newx][newy] == -1:
                    if graph[newx][newy] == '.':
                        if cammed[newx][newy] == 0:
                            vis[newx][newy] = cnt
                            q.append((newx,newy))

                    if graph[newx][newy] in ('L', 'R', 'U', 'D'):
                        new = solve(newx, newy, key[graph[newx][newy]][0], key[graph[newx][newy]][1], set())
                        if new != -1:
                            if vis[new[0]][new[1]] == -1:
                                if cammed[new[0]][new[1]] == 0:
                                    vis[new[0]][new[1]] = cnt
                                    q.append((new[0], new[1]))
    cnt += 1

for x in range(n):
    for y in range(m):
        if graph[x][y] == '.':
            print(vis[x][y])
