import math
infinity = math.inf
import sys
input = sys.stdin.readline
graph = [ 
]


n = int(input())
m = int(input())

# n, m = [int(x) for x in input().split()]

for x in range(n):
    graph.append([0] * n)

for x in range(m):
    a, b, c = [int(x) for x in input().split()] 
    if graph[a-1][b-1] != 0:
        if graph[a-1][b-1] > c:
            graph[a-1][b-1] = c 
            graph[b-1][a-1] = c
    else:
        graph[a-1][b-1] = c 
        graph[b-1][a-1] = c

pens = [False] * n
for x in range(int(input())):
    city, cost = [int(x) for x in input().split()] 
    pens[city-1] = cost 

src = int(input())-1
dist = [infinity] * n
dist[src] = 0


vis = [False] * n

cnt = 0


for x in range(n):
    # find unvisited node with min dist 
    min = infinity
    for y in range(n):
        if dist[y] < min and not vis[y]:
            min = dist[y]
            node = y 
    
    vis[node] = True

    for v in range(n):
        if graph[node][v] > 0 and not vis[v] and dist[v] > dist[node] + graph[node][v]:
            dist[v] = dist[node] + graph[node][v]

min = infinity 
for x in range(n):
    if dist[x] != infinity:
        if pens[x] != False:
            if dist[x] + pens[x] < min:
                min = dist[x] + pens[x]
print(min)
