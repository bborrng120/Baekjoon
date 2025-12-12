import sys

n, l = map(int, sys.stdin.readline().split())
my_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = 0

def rotated(arr):
    rot_list = zip(*arr[::-1])
    return [list(e) for e in rot_list]
    
def check(arr):
    used = [0 for _ in range(n)]
    
    for i in range(1, n):
        if abs(arr[i-1] - arr[i]) > 1:
            return False
        if arr[i] > arr[i-1]:
            for k in range(l):
                if (i-k-1) < 0 or used[i-k-1] or arr[i-k-1] != arr[i-1]:
                    return False
                elif arr[i-k-1] == arr[i-1]:
                    used[i-k-1] = 1
        elif arr[i] < arr[i-1]:
            for k in range(l):
                if (i+k) >= n or used[i+k] or arr[i+k] != arr[i]:
                    return False
                elif arr[i+k] == arr[i]:
                    used[i+k] = 1
        
    return True

for i in range(n):
    res = check(my_list[i])
    
    if res:
        ans += 1
        
my_list = rotated(my_list)
for i in range(n):
    res = check(my_list[i])
    
    if res:
        ans += 1

print(ans)