graph = []

for x in range(10):
    graph.append(input().split())

def val(r, c, vis=[]):
    if graph[r][c].isnumeric(): 
        return int(graph[r][c])
    
    sum = 0
    for x in graph[r][c].split("+"):
        xx = ord(x[0])-65
        yy = int(x[1])-1

        #this probably shouldn't work 
        #try to implement an actual loop detection system
        
        if vis.count([xx, yy]) < 10:
            vis.append([xx, yy])
            sum += val(xx, yy, vis)
        else:
            if not graph[r][c].isnumeric():
                sum = 1000000001
                break
                
    graph[r][c] = str(sum)

    return sum 

for x in range(10):
    for y in range(9):
        val(x,y,[])

for x in range(10):
    for y in range(9):
        if int(graph[x][y]) > 1000000000:
            graph[x][y] = "*"

for x in graph:
    print(" ".join(x))

