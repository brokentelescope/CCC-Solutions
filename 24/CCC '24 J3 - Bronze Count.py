s = []
for x in range(int(input())):
    s.append(int(input()))
print(sorted(list(set(s)), reverse=1)[2], s.count(sorted(list(set(s)), reverse=1)[2]))