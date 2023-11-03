import sys

n = int(sys.stdin.readline())
my_list = [0]
my_list.extend(list(map(int,sys.stdin.readline().split())))
d = [0]*(n+1)
d[1] = my_list[1]

for i in range(2,n+1):
    for k in range(1,i+1):
        if k <= i-k or k == i:
            d[i] = max(d[i],my_list[k] + d[i-k])
            
print(d[-1])