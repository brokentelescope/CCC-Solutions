w = int(input())

words = ["WELCOME", "TO", "CCC", "GOOD", "LUCK", "TODAY", "DEEZNUTSDEEZNUTSDEEZNUTSDEEZNUTSDEEZNUTSDEEZNUTSDEEZNUTSDEEZNUTSDEEZNUTSDEEZNUTSDEEZNUTSDEEZNUTSDEEZNUTSDEEZNUTSDEEZNUTS"]

def dots(extra, words):
    distribution = [0] * (words-1)
    
    if words == 1:
        return [extra]
        
    while extra != 0:
        for x in range(words-1):
            if extra != 0:
                distribution[x] = distribution[x] + 1
                extra -= 1 
            else:
                break
    
    distribution.append(0)
    return distribution

while len(words) != 1:
    #LINE
    letters = 0 
    hm_words = 0
    extra = 0
    while True:
        if letters + len(words[hm_words]) + (hm_words-1) >= w:
            extra = w - letters
            dot = dots(extra, hm_words)
            
            for x in range(hm_words):
                print(words[x] + "." * dot[x], end="")
            
            print()
            for x in range(hm_words):
                words.pop(0)
            break
        else:
            letters += len(words[hm_words])
            hm_words += 1