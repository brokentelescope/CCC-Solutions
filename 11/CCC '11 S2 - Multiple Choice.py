n = int(input())
questions = []
for x in range(n * 2):
    questions.append(input())
first = questions[:n]
second = questions[n:]
ans = 0
for x in range(n):
    if first[x] == second[x]: ans += 1 
print(ans)
