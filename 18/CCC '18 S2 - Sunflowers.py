n = int(input())

arr = []

for x in range(n):
    arr.append([int(x) for x in input().split()])

for _ in range(4):

    arr = list(zip(*arr[::-1]))

    for x in range(n):
        prev = 0
        wrong = False
        
        if [x[0] for x in arr] != sorted([x[0] for x in arr]):
            wrong = True

        if wrong:
            break

        for y in range(n):
            if arr[x][y] < prev:
                wrong = True
                break 
            prev = arr[x][y]

    if not wrong:
        for x in arr:
            print(" ".join([str(num) for num in x]))
    

