n = int(input())

ranks = []

if n != 0:
    for x in range(n):
        name, a, b, c = input().split()
        a = int(a); b = int(b); c = int(c) 
        score = 2*a+3*b+c 
        ranks.append((-score, name)) 

    ranks.sort(key=lambda x: (x[0], x[1]))

    if n == 1:
        print(ranks[0][1])
    else:
        print(ranks[0][1])
        print(ranks[1][1])