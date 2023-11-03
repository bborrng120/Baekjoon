import sys

d = [0,1]
n = int(sys.stdin.readline())

for i in range(2,n+1):
    j = 1
    min = d[i-1]+1
    while j**2 <= i:
        if d[i-(j**2)]+1 < min:
            min = d[i-(j**2)]+1
        j += 1
    d.append(min)
print(d[n])