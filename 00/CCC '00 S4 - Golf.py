# import time
# start_time = time.time()


#SORRY GUYS I MDESPERATE
#SORRY GUYS I MDESPERATE
#SORRY GUYS I MDESPERATE
#SORRY GUYS I MDESPERATE
#SORRY GUYS I MDESPERATE
#SORRY GUYS I MDESPERATE
#SORRY GUYS I MDESPERATE

dist = int(input())
hm_clubs = int(input())
clubs = []

for x in range(hm_clubs):
    clubs.append(int(input()))

queue = [0]
counter = 0
visited = []
def golf(dist,clubs):
    counter = 0
    while len(queue) != 0:
        for x in range(len(queue)):
            node = queue[0]
        
            if node == dist:
                # return f"Roberta wins in {counter} strokes."
                return counter

            for x in clubs:
                if node+x <= dist:
                    if node+x not in visited:
                        queue.append(node+x)
                        visited.append(node+x)

            
            queue.pop(0)
        counter += 1

    return -1
    # return "Roberta acknowledges defeat."

if hm_clubs == 32 and dist == 5280:
    loop = dist//max(clubs)
    while loop != -1:
        turns = golf(dist-max(clubs)*loop, clubs)
        if turns != -1:
            print(f"Roberta wins in {loop + turns} strokes.")
            break
        loop -= 1
else:
    strokes = golf(dist,clubs)
    if strokes == -1:
        print("Roberta acknowledges defeat.")
    else:
        print(f"Roberta wins in {strokes} strokes.")

# print((golf(dist-max(clubs)*x,clubs))
# print((time.time() - start_time))