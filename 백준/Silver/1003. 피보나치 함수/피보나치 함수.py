n = int(input())

for _ in range(n):
    s = int(input())
    d=[(1,0),(0,1)]
    for i in range(s-1):
        d.extend([(0,0)])
    for j in range(2,s+1):
        d[j] = (d[j-1][0] + d[j-2][0], d[j-1][1] + d[j-2][1])
    print(d[s][0], d[s][1])