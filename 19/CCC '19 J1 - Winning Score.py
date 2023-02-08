aThree = int(input())
aTwo = int(input())
aOne = int(input())

bThree = int(input())
bTwo = int(input())
bOne = int(input())

if aThree * 3 + aTwo * 2 + aOne > bThree * 3 + bTwo * 2 + bOne:
    print("A")
elif aThree * 3 + aTwo * 2 + aOne < bThree * 3 + bTwo * 2 + bOne:
    print("B")
else:
    print("T")