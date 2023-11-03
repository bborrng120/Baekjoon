import sys

n = int(sys.stdin.readline())
d = [0,1,1,2,2,1,2,1]

for i in range(8, n + 1):
    ans = min(d[i - 1] + 1, d[i - 2] + 1, d[i - 5] + 1, d[i - 7] + 1)
    d.append(ans)
print(d[n])