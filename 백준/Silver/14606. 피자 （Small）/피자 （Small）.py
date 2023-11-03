import sys

n = int(sys.stdin.readline())
d = [0]*(n+1)
count = 1

for i in range(2,n+1):
    d[i] = d[i-1]+count
    count += 1
    
print(d[n])