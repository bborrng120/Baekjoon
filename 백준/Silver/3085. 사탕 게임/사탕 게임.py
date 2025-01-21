import sys

n = int(sys.stdin.readline())

my_list = [list(sys.stdin.readline().strip()) for _ in range(n)]
rr_ans, cc_ans = 1, 1

def check(temp):
    r_ans, c_ans = 1, 1
    
    for i in range(n):
        r_res = 1
        for j in range(n-1):
            if temp[i][j] == temp[i][j+1]:
                r_res += 1
            else:
                r_res = 1
            r_ans = max(r_ans, r_res)
        
    for i in range(n):
        c_res = 1
        for j in range(n-1):
            if temp[j][i] == temp[j+1][i]:
                c_res += 1
            else:
                c_res = 1
            c_ans = max(c_ans, c_res)
        
    return max(c_ans, r_ans)
    
for i in range(n):
    for j in range(n-1):
        my_list[i][j], my_list[i][j+1] = my_list[i][j+1], my_list[i][j]
        rr_res = check(my_list)
        rr_ans = max(rr_ans, rr_res)
        my_list[i][j], my_list[i][j+1] = my_list[i][j+1], my_list[i][j]
        
        
for i in range(n):
    for j in range(n-1):        
        my_list[j][i], my_list[j+1][i] = my_list[j+1][i], my_list[j][i]
        cc_res = check(my_list)
        cc_ans = max(cc_ans, cc_res)
        my_list[j][i], my_list[j+1][i] = my_list[j+1][i], my_list[j][i]
        
print(max(rr_ans, cc_ans))