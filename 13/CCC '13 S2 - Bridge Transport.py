w = int(input())
n = int(input())

cars = [0] * 3 

for x in range(n):
    cars.append(int(input()))
cars.append(100001) 

x = 3
cnt = 0

weight = cars[x] + cars[x-1] + cars[x-2] + cars[x-3] 

while weight <= w:
    x += 1 
    cnt += 1 

    weight = cars[x] + cars[x-1] + cars[x-2] + cars[x-3]  

print(cnt)