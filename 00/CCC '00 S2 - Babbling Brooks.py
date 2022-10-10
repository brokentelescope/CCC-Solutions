#https://dmoj.ca/problem/ccc00s2
initial = int(input())

streams = []

for x in range(initial):
    streams.append(float(input()))


while True:
    stream = int(input())

    #SPLIT
    if stream == 99:
        stream_num = int(input())-1
        percent = float(input())

        left = streams[stream_num] * percent/100.0
        right = streams[stream_num] - left

        streams[stream_num] = left
        streams.insert(stream_num+1, right)

    #JOIN
    elif stream == 88:
        stream_num = int(input())-1
        streams[stream_num] += streams[stream_num+1]
        streams.pop(stream_num+1)
    
    #END
    else:
        break

print(" ".join([str(round(x)) for x in streams]))
