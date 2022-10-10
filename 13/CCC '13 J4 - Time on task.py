hm_time = int(input())
hm_chores = int(input())
chores = []
counter = 0

for x in range(hm_chores):
    chores.append(int(input()))

chores.sort(reverse=True)

while True:
    if hm_time - chores[-1] >= 0:
        hm_time -= chores[-1]
        chores.pop()
        counter += 1
    else:
        break
    
print(counter)