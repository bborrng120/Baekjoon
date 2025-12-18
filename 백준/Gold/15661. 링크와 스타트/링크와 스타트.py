import sys

n = int(sys.stdin.readline())
my_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = int(1e9)

def add(l):
    temp_sum = 0
    for i in range(0, len(l)-1):
        for j in range(i+1, len(l)):
            temp_sum += my_list[l[i]][l[j]]
            temp_sum += my_list[l[j]][l[i]]
            
    return temp_sum

def back(arr, k):
    global ans
    
    if len(arr) <= n//2:
        brr = list(set(range(n)) - set(arr))
        a = add(arr)
        b = add(brr)
        
        ans = min(ans, abs(a-b))
    else:
        return
    
    for i in range(k, n):
        arr.append(i)
        back(arr, i+1)
        arr.pop(-1)
                
back([], 0)

print(ans)