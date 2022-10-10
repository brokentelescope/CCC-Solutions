x = 0
translation =[]
while x == 0:
    word = input()
    wordlist = list(word)
    if word == ("quit!"):
        break
    else:
        if len(wordlist) > 3:
            if wordlist[-3] != "a" and wordlist[-3] != "e" and wordlist[-3] != "i" and wordlist[-3] != "o" and wordlist[-3] != "u" and wordlist[-3] != "y" and wordlist[-1] == ("r") and wordlist[-2] == ("o"):
                wordlist.pop(-1)
                wordlist.pop(-1)
                translation.append("".join(wordlist)+ "our")
            else:
                translation.append(word)
for i in (translation):
    print(i)