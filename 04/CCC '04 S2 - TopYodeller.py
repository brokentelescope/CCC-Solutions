hm_yodellers , hm_rounds = [int(x) for x in input().split(" ")]

yodellers = [0] * hm_yodellers
worst = [1] * hm_yodellers
current = [0] * hm_yodellers
for x in range(hm_rounds):
    scores = [int(x) for x in input().split(" ")]
    for x in range(hm_yodellers):
        yodellers[x] += scores[x]
    for x in range(hm_yodellers):
        rank = 1
        for y in range(hm_yodellers):
            if x != y and yodellers[x] < yodellers[y]:
                rank += 1
        if rank > worst[x]:
            worst[x] = rank
        current[x] = rank
        
for x in range(hm_yodellers):
    if current[x] == 1:
        print(f"Yodeller {x+1} is the TopYodeller: score {yodellers[x]}, worst rank {worst[x]}")
