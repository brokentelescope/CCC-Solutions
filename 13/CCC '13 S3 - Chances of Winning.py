# this solution it very bad as it checks many duplicate cases
# it still passes since tho
# will try to eliminate the duplicate cases later
import math

t = int(input())
g = int(input()) 

games = {
    (1,2): -1,
    (1,3): -1,
    (1,4): -1,
    (2,3): -1,
    (2,4): -1,
    (3,4): -1,
}

def pb():
    for x in range(1, 5):
        for y in range(1, 5):
            print(games[x][y], end = " ")
        print()

def points(team):
    p = 0
    for x in range(1, 5):
        p += games[team][x]
    return p 

for x in range(g):
    a, b, c, d = [int(x) for x in input().split()]
    if c > d:
        games[(a,b)] = 3
    elif c < d:
        games[(a,b)] = 0
    else:
        games[(a,b)] = 1

def winner(g):
    scores = [0] * 5
    for x in range(1, 4):
        for y in range(x+1, 5):
            if g[(x,y)] == 3:
                scores[x] += 3
            elif g[(x,y)] == 1:
                scores[x] += 1
                scores[y] += 1
            else:
                scores[y] += 3

    if scores[t] == max(scores) and scores.count(scores[t]) == 1:
        return 1 
    return 0 
             

def solve(g):
    sum = 0
    flag = True
    for x in range(1, 4):
        for y in range(x+1, 5):
            if g[(x,y)] == -1:
                flag = False
                a = g.copy()
                a[(x,y)] = 3 
                b = g.copy()
                b[(x,y)] = 1
                c = g.copy()
                c[(x,y)] = 0 
                sum += solve(a)
                sum += solve(b)
                sum += solve(c)
    if flag:
        return winner(g)
    return sum


print(solve(games)//math.factorial(6-g))

