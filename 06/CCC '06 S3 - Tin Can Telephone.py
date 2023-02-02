# represent the lines in form of ax + by + c
# and use formulas to find the intersection of lines

# https://dmoj.ca/problem/dmopc19c6p1/editorial

# this is very helpful ^^^^

X1, Y1, X2, Y2 = [int(x) for x in input().split()]

A1 = Y1 - Y2
B1 = X2 - X1
C1 = -(A1 * X1 + B1 * Y1)

n = int(input())

def check(x1, y1, x2, y2):
    if x1 > x2:
        x1, x2 = x2, x1 
    if y1 > y2:
        y1, y2 = y2, y1 

    A2 = y1 - y2
    B2 = x2 - x1
    C2 = -(A2 * x1 + B2 * y1)

    if (A1 * B2 == A2 * B1):
        if (B1 * C2 == B2 * C1):
            if x1 > max(X1, X2) or x2 < min(X1,X2):
                return False
            if y1 > max(Y1, Y2) or y2 < min(Y1, Y2):
                return False
            return True
        return False

    x = (B1 * C2 - B2 * C1)/(B2 * A1 - B1 * A2)
    y = (A1 * C2 - A2 * C1)/(A2 * B1 - A1 * B2)

    if x < x1 or x > x2:
        return False 
    if y < y1 or y > y2:
        return False

    if x < X1 or x > X2:
        return False 
    if y < Y1 or y > Y2:
        return False

    return True 

ans = 0
for x in range(n):
    building = [int(x) for x in input().split()]
    e = building[0]
    building.pop(0)

    for y in range(0, e*2-1, 2):
        a, b = building[y], building[y+1]
        if y == e*2-2:
            c, d = building[0], building[1]
        else:
            c, d = building[y+2], building[y+3]
        if check(a,b,c,d):
            ans += 1
            break 
print(ans)
