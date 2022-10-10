number = "9780921418"
for x in range(3):
    number += input()
times_one = number[0::2]
times_three = number[1::2]

sum = 0
for x in times_one:
    sum += int(x)

for x in times_three:
    sum += int(x) * 3
    
print(f"The 1-3-sum is {sum}")
