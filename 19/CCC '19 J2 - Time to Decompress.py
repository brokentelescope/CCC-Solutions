howManyLines = int(input())
for x in range(howManyLines):
    message = input().split(" ")
    print(message[-1] * int(message[0]))
