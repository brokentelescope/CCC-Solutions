import math
# hm_chips = int(input())
chips = []
def obtuse(a, b, c):
    if a*a + b*b < c*c:
        return c 
    if b*b + c*c < a*a:
        return a
    if c*c + a*a < b*b:
        return b 
    return -1

def heron(a, b, c):
    # ax, ay = a
    # bx, by = b 
    # cx, cy = c

    # d1 = math.sqrt((ax-bx)*(ax-bx) + (ay-by)*(ay-by)) 
    # d2 = math.sqrt((bx-cx)*(bx-cx) + (by-cy)*(by-cy)) 
    # d3 = math.sqrt((cx-ax)*(cx-ax) + (cy-ay)*(cy-ay)) 

    # a, b, c = d1, d2, d3
    print(a, b, c)
    s = (a+b+c)/2 

    #check if its an obtse triangle bc ucant have circumscribed circle if its obtuse or smt idfk 
    if obtuse(a,b,c) != -1:
        return obtuse(a,b,c)

    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    # print(area)
    if area == 0:
        return 0
    radius = (a*b*c)/(4*area)

    return radius*2

# chips = []
# n = int(input())
# for x in range(n):
#     chips.append([int(x) for x in input().split()])

# ans = 0
# for x in range(n):
#     for y in range(1,n):
#         for z in range(2,n):
#             if heron(chips[x], chips[y], chips[z]) > ans:
#                 ans = heron(chips[x], chips[y], chips[z])
# print(round(ans,2))

print(heron(1.00, 1.41, 1.00))

