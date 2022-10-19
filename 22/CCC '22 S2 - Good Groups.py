hm_tog = int(input())

together = {}
apart = {}

violated = 0

for x in range(hm_tog):
    first, second = input().split(" ")

    if first in together.keys():
        together[first].append(second)

    else:    
        together[first] = [second]

hm_apart = int(input())

for x in range(hm_apart):
    first, second = input().split(" ")

    if first in apart.keys():
        apart[first].append(second)

    else:    
        apart[first] = [second]

hm_groups = int(input())

for x in range(hm_groups):
    group = input().split(" ")
    for y in group:

        if y in together.keys():
            for i in together[y]:
                if i not in group:
                    violated += 1

        if y in apart.keys():
            for i in apart[y]:
                if i in group:
                    violated += 1

print(violated)
