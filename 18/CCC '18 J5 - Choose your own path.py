books = {}
hm_pages = int(input())
visitable = [1]

for x in range(1,hm_pages+1):

    options = input()

    if options == "0":
        books[x] = -1

    else:
        page = [int(z) for z in options.split(" ")]
        books[x] = page[1:]
        
        for y in page[1:]:
            if y != x:
                visitable.append(y)

def shortest(books):
    counter = 1
    queue = [1]
    # visited = [1]

    while len(queue) > 0:

        for x in range(len(queue)):
            node = queue[0]
            # visited.append(node)

            for y in books[node]:
                if books[y] == -1:
                    return counter+1
                
                else:
                    # if y not in visited:
                    queue.append(y)            
            
            queue.pop(0)
        counter += 1

if len(set(visitable)) == hm_pages:
    print("Y")
else:   
    print("N")

print(shortest(books))