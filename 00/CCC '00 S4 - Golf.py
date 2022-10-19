from collections import deque

dist = int(input())
hm_clubs = int(input())
clubs = []

for x in range(hm_clubs):
    clubs.append(int(input()))

def golf(dist,clubs):
    
    queue = []
    queue.append(0)
    steps = 0
    visited = [False] * 5281
    
    while queue:
        for x in range(len(queue)):
            node = queue[0]
        
            if node == dist:
                return f"Roberta wins in {steps} strokes."

            for x in clubs:
                if node+x <= dist:
                    if not visited[node+x]:
                        queue.append(node+x)
                        visited[node+x] = True
            
            queue.pop(0)
        steps += 1

    return "Roberta acknowledges defeat."

print(golf(dist, clubs))
