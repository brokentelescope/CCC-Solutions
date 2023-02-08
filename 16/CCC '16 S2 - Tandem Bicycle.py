problem = int(input())
hm_citizens = int(input())

dmojistan = [
    int(x) for x in input().split(" ")
]

pegland = [
    int(x) for x in input().split(" ")
]

total = 0

if problem == 1:
    dmojistan.sort()
    pegland.sort()

    for x in range(hm_citizens):
        total += max(dmojistan[x], pegland[x])

else:
    dmojistan.sort()
    pegland.sort(reverse=True)

    for x in range(hm_citizens):
        total += max(dmojistan[x], pegland[x])

print(total)
