k = int(input())

d = {}

for x in range(k):
    a, b = input().split()
    d[b] = a 

line = input()

n = len(line)

l = 0
r = 0

ans = ""
while l < n and r < n:
    if line[l:r+1] in d.keys():
        ans += d[line[l:r+1]]
        l = r+1
        r = l
    else:
        r += 1
print(ans)
