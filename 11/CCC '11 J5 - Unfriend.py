n = int(input())
invited_by = {} 
possible = {}
invited = []
for x in range(1,n):
    ind = int(input())
    invited_by[x] = ind
    invited.append(ind)


for x in range(1,n+1):
    count = 1
    if x in invited:
        #FIND COUNTS OF PEOPLE THEY INVITED

        for y in range(len(invited)):
            if invited[y] == x:
                count *= possible[y+1]
                
        
        possible[x] = count + 1

    else:
        count = 2
        possible[x] = count

print(possible[n]-1)