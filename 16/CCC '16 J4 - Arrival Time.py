hrs, mins = [int(x) for x in input().split(":")]

time = 60*hrs+mins

dist = 0
while dist != 120:
    if (time >= 420 and time < 600) or (time >= 900 and time < 1140): 
        time += 2
    else:
        time += 1 

    dist += 1

time = time %  1440 

hrs = time//60
mins = time % 60 

if hrs < 10:
    hrs = "0" + str(hrs)

if mins < 10:
    mins = "0" + str(mins)

hrs = str(hrs)
mins = str(mins)

print(hrs+":"+mins)