import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    w = int(sys.stdin.readline())
    d = [0]*(w+1)
    d[0] = 1
    
    for i in coins:
        for j in range(i, w+1):
            d[j]+=d[j-i]
            
    print(d[w])