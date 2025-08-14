import math
import sys
 
n, m, k = map(int, sys.stdin.readline().split())
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
good = [0, 2, 4, 6]
bad = [1, 3, 5, 7]
ans = 0

fireball_dict = {}
for _ in range(m):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    fireball_dict[(r-1,c-1)] = [(m, s, d)]
 
for _ in range(k):
    new_fireball_dict = {}
    my_list = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]

    for fd in fireball_dict:
        x, y = fd[0], fd[1]
        for i in fireball_dict[fd]:
            m, s, d = i[0], i[1], i[2]
            nx = (x + dx[d]*s)%n
            ny = (y + dy[d]*s)%n
            
            if (nx, ny) in new_fireball_dict:
                my_list[nx][ny][0] += m
                my_list[nx][ny][1] += s
                my_list[nx][ny][3] += 1
                
                
                if my_list[nx][ny][2] != -1 and (d % 2) != (my_list[nx][ny][2] % 2):
                    my_list[nx][ny][2] = -1
                
            else:
                my_list[nx][ny] = [m, s, d, 1]
                new_fireball_dict[(nx, ny)] = [(m, s, d)]
    
    for i in range(n):
        for j in range(n):
            if my_list[i][j][3] > 1:
                new_fireball_dict[(i,j)] = []
                if my_list[i][j][0]//5 > 0:
                    nm = my_list[i][j][0]//5
                    ns = my_list[i][j][1]//my_list[i][j][3]
                    
                    if my_list[i][j][2] != -1:
                        tp = good
                    else:
                        tp = bad
                        
                    for k in tp:
                        new_fireball_dict[(i,j)].append((nm, ns, k))
                
    fireball_dict = new_fireball_dict
    
for fd in fireball_dict:
    x, y = fd[0], fd[1]
    for i in fireball_dict[fd]:
        ans += i[0]
        
print(ans)