import sys

n = int(sys.stdin.readline())
my_list = [0]
my_list.extend(list(map(int,sys.stdin.readline().split())))
d = [int(1e9)]*(n+1)
d[0] = 0
d[1] = my_list[1]

for i in range(2,n+1):
    for j in range(1,i+1):
        d[i] = min(d[i],my_list[j]+d[i-j])

print(d[-1])