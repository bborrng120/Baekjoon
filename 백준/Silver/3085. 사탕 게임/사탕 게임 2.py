import sys

n = int(sys.stdin.readline())

my_list = [list(sys.stdin.readline().strip()) for _ in range(n)]
ans = 1

def check(temp):
    ans = 1
    
    for i in range(n):
        res = 1
        for j in range(n-1):
            if temp[i][j] == temp[i][j+1]:
                res += 1
            else:
                res = 1
            ans = max(ans, res)
        
    res = 1
    for i in range(n):
        res = 1
        for j in range(n-1):
            if temp[j][i] == temp[j+1][i]:
                res += 1
            else:
                res = 1
            ans = max(ans, res)
        
    return ans
    
for i in range(n):
    for j in range(n-1):
        if my_list[i][j] != my_list[i][j+1]:
            my_list[i][j], my_list[i][j+1] = my_list[i][j+1], my_list[i][j]
            ans = max(ans, check(my_list))
            my_list[i][j], my_list[i][j+1] = my_list[i][j+1], my_list[i][j]
            
        if my_list[j][i] != my_list[j+1][i]:
            my_list[j][i], my_list[j+1][i] = my_list[j+1][i], my_list[j][i]
            ans = max(ans, check(my_list))
            my_list[j][i], my_list[j+1][i] = my_list[j+1][i], my_list[j][i]
        
print(ans)
