def find_sites(line):
    found = False 
    curstring = ""
    sites = []
     
    for x in line:
        if found:
            if x == '"':
                sites.append(curstring)
                curstring = ""
                found = False 
            else:
                curstring += x 
        else:
            if x == '"':
                found = True 
    return sites 

def new_site(site, cnt):
    if site not in site_names:
        site_names.add(site)
        key[site] = cnt
        return True 
    return False 

def bfs(x, y):
    q = [x] 

    vis = [False] * 1000
    while q:
        node = q.pop()

        if node == y:
            return True 

        for x in graph[node]:
            if not vis[x]:
                vis[x] = True 
                q.append(x) 

    return False 

n = int(input())

graph = [[] for x in range(1000)]

output = []
cnt = 0
key = {}
site_names = set()

for x in range(n):
    site = input()
    if new_site(site, cnt): cnt += 1

    while True:
        line = input()
        if line == "</HTML>": break 

        for x in find_sites(line):
            output.append(f"Link from {site} to {x}")
            if new_site(x, cnt): cnt += 1
            graph[key[site]].append(key[x])

while True:
    a = input()
    if a == "The End": break 
    b = input()

    if bfs(key[a], key[b]):
        output.append(f"Can surf from {a} to {b}.")
    else:
        output.append(f"Can't surf from {a} to {b}.")

for x in output:
    print(x)
    
