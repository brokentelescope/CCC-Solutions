# A monkey language word is a special type of word called an A-word, which may be optionally followed by the letter N and a monkey language word.
# An A-word is either only the single letter A, or the letter B followed by a monkey language word followed by the letter S.
#BBASNBASSNA
#BBANANASNBANANASS


def monkey(word):
    if word == "A":
        return "YES"
    
    if len(word) % 2 == 0:
        return "NO"

    else:
        
        if word[0] == "B":
            if word[-1] == "S":
                if monkey(word[1:-1]) == "NO":
                    #FIND ALL N'S
                    indices = []

                    for x in range(len(word)):
                        if word[x] == "N":
                            indices.append(x)
                    
                    for x in range(len(indices)):
                        if monkey(word[:indices[x]]) == "YES" and monkey(word[indices[x]+1:]) == "YES":
                            return "YES"
                    
                else:
                    
                    return "YES"

            else:
                indices = []
                for x in range(len(word)):
                        if word[x] == "N":
                            indices.append(x)
                    
                for x in range(len(indices)):
                    if monkey(word[:indices[x]]) == "YES" and monkey(word[indices[x]+1:]) == "YES":
                        return "YES"

                return "NO"

        if word[0] == "A":    
            if word[0:2] == "AN":
                return monkey(word[2:])
        
            else:
                return "NO"
        

while True:
    var = input()
    if var == "X":
        break

    else:
        print(monkey(var))                                                                          

