play = ["A", "B", "C", "D", "E"]

while True:
    move = int(input())
    n = int(input())

    if move == 4:
        break

    if move == 1:
        for x in range(n):
            play[0], play[1], play[2], play[3], play[4] = play[1], play[2], play[3], play[4], play[0]
    
    elif move == 2:
        for x in range(n):
            play[0], play[1], play[2], play[3], play[4] = play[4], play[0], play[1], play[2], play[3]
    
    else:
        for x in range(n):
            play[0], play[1], play[2], play[3], play[4] = play[1], play[0], play[2], play[3], play[4]

print(" ".join(play))