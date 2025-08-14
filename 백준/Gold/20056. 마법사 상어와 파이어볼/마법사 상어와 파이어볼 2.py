import math
import sys
 
n, m, k = map(int, sys.stdin.readline().split())
my_list = [[[] for _ in range(n)] for _ in range(n)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

fireball = []
for _ in range(m):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    fireball.append((r-1, c-1, m, s, d))
 
for _ in range(k):
    while fireball:
        x, y, m, s, d = fireball.pop()
        nx = (x + dx[d]*s)%n
        ny = (y + dy[d]*s)%n
        
        my_list[nx][ny].append([m, s, d])
    
    for i in range(n):
        for j in range(n):
            if len(my_list[i][j]) > 1:
                sm, ss, pd, cnt, check = 0, 0, my_list[i][j][-1][2], len(my_list[i][j]), True
                while my_list[i][j]:
                    m, s, d = my_list[i][j].pop()
                    sm += m
                    ss += s
                    
                    if (check) and (d%2 == pd%2):
                        check = True
                    else:
                        check = False
                        
                    pd = d
                    
                if check:
                    fire_dir = [0, 2, 4, 6]
                else:
                    fire_dir = [1, 3, 5, 7]
                    
                if sm//5 > 0:
                    for k in fire_dir:
                        fireball.append([i, j, sm//5, ss//cnt, k])
                        
            elif len(my_list[i][j]) == 1:
                fireball.append([i, j] + my_list[i][j].pop())
                        

print(sum(i[2] for i in fireball))
