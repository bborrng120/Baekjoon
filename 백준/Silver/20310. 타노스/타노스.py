from collections import Counter
import sys

s = sys.stdin.readline().strip()
count = Counter(s)
o_list,z_list = [],[]
ans = ''

for i in range(len(s)):
    if s[i]=='0':
        z_list.append((i,'0'))
    else:
        o_list.append((i,'1'))
        
for _ in range(count['0']//2):
    z_list.pop()
    
for _ in range(count['1']//2):
    o_list.pop(0)
    
ans_list = sorted(z_list+o_list,key=lambda x:x[0])

for i in ans_list:
    ans+=i[1]
    
print(ans)