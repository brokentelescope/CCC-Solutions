hm_lines = int(input())
time = 1

received = {}
sent = {}
hm_msgs = {}

for x in range(hm_lines):
    msg = input().split(" ")
    action = msg[0]
    num = int(msg[1])
    
    if action == "W":
        time += num - 1
    
    if action == "R":
        if str(num) not in received:
            received[str(num)] = time
        
        else:
            received[str(num)] += time

        if str(num) not in hm_msgs:
            hm_msgs[str(num)] = 1
        
        else:
            hm_msgs[str(num)] += 1

        time += 1

    if action == "S":
        if str(num) not in sent:
            sent[str(num)] = time
        
        else:
            sent[str(num)] += time
        
        if str(num) not in hm_msgs:
            hm_msgs[str(num)] = 1
        
        else:
            hm_msgs[str(num)] += 1
        
        time += 1

for key in sorted(received):
    if hm_msgs[key] % 2 == 0:
        wait_time = sent[key] - received[key]

    else:
        wait_time = -1

    print(key + " "+ str(wait_time))
