from itertools import combinations
import sys
        
n = int(sys.stdin.readline())
res = 0
min_ans, max_ans = int(1e10), 0
            
def back(num, cnt):
    global min_ans, max_ans
    
    for i in str(num):
        if int(i) % 2 != 0:
            cnt += 1
    
    if len(str(num)) == 1:
        min_ans = min(min_ans, cnt)
        max_ans = max(max_ans, cnt)
        return
    elif len(str(num)) == 2:
        tmp = int(str(num)[0]) + int(str(num)[1])
        back(tmp, cnt)
    else:
        k = [i for i in range(1, len(str(num)))]
        
        for i in combinations(k, 2):
            tmp = int(str(num)[:i[0]]) + int(str(num)[i[0]:i[1]]) + int(str(num)[i[1]:])
            back(tmp, cnt)
            
back(n, 0)
print(min_ans, max_ans)