from itertools import product
from itertools import combinations
import copy
import sys
 
n = int(sys.stdin.readline())
school = [list(map(str,sys.stdin.readline().split())) for _ in range(n)]
c = [i for i in range(n)]
comb = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 'NO'

for i in list(product(c,repeat=2)):
	if school[i[0]][i[1]]=='X':
		comb.append((i[0],i[1]))
 
def check(temp):
    for x in range(n):
        for y in range(n):
            if temp[x][y]=='T':
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    
                    while 0<=nx<n and 0<=ny<n and temp[nx][ny]!='O':
                    	if temp[nx][ny]=='S':
                    		return False
                    	if i==0:
                    		nx-=1
                    	elif i==1:
                    		nx+=1
                    	elif i==2:
                    		ny-=1
                    	else:
                    		ny+=1
    return True
 
for i in combinations(comb,3):
    temp = copy.deepcopy(school)
 
    for x,y in i:
        temp[x][y]='O'
 
    c = check(temp)
    if c:
        ans = 'YES'
        break
 
print(ans)