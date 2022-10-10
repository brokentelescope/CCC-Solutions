flooring, rows, cols = int(input()), int(input()), int(input())
sizes, board, visited, rooms =[], [], [], 0, 

locations = []
def newRoom(r,c):
    #left
    if [r, c-1] in visited:
        return False
    elif board[r][c-1] == ".":
        visited.append([r, c-1])
        return newRoom(r, c-1)
    #right
    if [r, c+1] in visited:
        return False
    elif board[r][c+1] == ".":
        visited.append([r, c+1])
        return newRoom(r, c+1)
    #up 
    if [r-1, c] in visited:
        return False
    elif board[r-1][c] == ".":
        visited.append([r-1, c])
        return newRoom(r-1, c)
    #down
    if [r+1, c] in visited:
        return False
    elif board[r+1][c] == ".":
        visited.append([r+1, c])
        return newRoom(r+1, c)
    return True

def explore(r,c):
    queue = [[r,c]]
    size = 1
    while queue:
        r, c = queue[0]
        try:
            if board[r+1][c] == "." and [r+1,c] not in visited:
                visited.append([r+1,c])
                queue.append([r+1,c])
                size += 1
        except:
            pass

        try:
            if board[r-1][c] == "." and [r-1,c] not in visited:
                visited.append([r-1,c])
                queue.append([r-1,c])
                size += 1
        except:
            pass

        try:
            if board[r][c+1] == "." and [r,c+1] not in visited:
                visited.append([r,c+1])
                queue.append([r,c+1])
                size += 1
        except:
            pass

        try:
            if board[r][c-1] == "." and [r,c-1] not in visited:
                visited.append([r,c-1])  
                queue.append([r,c-1])  
                size += 1
        except:
            pass
        
        queue.pop(0)
        
    return size

for x in range(rows):
    line = list(input())
    board.append(line)

for r in range(1,rows-1):

    for c in range(1,cols-1):
        
        if board[r][c] == "." and [r,c] not in visited:
            visited.append([r,c])
            sizes.append(explore(r,c))
            locations.append([r,c])

# print(locations)
# print(flooring)

sizes.sort(reverse=True)

for x in sizes:
    if flooring-x >= 0:
        flooring -= x
        rooms += 1
    else:
        break

# print(rooms)
# print(flooring)

if rooms == 1:
    print(f"{rooms} room, {flooring} square metre(s) left over")
else:
    print(f"{rooms} rooms, {flooring} square metre(s) left over")
