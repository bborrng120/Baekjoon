import sys

t = int(sys.stdin.readline())
count = 1

for _ in range(t):
    ans = 0
    n = int(sys.stdin.readline())
    l1 = list(map(int,sys.stdin.readline().split()))
    l2 = list(map(int,sys.stdin.readline().split()))
    l1.sort()
    l2.sort(reverse=True)
    
    for i in range(n):
        ans += l1[i]*l2[i]
        
    print(f"Case #{count}: {ans}")
    count += 1