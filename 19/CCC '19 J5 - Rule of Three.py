# pretty braindead brute force solution
# passes CCC test cases

rules = []

for x in range(1,4):
    a, b = input().split()
    rules.append((a,b,x))

steps, src, end = input().split()

steps = int(steps)

q = [(src, [], 0)]

while q:
    s, path, cnt = q.pop()
    if cnt == steps:
        if s == end:
            for x in path:
                print(" ".join([str(x) for x in x]))
            break
        continue

    n = len(s)
    if n > 10:
        continue 

    for x in range(n):
        for a, b, c in rules:
                if s[x:x+len(a)] == a:
                    new = s[:x] + b + s[x+len(a):]
                    newpath = path.copy()
                    newpath.append((c, x+1, new))
                    q.append((new, newpath, cnt+1))
        
    
