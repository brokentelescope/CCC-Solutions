# output = []
for x in range(int(input())):

    hm_steps = int(input())
    slow_steps = []

    for y in range(hm_steps):
        slow_steps.append(input())

    root = slow_steps[-1]
    
    stack = [root]
    counter = 0
    max = 0
    for x in slow_steps:
        if x in stack:
            stack.pop()
        else:
            stack.append(slow_steps[counter])

        if len(stack) > max:
            max = len(stack)

        counter += 1
        # print(stack)
    
    slow = hm_steps*10
    fast = 2*(max-1)*10
    print(
        slow - fast
        )
    
    # output.append(slow-fast)

# print(output)

