k = int(input())
string = list(input().lower())

alphabet = "zyxwvutsrqponmlkjihgfedcba"

for x in range(len(string)):
    shift_value = (x+1) * 3 + k
    next_letter = (alphabet.index(string[x]) + shift_value) % 26

    string[x] = alphabet[next_letter]

print("".join([x.upper() for x in string]))