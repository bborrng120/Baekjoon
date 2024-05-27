import sys

n = int(sys.stdin.readline())
d = [0]*(101)
d[1], d[2], d[3], d[4], d[5], d[6] = 1, 2, 3, 4, 5, 6

for i in range(7,101):
    for j in range(3,i):
        d[i] = max(d[i],d[i-j]*(j-1))
        
print(d[n])