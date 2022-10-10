a = 100
b = 100
rounds = int(input())
points = []
for x in range(rounds): 
    points.append(input().split(" "))
for y in range(rounds):
    if (int(points[y][0])) > (int(points[y][1])):
        b -= (int(points[y][0]))
    elif (int(points[y][0])) < (int(points[y][1])):
        a -= (int(points[y][1]))
print(a)
print(b)