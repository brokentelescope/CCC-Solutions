root = [0] * 100001

def find(x): 
    if x!=root[x]:
        root[x] = find(root[x])
    return root[x]

def merge(x,y): 
    root[find(x)] = find(y)

g = int(input())
p = int(input())
for i in range(1,g+1):
    root[i] = i
i = 0
kontinue = True
while i < p and kontinue:
    wanted = int(input())
    root = find(wanted)
    if root == 0:
        print(i)
        kontinue = False 
    merge(root,root-1)
    i = i + 1
if kontinue:    
    print(p)