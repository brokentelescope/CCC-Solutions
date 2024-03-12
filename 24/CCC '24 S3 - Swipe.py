n = int(input())

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

compressed = []

# compress the array into new array of form (value, left, right)

l = 0
r = 0

while r < n:
    while l < n and r < n and b[l] == b[r]:
        r += 1 
    compressed.append((b[l], l, r-1))
    l = r 

left = []
right = []

i = 0
j = 0
while i < n and j < len(compressed):
    v, l, r = compressed[j]
    if a[i] == v:
        if i > l:
            left.append((l, i))
        if i < r:
            right.append((i, r))
        j += 1
    i += 1

if j == len(compressed):
    print("YES")

    print(len(left)+len(right))
    
    for l, r in left:
        print("L", l, r)
    right.reverse()
    for l, r in right:
        print("R", l, r)
else:
    print("NO")