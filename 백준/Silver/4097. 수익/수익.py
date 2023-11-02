import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    my_list = []
    for _ in range(n):
        my_list.append(int(sys.stdin.readline()))
    d = [0]*n
    d[0] = my_list[0]
    
    for i in range(1,n):
        d[i] = max(my_list[i],d[i-1]+my_list[i])
    print(max(d))