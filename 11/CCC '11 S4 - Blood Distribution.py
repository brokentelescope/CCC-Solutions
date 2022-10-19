have = [int(x) for x in input().split()]
give = [int(x) for x in input().split()]

have.insert(0, "a")
give.insert(0, "a")

graph = [[0]*18 for x in range(18)]

for x in range(1,9):
    graph[0][x] = have[x] 

for x in range(1,9):
    graph[x+8][-1] = give[x]

#O-
n=1
for x in range(9, 17):
    graph[n][x] = give[x-8]

#O+
n=2 
graph[n][n+8] = float('inf')
graph[n][12] = float('inf')
graph[n][14] = float('inf')
graph[n][16] = float('inf')

#A-
n=3
graph[n][n+8] = float('inf')
graph[n][12] = float('inf')
graph[n][15] = float('inf')
graph[n][16] = float('inf')

#A+
n=4
graph[n][n+8] = float('inf')
graph[n][16] = float('inf')

#B-
n=5
graph[n][n+8] = float('inf')
graph[n][14] = float('inf')
graph[n][15] = float('inf')
graph[n][16] = float('inf')

#B+
n=6
graph[n][n+8] = float('inf')
graph[n][16] = float('inf')

#AB-
n=7
graph[n][n+8] = float('inf')
graph[n][16] = float('inf')

#AB+
n=8
graph[n][n+8] = float('inf')

# for x in graph:
#     print(x)
 
class Graph:
    def __init__(self, graph):
        self.graph = graph
        self. ROW = len(graph)
    def BFS(self, s, t, parent):
        visited = [False]*(self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
        return False
    def FordFulkerson(self, source, sink):
        parent = [-1]*(self.ROW)
        max_flow = 0
 
        while self.BFS(source, sink, parent) :
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow +=  path_flow
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow

g = Graph(graph)
   
print (g.FordFulkerson(0, 17))
 
