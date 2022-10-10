graph = {1: [6], 2: [6], 3: [4, 5, 6, 15], 4: [3, 5, 6], 5: [3, 4, 6], 6: [1, 2, 3, 4, 5, 7], 7: [6, 8], 8: [7, 9], 9: [8, 10, 12], 10: [9, 11], 11: [10, 12], 12: [9, 11, 13], 13: [12, 14, 15], 14: [13], 15:[3,13], 16:[17,18], 17:[16,18], 18:[16,17]}

# def shortest(graph, x, y):
#     counter = 1
#     queue = [x]
    
#     counter = 0
    
#     while len(queue) > 0 and counter < len(graph):
        
#         for x in range(len(queue)):
#             node = queue[0]
            
#             if y in graph[node]:
#                 return counter
            
#             else:
#                 counter += 1 
                
#                 for x in range(len(graph[node])):
#                     queue.append(graph[node][x])
#             queue.pop(0)

def shortest(graph, start, goal):
    explored = []
     
    queue = [[start]]
     
    if start == goal:
        print("Same Node")
        return
     
    while queue:
        path = queue.pop(0)
        node = path[-1]
         
        if node not in explored:
            neighbours = graph[node]
             
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                 
                if neighbour == goal:
                    return (len(new_path)-1)

            explored.append(node)

    return False
    
while True:
    command = input()
    
    if command == "q":
        break
    
    else:
        
        if command == "i":
            friend1 = int(input())
            friend2 = int(input())
            
            if friend1 in graph.keys():
                graph[friend1].append(friend2)
            
            else:
                graph[friend1] = [friend2]
                
            if friend2 in graph.keys():
                graph[friend2].append(friend1)
            
            else:
                graph[friend2] = [friend1]
                
        elif command == "d":
            friend1 = int(input())
            friend2 = int(input())
            
            try: 
                graph[friend1].remove(friend2)
                graph[friend2].remove(friend1)
            
            except:
                pass
            
        elif command == "n":
            friend = int(input())
            # print(len(graph[friend]))
            print(f"output {len(graph[friend])}")

        elif command == "f":
            friend = int(input())
            
            sum = 0
            visited = []

            for x in graph[friend]:
                for y in graph[x]:
                    if y in visited or y in graph[friend] or y == friend:
                        pass
                    else:
                        sum += 1
                        visited.append(y)

            # print(sum)
            print(f"output {sum}")
        elif command == "s":
            friend1 = int(input())
            friend2 = int(input())
            
            # print(shortest(graph, friend1, friend2))
            print(f"output {shortest(graph, friend1, friend2)}")