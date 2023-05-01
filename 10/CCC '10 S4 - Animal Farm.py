# hardest part of this problem is creating the graph 

# we must create a graph using the edges between pens,
# not the edges between pen corners (the ones given in the input)

# the pens are numbered 1 to n, with 0 being outside
# if an input pen ()

# sample input first pen 

# num of edges: 3 
# pen corners: 1, 2, 3
# edge costs:  7, 4, 6

# from this pen we can create 3 edges (node1, node2, cost):
# (1, 2, 7), (2, 3, 4) and (3, 1, 6)

# use a map to keep track of these edges and which pens have this edge
# if only one have this edge, it is a connection between a pen and outside
# if two pens have this edge, it is a connection between two pens
# using this information we can create the real graph 

# after creating the graph, we can use kruskal's algorithm to find the minimum spanning tree
# however, we must check for if the animals meet inside a large group of pens,
# or if the animals meet outside (in some cases this is the only option)
# then we return the miniumum of these two answers

n = int(input())

graph = [[] for x in range(n+1)]

# edges between pen corners
edges = []

# map to keep track of which pens have which edges
edge_to_nodes = {}

for p in range(1, n+1):
    pen = [int(x) for x in input().split()] 
    e = pen[0]

    vertices = pen[1:e+1]
    costs = pen[e+1:]

    for x in range(e):
        a = vertices[x]
        b = vertices[(x+1)%e]

        c = costs[x]

        a, b = min(a, b), max(a,b)
        
        edges.append((a, b, c))
        if (a, b, c) in edge_to_nodes:
            edge_to_nodes[(a, b, c)].append(p)
        else:
            edge_to_nodes[(a, b, c)] = [p]

# edges between pens
true_edges = []

outside_edges = []
for a, b, c in edges:
    if len(edge_to_nodes[(a, b, c)]) == 1:
        v = edge_to_nodes[(a, b, c)][0]
        graph[0].append((v, c))
        graph[v].append((0, c))
        outside_edges.append((0, v, c))

    else:
        v = edge_to_nodes[(a, b, c)][0]
        z = edge_to_nodes[(a, b, c)][1]
        graph[v].append((z, c))
        graph[z].append((v, c))
        true_edges.append((v, z, c))

parent = list(range(n+1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(x)] = find(y)

true_edges.sort(key = lambda x: x[2])

ans1 = 0

cnt = 0

# meet inside
for a, b, c in true_edges:
    if find(a) != find(b):
        union(a, b)
        ans1 += c 
        cnt += 1

# if the number of edges isn't n-1, meeting inside is impossible
if cnt != n-1:
    ans1 = float('inf')

# meet outside
parent = list(range(n+1))
true_edges.extend(outside_edges)
true_edges.sort(key = lambda x: x[2])

ans2 = 0
cnt = 0
for a, b, c in true_edges:
    if find(a) != find(b):
        union(a, b)
        ans2 += c 
        cnt += 1

print(min(ans1, ans2))
