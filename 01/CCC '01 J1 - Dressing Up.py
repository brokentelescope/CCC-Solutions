layers = int(input())

stars = list(range(1,layers+1,2))

stars.extend(stars[::-1][1:])

for x in range(layers):
    first = "*" * stars[x]
    second = " " * ((layers-stars[x])*2)
    last = "*" * stars[x]

    print(first + second + last)