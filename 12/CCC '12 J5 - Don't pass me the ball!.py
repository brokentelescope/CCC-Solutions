import math
j = int(input())

if j < 4:
    print(0)

else:
    print(int(math.factorial(j-1)/(math.factorial(3)*math.factorial((j-4)))))