import sys

n = int(sys.stdin.readline())
d = [0]*(n+1)
check = [0]*(n+1)
for i in range(2,n+1):
    d[i] = d[i-1]+1
    check[i] = i-1
    if i%3 == 0:
        if d[i//3]+1 < d[i]:
            d[i] = d[i//3]+1
            check[i] = i//3
    if i%2 == 0:
        if d[i//2]+1 < d[i]:
            d[i] = d[i//2]+1
            check[i] = i//2

num = n
my = [num]
while num > 1:
    num = check[num]
    my.append(num)
print(d[n])
print(*my)