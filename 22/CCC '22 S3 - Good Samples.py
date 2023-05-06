import sys

n, m, k = [int(x) for x in input().split()]

ans = [-1] * (n+1)
last = [0] * (n+1)

last[1] = 1
ans[1] = 1

target = k-n 

if (n*(n+1))/2 - (n-m)*(n-m+1)/2 < k or n > k:
    print(-1)
    sys.exit()

for x in range(2, n+1):
    next = ans[x-1] + 1
    if next > m: next = 1

    g = x - last[next] - 1

    if g <= target:
        ans[x] = next
        target -= g 
    else:
        ans[x] = ans[x-(target+1)]
        target = 0
    last[ans[x]] = x 

for x in range(1, n+1):
    print(ans[x], end = " ")



