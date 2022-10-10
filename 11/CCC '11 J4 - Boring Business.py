x = -1
y = -5
visited = [[x,y], [0,-1], [0,-2], [0,-3], [1,-3], [2,-3], [3,-3], [3,-4], [3,-5], [4,-5], [5,-5], [6,-3], [7,-3], [7,-4], [7,-5], [7,-6], [7,-7], [6,-7], [5,-7], [4,-7], [3,-7], [2,-7], [1,-7], [0,-7], [-1,-7], [-1,-6], [-1,-5]]
safe = True


while safe:
    command = input().split(" ")

    if command == ["q", "0"]:
        break

    dir, dist = command[0], int(command[1])
    
    if dir == "l":

        end_x = x - dist

        for i in range(dist):
            x -= 1

            if [x,y] not in visited:
                visited.append([x,y])

            else:
                print(str(end_x) + " " + str(y) + " DANGER")
                safe = False
                break
        
        if safe:
            print(str(end_x) + " " + str(y) + " safe")
        
    if dir == "r":

        end_x = x + dist
        
        for i in range(dist):
            x += 1

            if [x,y] not in visited:
                visited.append([x,y])

            else:
                print(str(end_x) + " " + str(y) + " DANGER")
                safe = False
                break
        
        if safe:
            print(str(end_x) + " " + str(y) + " safe")

    if dir == "u":

        end_y = y + dist

        for i in range(dist):
            y += 1

            if [x,y] not in visited:
                visited.append([x,y])

            else:
                print(str(x) + " " + str(end_y) + " DANGER")
                safe = False
                break
        
        if safe:
            print(str(x) + " " + str(end_y) + " safe")

    if dir == "d":

        end_y = y - dist

        for i in range(dist):
            y -= 1

            if [x,y] not in visited:
                visited.append([x,y])

            else:
                print(str(x) + " " + str(end_y) + " DANGER")
                safe = False
                break
        
        if safe:
            print(str(x) + " " + str(end_y) + " safe")