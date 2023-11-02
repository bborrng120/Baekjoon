import sys

n = int(sys.stdin.readline())
d = [1]*(n+1)
count = 0

for i in range(1,len(d)):
    d[i] = d[i-1]*i
    
s = str(d[-1])
for i in reversed(s):
    if i == '0':
        count += 1
    else:
        break
print(count)