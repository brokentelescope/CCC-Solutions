constraints = {1:[2], 2:[], 3:[], 4:[1,3], 5:[3], 6:[], 7:[1]}

completed = []

while True:
    one = int(input())
    two = int(input())

    if one == 0 and two == 0:
        break

    constraints[two].append(one)

for x in range(7):
    for x in range(1,8):
        if len(constraints[x]) == 0 and x not in completed:
            completed.append(x)

            for y in range(1,8):
                if x in constraints[y]:
                    constraints[y] = [z for z in constraints[y] if z != x]
            
            break

if len(completed) == 7:
    print(" ".join([str(x) for x in completed]))

else:
    print("Cannot complete these tasks. Going to bed.")


        
    
                




