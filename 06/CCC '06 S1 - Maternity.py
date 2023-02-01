p1 = input()
p2 = input()

possible = set()

a = [p1[:2], p2[:2]]
b = [p1[2:4], p2[2:4]]
c = [p1[4:6], p2[4:6]]
d = [p1[6:8], p2[6:8]]
e = [p1[8:], p2[8:]]

all = [a, b, c, d, e]

for x in range(5):
    for i in range(2):
        for j in range(2):  
            gene = all[x][0][i]+all[x][1][j]
            if gene.count(chr(65+x)) >= 1:
                possible.add(chr(65+x))
            elif gene.count(chr(97+x)) == 2:
                possible.add(chr(97+x))

def pos(line):
    for x in line:
        if x not in possible:
            return "Not their baby!"
    return "Possible baby."

n = int(input())
for x in range(n):
    line = input()
    print(pos(line))

