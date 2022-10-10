graph = {1:[]}

target = int(input())
#SET UP GRAPH
while True:
    x, y = [int(x) for x in input().split()]

    if x == 0 and y == 0:
        break

    else:
        if y not in graph.keys():
            graph[y] = []
        if x not in graph.keys():
            graph[x] = []

        graph[x].append(y)

visited = {}
def paths(graph, point):
    sum = 0

    for x in graph[point]:

        if x == target:
            sum += 1
        
        else:
            if x in visited.keys():
                sum += visited[x]
            else:
                sum += paths(graph, x)
                visited[x] = paths(graph, x)

    return sum

print(paths(graph, 1))
    
