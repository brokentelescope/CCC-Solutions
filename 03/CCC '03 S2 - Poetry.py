def last_syl(word):
    vowels = "aeiouAEIOU"
    
    letters = 0
    for x in range(len(word)):
        if word[-(x+1)] in vowels:
            break
        else:
            letters += 1 
    
    return word[-letters-1:].lower()

for x in range(int(input())):
    first = input().split(" ")
    second = input().split(" ")
    third = input().split(" ")
    fourth = input().split(" ")
    
    if last_syl(first[-1]) == last_syl(second[-1]) and last_syl(second[-1]) == last_syl(third[-1]) and last_syl(third[-1]) == last_syl(fourth[-1]):
        print("perfect")
    else:
        if last_syl(first[-1]) == last_syl(second[-1]) and last_syl(third[-1]) == last_syl(fourth[-1]):
            print("even")
        elif last_syl(first[-1]) == last_syl(third[-1]) and last_syl(second[-1]) == last_syl(fourth[-1]):
            print("cross")
        elif last_syl(first[-1]) == last_syl(fourth[-1]) and last_syl(second[-1]) == last_syl(third[-1]):
            print("shell")
        else:
            print("free")