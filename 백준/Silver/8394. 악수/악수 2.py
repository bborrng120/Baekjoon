import sys

d = [1,1]
n = int(sys.stdin.readline())
for i in range(2,n+1):
    temp = str(d[i-1]+d[i-2])
    temp = temp[-1]
    d.append(int(temp))
print(d[n])
