from collections import deque

my_list = deque()
n = int(input())

for i in range(1, n+1):
    my_list.append(i)
    
while len(my_list) != 1:
    my_list.popleft()
    my_list.append(my_list.popleft())

for i in my_list:
    print(i)