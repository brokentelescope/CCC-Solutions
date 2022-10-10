import sys
sys.setrecursionlimit(15000)


input = sys.stdin.readline

def circle(friends, x, y, counter):
    if counter > len(friends):
        return "No"

    if friends[x] == y:
        return "Yes " + str(counter)

    return circle(friends, friends[x], y, counter + 1)

hm_friends = int(input())

friends = {}

for x in range(hm_friends):
    beta, chad = [int(x) for x in input().split(" ")]
    friends[beta] = chad

while True:
    test = input()
    if test == "0 0\n":
        break
    
    first, second = [int(x) for x in test.split(" ")]

    print(circle(friends, first, second, 0))