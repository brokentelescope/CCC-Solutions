start, days = [int(x) for x in input().split(" ")]

print("Sun Mon Tue Wed Thr Fri Sat")


day = 1

distr = []

line = []
for x in range(day,7-start+2):
    line.append(x)
    day += 1

distr.append(line)

line = []

for x in range(day, day+7):
    line.append(x)
    day += 1
distr.append(line)

line = []
for x in range(day, day+7):
    line.append(x)
    day += 1
distr.append(line)

line = []
for x in range(day, day+7):
    line.append(x)
    day += 1
distr.append(line)

line = []
for x in range(day, min(days+1, day+7)):
    line.append(x)
    day += 1
distr.append(line)

line = []
for x in range(day, min(days+1, day+7)):
    line.append(x)
distr.append(line)

print("  " + "    " * (start-1), end="")
print("   ".join(
        [str(x) for x in distr[0]]
        ))

line = "  "
line += str(distr[1][0])

for x in distr[1][1:]:
    if x < 10:
        line += "   "
        line += str(x) 
    
    else:
        line += "  "
        line += str(x)

print(line)

if distr[2][0] < 10:
    line = "  "
else:
    line = " "
line += str(distr[2][0])

for x in distr[2][1:]:
    line += "  "
    line += str(x)

print(line)

line = " "
line += str(distr[3][0])

for x in distr[3][1:]:
    line += "  "
    line += str(x)

print(line)

try:
    line = " "
    line += str(distr[4][0])

    for x in distr[4][1:]:
        line += "  "
        line += str(x)

    print(line)

except:
    pass

try:
    line = " "
    line += str(distr[5][0])

    for x in distr[5][1:]:
        line += "  "
        line += str(x)

    print(line)

except:
    pass