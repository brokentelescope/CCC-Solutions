n = int(input())
boxes = []
for x in range(n):
    boxes.append(sorted([int(x) for x in input().split()]))
boxes.sort(key=lambda x: x[0] * x[1] * x[2])

# print(boxes)
m = int(input())
items = []
for x in range(m):
    items.append(sorted([int(x) for x in input().split()]))

def solve(item):
    for box in range(n):
        if boxes[box][0] >= item[0] and boxes[box][1] >= item[1] and boxes[box][2] >= item[2]:
            return boxes[box][0] * boxes[box][1] *  boxes[box][2]
    return "Item does not fit."

for x in range(m):
    print(solve(items[x]))