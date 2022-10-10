pink = int(input())
green = int(input())
red = int(input())
orange = int(input())

cost = int(input())


sols = []
for p in range(0, cost//pink+1):
    for g in range(0, cost//green+1):
        for r in range(0, cost//red+1):
            for o in range(0, cost//orange+1):
                if p*pink + g*green + r*red + o*orange == cost:
                    sols.append([p, g, r, o])

ticks = []
for x in sols:
    p, g, r, o = x 

    ticks.append(p + g + r + o)
    print(f"# of PINK is {p} # of GREEN is {g} # of RED is {r} # of ORANGE is {o}")

# print(ticks)
print(f"Total combinations is {len(sols)}.")
print(f"Minimum number of tickets to print is {min(ticks)}.")