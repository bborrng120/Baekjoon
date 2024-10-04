import sys

bingo = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
end = False

def find(my_list, value):
    for i in range(5):
        for j in range(5):
            if my_list[i][j] == value:
                my_list[i][j] = 0

def check(my_list):
    count = 0
    for i in range(5):
        if sum(my_list[i])==0:
            count += 1
            
    for i in range(5):
        v_sums = 0
        for j in range(5):
            v_sums += my_list[j][i]
        if v_sums == 0:
            count += 1
            
    if my_list[0][0] + my_list[1][1] + my_list[2][2] + my_list[3][3] + my_list[4][4] == 0:
        count += 1
        
    if my_list[0][4] + my_list[1][3] + my_list[2][2] + my_list[3][1] + my_list[4][0] == 0:
        count += 1
        
    return count

for i in range(5):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(5):
        find(bingo, temp[j])
        c = check(bingo)
        if c >= 3:
            print((i*5)+j+1)
            end = True
            break
    if end:
        break
