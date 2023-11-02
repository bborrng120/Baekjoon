import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
d = [0]*n

d[0] = my_list[0]
        
if n > 1:
    for i in range(1,len(d)):
        if d[i-1] < 0:
            d[i-1] = my_list[i-1]
        d[i] = max(d[i-1]+my_list[i], my_list[i])
print(max(d))