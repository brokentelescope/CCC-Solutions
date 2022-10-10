x = int(input())
m = int(input())

try:
    n = pow(x, -1, m)
    print(n)
except:
    print("No such integer exists.")