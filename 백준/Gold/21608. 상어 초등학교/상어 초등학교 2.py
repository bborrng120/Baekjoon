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
    student = list(map(int, sys.stdin.readline().split()))
    student_dict[student[0]] = student[1:]
    available = []
            
    for i, j in empty_set:
        prefer, empty = 0, 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            
            if 0<=nx<n and 0<=ny<n:
                if my_list[nx][ny] in student_dict[student[0]]:
                    prefer += 1
                if my_list[nx][ny] == 0:
                    empty += 1
                    
        available.append((i, j, prefer, empty))
                
    available.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
    my_list[available[0][0]][available[0][1]] = student[0]
    empty_set.discard((available[0][0], available[0][1]))
        
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
