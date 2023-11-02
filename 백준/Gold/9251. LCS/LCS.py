import sys

n = sys.stdin.readline().strip()
m = sys.stdin.readline().strip()
d = [[0]*(len(n)+1) for _ in range(len(m)+1)]

for i in range(1,len(m)+1):
    for j in range(1, len(n)+1):
        if m[i-1]==n[j-1]:
            d[i][j] = d[i-1][j-1]+1
        else:
            d[i][j] = max(d[i-1][j],d[i][j-1])
            
print(d[len(m)][len(n)])