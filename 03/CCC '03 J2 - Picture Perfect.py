import math
def factor(n):
    pairs = []
    for x in range(1, int(math.sqrt(n))+1):
        if n % x == 0:
            t = n//x 
            pairs.append([x, t])
    return pairs

while True:
    n = int(input())
    if n == 0:
        break 
    ans = factor(n)
    ans.sort(key = lambda x: x[0] + x[1])
    x, y = ans[0]

    print(f"Minimum perimeter is {x*2+y*2} with dimensions {x} x {y}")
    