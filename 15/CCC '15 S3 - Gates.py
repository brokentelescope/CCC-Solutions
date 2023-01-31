# store free gates in a list
# assign each plane to the highest possible gate
# use binary search to find the highest possible gate
# if it is index 0, no gates left
# otherwise, remove that gate from the list 

import bisect

g = int(input())

p = int(input())

free = list(range(1, g+1))

ans = 0
for x in range(p):
    # print(free)
    plane = int(input())

    idx = bisect.bisect_right(free, plane)
    # print(idx)

    if idx == 0:
        break

    free.pop(idx-1)

    ans += 1

print(ans)
