parent = list(range(100001)) 

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def unionn(x, y):
    parent[find(x)] = find(y)


n, m, k = [int(x) for x in input().split()] 

edges = [] 


for x in range(1,m+1):
    a, b, c = [int(x) for x in input().split()] 

    if x >= n:
        edges.append((c, 1, a, b)) 
    else:
        edges.append((c, 0, a, b))

edges.sort(key=lambda x: (x[0], x[1]))

ans = 0

for x in range(m):
    w, new, a, b = edges[x]
    e = edges[x]

    if find(a) != find(b):
        unionn(a, b)
        # keep track of the last edge
        last = x
        lastw = w
        ans += new

if edges[last][1] and lastw <= k:
    # reset parent arr
    parent = list(range(100001)) 


    for x in range(last):
        w, new, a, b = edges[x]
        if (new == 0 or w < lastw):
            unionn(a, b)
    
    for x in range(last+1, m):
        w, new, a, b = edges[x]
        if new == 0 and w <= k:
            if find(a) != find(b):
                ans -= 1
                break

print(ans)
