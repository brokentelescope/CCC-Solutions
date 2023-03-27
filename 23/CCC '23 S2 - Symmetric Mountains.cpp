# interval dp

n = int(input())

arr = [int(x) for x in input().split()] 

dp = [[0] * n for x in range(n)]

dist = 1


ans = [float('inf')] * n
ans[0] = 0

for x in range(1, n+1):
    a = 0
    b = x 

    while b < n:
        
        if x == 1:
            dp[a][b] = abs(arr[a]-arr[b])
        else:
            dp[a][b] = abs(arr[a] - arr[b]) + dp[a+1][b-1]
        
        ans[x] = min(ans[x], dp[a][b])

        a += 1
        b += 1
        
for x in range(n):
    print(ans[x], end = " ")
