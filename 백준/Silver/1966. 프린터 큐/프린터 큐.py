n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    my_list = list(map(int,input().split()))
    queue = []
    count = 0
    
    for i in range(len(my_list)):
        if i == b:
            queue.append((my_list[i], 'a'))
        else:
            queue.append((my_list[i], 'b'))
            
    while len(queue) != 0:
        if queue[0][0] != max(my_list):
            queue.append(queue[0])
            queue.pop(0)
        else:
            count += 1
            if queue[0][1] == 'a':
                break
            my_list.pop(my_list.index(queue[0][0]))
            queue.pop(0)
    print(count)