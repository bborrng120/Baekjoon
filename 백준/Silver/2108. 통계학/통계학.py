import sys
from collections import Counter

n = int(input())
my_list, count_list = [], []
k, m, maxs = 0, 0, 0

def rounds(n):
    if abs(n) - int(abs(n)) > 0.5:
        if n < 0:
            return int(n)-1
        
        else:
            return int(n)+1
    else:
        return int(n)
    
for _ in range(n):
    my_list.append(int(sys.stdin.readline()))
    
my_list = sorted(my_list)
cnt = Counter(my_list)

for i in set(my_list):
    count_list.append(cnt[i])
    
maxs = max(count_list)

for i in sorted(set(my_list)):
    if cnt[i] > k:
        k = cnt[i]
        m = i
    elif cnt[i] == k and k == maxs:
        m = i
        break

print(rounds(sum(my_list)/len(my_list)))
print(my_list[len(my_list)//2])
print(m)
print(my_list[-1]-my_list[0])