num = int(input())
hm_shifts = int(input())

sum = num

for x in range(hm_shifts):
    sum += num * 10 ** (x+1)

print(sum)