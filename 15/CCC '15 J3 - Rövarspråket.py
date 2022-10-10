letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
cons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]

vowel_indexes = [0, 4, 8, 14, 20, 0]

word = list(input())

for x in word:
    if x in vowels:
        pass

    else:
        for y in range(5):
            if abs(letters.index(x) - vowel_indexes[y]) <= abs(letters.index(x) - vowel_indexes[y+1]):
                next_vowel = letters[vowel_indexes[y]]
                break

        if x != "z":
            next_cons = cons[cons.index(x)+1]
        
        else:
            next_cons = "z"

        word[word.index(x)] = x + next_vowel + next_cons

print("".join(word))