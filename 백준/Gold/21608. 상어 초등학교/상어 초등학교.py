import sys

n = int(sys.stdin.readline())
my_list = [[0]*n for _ in range(n)]
student_dict = {}
empty_set = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
scores = {0: 0, 1: 1, 2: 10, 3: 100, 4:1000}
ans = 0

for i in range(n):
    for j in range(n):
        empty_set.add((i, j))

for c in range(n**2):
    t = list(map(int, sys.stdin.readline().split()))
    student_dict[t[0]] = t[1:]
    max_count, max_next_count = 0, 0
    max_list, max_next_list = [], []
            
    for i, j in empty_set:
        count = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            
            if 0<=nx<n and 0<=ny<n:
                if my_list[nx][ny] in student_dict[t[0]]:
                    count += 1
                    
        if count > max_count:
            max_list = []
            max_list.append((i, j))
            max_count = count
        elif count == max_count:
            max_list.append((i, j))
            
    if len(max_list) > 1:
        for i, j in max_list:
            next_count = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                
                if 0<=nx<n and 0<=ny<n:
                    if my_list[nx][ny] == 0:
                        next_count += 1
                    
            if next_count > max_next_count:
                max_next_list = []
                max_next_list.append((i, j))
                max_next_count = next_count
            elif next_count == max_next_count:
                max_next_list.append((i, j))
                
        max_next_list.sort(key=lambda x: (x[0], x[1]))
        my_list[max_next_list[0][0]][max_next_list[0][1]] = t[0]
        empty_set.discard((max_next_list[0][0], max_next_list[0][1]))
            
    else:
        my_list[max_list[0][0]][max_list[0][1]] = t[0]
        empty_set.discard((max_list[0][0], max_list[0][1]))
        
for i in range(n):
    for j in range(n):
        temp_count = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            
            if 0<=nx<n and 0<=ny<n:
                if my_list[nx][ny] in student_dict[my_list[i][j]]:
                    temp_count += 1
                    
        ans += scores[temp_count]
        
print(ans)
