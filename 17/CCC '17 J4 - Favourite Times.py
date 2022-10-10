first = [x for x in range(2)]
second = [x for x in range(10)]
third = [x for x in range(6)]
fourth = [x for x in range(10)]
fav_times = []
print(first)
print(second)
print(third)
print(fourth)

for a in first:
    if a == 0:
        for b in second:
            for c in third:
                for d in fourth:
                    if a - b == b - c and b - c == c - d:
                        fav_times.append([a,b,c,d])
    else:
        for b in second[0:3]:
            for c in third:
                for d in fourth:
                  if a - b == b - c and b - c == c - d:
                        fav_times.append([a,b,c,d])

print(fav_times)