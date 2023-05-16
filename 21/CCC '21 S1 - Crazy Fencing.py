n = int(input())

heights = [int(x) for x in input().split()]
widths = [int(x) for x in input().split()]

a = 0
for x in range(n):
    a += widths[x]*(heights[x]+heights[x+1])/2

print(a)
