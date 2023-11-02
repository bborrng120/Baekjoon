import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
my_list.sort()
s, e, sums, count = 0, n-1, 0, 0
 
while s < e:
    sums = my_list[s]+my_list[e]
    if sums >= m:
        e-=1
    else:
        s+=1
    if sums == m:
        count+=1
 
print(count)