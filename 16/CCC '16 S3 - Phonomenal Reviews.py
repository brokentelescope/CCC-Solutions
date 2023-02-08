from collections import deque

n, m = [int(x) for x in input().split()]

pho = [False] * n 
for y in [int(x) for x in input().split()]:
    pho[y] = True

graph = [[] for x in range(n)]

deg = [0] * n
for x in range(n-1):
    a, b = [int(x) for x in input().split()]

    deg[a] += 1 
    deg[b] += 1

    graph[a].append(b)
    graph[b].append(a) 

def prune():
    vis = [0] * n 
    q = deque()
    for x in range(n):
        if deg[x] == 1:
            q.append(x) 
            vis[x] = 1

    while q:
        node = q.popleft() 
        if not pho[node]:
            for x in graph[node]:
                deg[x] -= 1 
                if deg[x] <= 1 and vis[x] != 1:
                    vis[x] = 1
                    q.append(x) 
                deg[node] = 0

prune()

def bfs(u):
    q = deque()
    q.append(u)

    cnt = 0

    vis = [False] * n

    vis[u] = True

    while q:
        for x in range(len(q)):
            cur = q.popleft()
            for next in graph[cur]:
                if vis[next] == False and deg[next] > 0:
                    q.append(next)
                    vis[next] = True 
        
        cnt += 1

    return [cur, cnt-1] 

total = -1
first = -1

for x in range(n):
    if deg[x] > 0:
        if first < 0: 
            first = x
        total += 1 

total = total * 2

print(total-(bfs(bfs(first)[0])[1]))









