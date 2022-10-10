graph = {
    }

roads = [
    ]

dc = [
    ]

while 1:
    road = input()

    if road == "**":
        break
        
    else:
        roads.append(road)
        try:
            graph[road[0]].append(road[-1])
        except:
            graph[road[0]] = [road[-1]]
        
        try:
            graph[road[-1]].append(road[0])
        except:
            graph[road[-1]] = [road[0]]

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: 
                return True
    return False

for x in roads:
    start, second = x[0], x[-1]

    graph[start].remove(second)
    graph[second].remove(start)

    if find_path(graph, "A", "B") ==  False:
        dc.append(x)

    graph[start].append(second)
    graph[second].append(start)


for x in range(len(dc)):
    print(dc[x])

print(f"There are {len(dc)} disconnecting roads.")