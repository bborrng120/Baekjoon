import sys

n, m = map(int, sys.stdin.readline().split())
my_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
kx = [-1, -1, 1, 1]
ky = [-1, 1, -1, 1]
rain = [(n-2, 0), (n-2, 1), (n-1, 0), (n-1, 1)]

def move_cloud(rain, d, s):
    new_rain = set()
    for x, y in rain:
        nx, ny = (x + dx[d-1]*s) % n, (y + dy[d-1]*s) % n
        my_list[nx][ny] += 1
        new_rain.add((nx, ny))
        
    return new_rain
    
def water_copy(rain):
    for i in rain:
        count = 0
        for j in range(4):
            nx = i[0] + kx[j]
            ny = i[1] + ky[j]
            
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if my_list[nx][ny] > 0:
                count += 1
                
        my_list[i[0]][i[1]] += count
        
def find_water(rain):
    new_rain = []
    for i in range(n):
        for j in range(n):
            if (i, j) in rain or my_list[i][j] < 2:
                continue
            my_list[i][j] -= 2
            new_rain.append((i, j))
                    
    return new_rain
    
def get_ans():
    ans = 0
    for i in range(n):
        ans += sum(my_list[i])
        
    return ans

for _ in range(m):
    d, s = map(int, sys.stdin.readline().split())
    new_rain = move_cloud(rain, d, s)
    water_copy(new_rain)
    rain = find_water(new_rain)
    
print(get_ans())
