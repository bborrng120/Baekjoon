from collections import deque

n = int(input())

for _ in range(n):
    a = input()
    my_list = deque()
    for i in a:
        if i == '(':
            my_list.append(i)
        else:
            if len(my_list) == 0:
                my_list.append(i)
                break
            else:
                my_list.popleft()
    if len(my_list) != 0:
        print("NO")
    else:
        print("YES")