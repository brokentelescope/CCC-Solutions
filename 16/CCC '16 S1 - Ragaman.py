from string import ascii_lowercase


a = input()
b = input()

extra = b.count("*")

for x in ascii_lowercase:
    extra -= abs(a.count(x)- b.count(x))

if extra == 0:
    print("A")
else:
    print("N")