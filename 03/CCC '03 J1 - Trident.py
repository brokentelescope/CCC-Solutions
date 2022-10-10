t = int(input())
s = int(input())
h = int(input())

#top prongs 

for x in range(t):
    print((" "*s).join(["*"]*3))

print("*"*(3+2*s))

for x in range(h):
    print(" "*(s+1) + "*")  