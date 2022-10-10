from collections import deque

import sys 
input = sys.stdin.readline

rows = int(input())
columns = int(input())

positions = [False] * 1000001

for r in range(1,rows+1):
    row = [int(x) for x in input().split(" ")]

    for c in range(1, columns+1):
        try:
            positions[row[c-1]].append([r, c])
        except:
            positions[row[c-1]] = [[r,c]]

def bfs():
    queue = deque()
    
    queue.append([rows, columns])
    visited = []

    for x in range(rows+1):
        visited.append([False] * (columns+1))
    
    visited[rows][columns] = True

    visitednums = [False] * 1000001

    while queue:
        for x in range(len(queue)):
            node = queue.popleft()
            target_r = node[0]
            target_c = node[1]

            if target_r == 1 and target_c == 1:
                return "yes"

            target = target_r * target_c 

            if target <= 1000000:
                if not visitednums[target]: 
                    visitednums[target] = True

                    if positions[target]:
                        for y in positions[target]:

                            if not visited[y[0]][y[1]]:
                                queue.append(y)
                                visited[y[0]][y[1]] = True

    return "no" 

print(bfs())