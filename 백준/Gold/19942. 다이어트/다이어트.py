import sys

n = int(sys.stdin.readline())
nut = list(map(int, sys.stdin.readline().split()))
my_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = int(1e9)
ans_list = []

def back(k, arr):
    global ans, ans_list
    
    if arr and len(arr) <= n:
        sums = [0, 0, 0, 0]
        price = 0
        for i in arr:
            for j in range(4):
                sums[j] += my_list[i][j]
            price += my_list[i][4]
            
        for i in range(4):
            if sums[i] < nut[i]:
                price = int(1e10)
        #print(arr,price)
        temp_arr = [x+1 for x in arr]
            
        if ans > price:
            ans_list = []
            ans_list.append(temp_arr)
            ans = price
        elif ans == price:
            ans_list.append(temp_arr)
        
    for i in range(k, n):
        arr.append(i)
        back(i+1, arr)
        arr.pop()
        
back(0, [])
if ans_list:
    ans_list.sort()
    print(ans)
    print(*ans_list[0])
else:
    print(-1)
                