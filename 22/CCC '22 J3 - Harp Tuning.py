inst = input() + "x"
numbers = "0123456789"
strings = ""
turns = ""
t_or_l = True
# output = False

for x in inst:
    if x != "+" and x != "-" and x not in numbers:

        if turns != "":
            if t_or_l:
                print(strings + " tighten " + turns)
                output = False
            
            else:
                print(strings + " loosen " + turns)
                output = False
            
            turns = ""
            strings = ""
        
        strings += x

    elif x in numbers:
        turns += x

    elif x == "+":
        t_or_l = True
        # output = True
    
    else:
        t_or_l = False
        # output = True
#AFB+8HC-4
    