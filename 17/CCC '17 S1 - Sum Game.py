n = int(input())

one = [int(x) for x in input().split(" ")]
two = [int(x) for x in input().split(" ")]

highest = 0

sum_one = 0
sum_two = 0
for x in range(n):
    sum_one += one[x]
    sum_two += two[x]

    if sum_one == sum_two:
        highest = x+1

print(highest)