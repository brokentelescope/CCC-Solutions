n = int(input())

cnt = 0

for x in range(n//4+1):
    if (n-4*x) % 5 == 0:
        cnt += 1

print(cnt)


    
    
