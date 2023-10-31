import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    my_list = list(map(int,sys.stdin.readline().split()))
    d = [0]*n
    d[0] = my_list[0]
    
    for i in range(1,n):
        d[i] = max(d[i-1]+my_list[i],my_list[i])
        
    print(max(d))