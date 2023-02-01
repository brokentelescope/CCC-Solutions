while True:
    digits = "1234567890"
    line = input()
    if line == "0":
        break 

    # read the line in reverse order

    line = line.split()[::-1]

    stack = []

    for x in line:
        # if the char is a digit, append it to the stack
        if x in digits:
            stack.append(x)
        # if the char is + or -, pop the two back elements from the stack
        else:
            a = stack.pop()
            b = stack.pop()
            # concatenate the a, b, and x and push it back into the stack
            stack.append(a + b + x)
    # the stack should have one element left which is the answer
    print(" ".join(list(stack[0])))
