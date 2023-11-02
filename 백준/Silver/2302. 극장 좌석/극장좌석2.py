import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
a = []
b = [x for x in range(1,n+1)]
d = [1]*(n+1)
for _ in range(m):
    a.append(int(input()))
    
res = [x for x in b if x not in a]
ans = []
count = 1

for i in range(len(res)-1):
    if res[i+1]-res[i]==1:
        count+=1
    else:
        ans.append(count)
        count = 1
ans.append(count)
        
for i in range(2,n+1):
    d[i] = d[i-2]+d[i-1]
    
s = 1
for i in ans:
    s *= d[i]
print(s)
