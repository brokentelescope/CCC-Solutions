num_of_adj = int(input())
num_of_noun = int(input())

adjs = []
nouns = []

for x in range(num_of_adj):
    adjs.append(input())

for x in range(num_of_noun):
    nouns.append(input())

for x in adjs:
    for y in nouns:
        print(f"{x} as {y}")
