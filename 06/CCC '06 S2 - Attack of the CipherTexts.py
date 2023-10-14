plain = input()
corres = input()
decode = input()

code = {
}

keySet = []
valSet = []

for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
    keySet.append(x)
    valSet.append(x)

for x in range(len(plain)):
    code[corres[x]] = plain[x]
    if corres[x] in keySet: keySet.remove(corres[x])
    if plain[x] in valSet: valSet.remove(plain[x])

if (len(keySet) == 1):
    code[keySet[0]] = valSet[0]

output = ""

for x in range(len(decode)):
    if decode[x] in code.keys():
        output += code[decode[x]]
    else:
        output += "."

print(output)
