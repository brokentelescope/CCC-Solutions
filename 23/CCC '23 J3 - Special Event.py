n = int(input())

guests = [0] * 5

for x in range(n):
    line = input()
    for y in range(5):
        guests[y] += int(line[y] == 'Y')

max = -1 
ans = []

for x in range(5):
    if guests[x] > max:
        max = guests[x]
        ans = [str(x+1)]
    elif guests[x] == max:
        ans.append(str(x+1))

print(",".join(ans))