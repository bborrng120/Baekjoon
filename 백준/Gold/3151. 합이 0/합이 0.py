import sys
from collections import Counter

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
my_list.sort()
counter = Counter(my_list)
count = 0

for i in range(n-2):
    l,r = i+1, n-1
        
    while l<r:
        sums = my_list[l]+my_list[r]+my_list[i]
        
        if sums>0:
            r-=1
        else:
            if sums==0:
                if my_list[l]==my_list[r]:
                    count += r-l
                else:
                    s = counter[my_list[r]]
                    count += s
            l+=1
            
print(count)