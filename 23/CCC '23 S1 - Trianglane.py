n = int(input())

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

ans = 3 * (a.count(1) + b.count(1)) 

for x in range(n):
    if a[x] == 1:
        if x + 1 < n and a[x+1] == 1:
            ans -= 2
        if x % 2 == 0 and b[x] == 1:
            ans -= 2
    if b[x] == 1:
        if x + 1 < n and b[x+1] == 1:
            ans -= 2
    
print(ans)
    