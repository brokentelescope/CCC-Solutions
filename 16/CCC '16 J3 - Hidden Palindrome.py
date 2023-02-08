string = input()

counter = 0

for x in range(len(string)):
    for y in range(len(string)+1):
        if string[0:y] == string[0:y][::-1]:
            if y > counter:
                counter = y
        
    string = string[1:]

print(counter)
        

