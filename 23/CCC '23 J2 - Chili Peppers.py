ans = 0
spice = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000
}

for x in range(int(input())):
    ans += spice[input()]

print(ans)