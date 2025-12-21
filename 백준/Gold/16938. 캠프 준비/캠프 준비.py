import sys

n, l, r, x = map(int, sys.stdin.readline().split())
my_list = list(map(int, sys.stdin.readline().split()))
ans = 0

def back(arr, k):
    global ans
    
    if len(arr) <= n and len(arr) > 1:
        diff = max(arr) - min(arr)
        sums = sum(arr)
        if diff >= x and sums >= l and sums <= r:
            ans += 1
    
    for i in range(k, n):
        arr.append(my_list[i])
        back(arr, i+1)
        arr.pop(-1)
        
back([], 0)
print(ans)
