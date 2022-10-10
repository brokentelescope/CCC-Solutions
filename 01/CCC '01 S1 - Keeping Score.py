from stringprep import c22_specials


line = input()

clubs = []
diamonds = []
hearts = []
spades = []

suit = ""

print("Cards Dealt              Points")

for x in line:
    if x == "C":
        suit = "clubs"
    elif x == "D":
        suit = "diamonds"
    elif x == "H":
        suit = "hearts"
    elif x == "S":
        suit = "spades"
    else:
        if suit == "clubs":
            clubs.append(x)
        elif suit == "diamonds":
            diamonds.append(x)
        elif suit == "hearts":
            hearts.append(x)
        else:
            spades.append(x)

c_score, d_score, h_score, s_score = 0, 0, 0, 0

if len(clubs) == 0:
    c_score = 3
elif len(clubs) == 1:
    c_score = 2
elif len(clubs) == 2:
    c_score = 1

for x in clubs:
    if x == "A":
        c_score += 4
    elif x == "K":
        c_score += 3
    elif x == "Q":
        c_score += 2
    elif x == "J":
        c_score += 1

if len(diamonds) == 0:
    d_score = 3
elif len(diamonds) == 1:
    d_score = 2
elif len(diamonds) == 2:
    d_score = 1

for x in diamonds:
    if x == "A":
        d_score += 4
    elif x == "K":
        d_score += 3
    elif x == "Q":
        d_score += 2
    elif x == "J":
        d_score += 1

if len(hearts) == 0:
    h_score = 3
elif len(hearts) == 1:
    h_score = 2
elif len(hearts) == 2:
    h_score = 1

for x in hearts:
    if x == "A":
        h_score += 4
    elif x == "K":
        h_score += 3
    elif x == "Q":
        h_score += 2
    elif x == "J":
        h_score += 1

if len(spades) == 0:
    s_score = 3
elif len(spades) == 1:
    s_score = 2
elif len(spades) == 2:
    s_score = 1

for x in spades:
    if x == "A":
        s_score += 4
    elif x == "K":
        s_score += 3
    elif x == "Q":
        s_score += 2
    elif x == "J":
        s_score += 1

print("Clubs ", end="")
print(" ".join(clubs), end="")
print(" " * 10 + str(c_score))

print("Diamonds ", end="")
print(" ".join(diamonds), end="")
print(" " * 10 + str(d_score))

print("Hearts ", end="")
print(" ".join(hearts), end="")
print(" " * 10 + str(h_score))

print("Spades ", end="")
print(" ".join(spades), end="")
print(" " * 10 + str(s_score))

print("                       Total " + str(c_score+d_score+h_score+s_score))

