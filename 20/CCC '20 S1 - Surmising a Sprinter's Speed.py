n = int(input())
times = []
for x in range(n):
    times.append([int(x) for x in input().split()])
times.sort(key=lambda x: x[0])

max = 0
for x in range(n-1):
    distance = abs(times[x][-1] - times[x+1][-1])
    time = times[x+1][0] - times[x][0]
    # print(distance, end=" ")
    # print(time)

    if distance/time > max:
        max = distance/time
print(max)