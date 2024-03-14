def solve(s):
    prv = s.count(s[0]) > 1 
    for x in range(1, len(s)):
        if prv + (s.count(s[x]) > 1) != 1:
            return 'F'
        prv = not prv 
    return 'T'
for x in range([int(x) for x in input().split()][0]): print(solve(input())) 
