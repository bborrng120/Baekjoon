import copy
import sys
 
n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
cctv = []
way = [0, 4, 2, 4, 4, 1]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
mins = int(1e9)
 
for i in range(n):
    for j in range(m):
        if graph[i][j]!=0 and graph[i][j]!=6:
            cctv.append((graph[i][j], i, j))
 
def move(x,y,ttt,k):
    if k==0:
        nx = x+dx[k]
        ny = y+dy[k]
        while 0<=nx<n and 0<=ny<m:
        	if ttt[nx][ny] ==6:
        		break
        	elif ttt[nx][ny]==0:
        		ttt[nx][ny]=7
        	nx-=1
        	
    elif k==1:
    	nx = x+dx[k]
    	ny = y+dy[k]
    	while 0<=nx<n and 0<=ny<m:
    		if ttt[nx][ny] ==6:
    		    break
    		elif ttt[nx][ny]==0:
    			ttt[nx][ny]=7
    		nx+=1
    		
    elif k==2:
    	nx = x+dx[2]
    	ny = y+dy[2]
    	while 0<=nx<n and 0<=ny<m:
    		if ttt[nx][ny] ==6:
    		    break
    		elif ttt[nx][ny]==0:
    			ttt[nx][ny]=7
    		ny-=1
    		
    else:
    	nx = x+dx[3]
    	ny = y+dy[3]
    	while 0<=nx<n and 0<=ny<m:
    		if ttt[nx][ny] ==6:
    		    break
    		elif ttt[nx][ny]==0:
    			ttt[nx][ny]=7
    		ny+=1
            
 
def fill(cnum,num,x,y,tt):
    if cnum==1:
        if num==1:
            move(x,y,tt,0)
        elif num==2:
            move(x,y,tt,1)
        elif num==3:
            move(x,y,tt,2)
        else:
            move(x,y,tt,3)
 
    elif cnum==2:
        if num==1:
            for i in range(2):
                if i==0:
                    move(x,y,tt,2)
                else:
                    move(x,y,tt,3)
        else:
            for i in range(2):
                if i==0:
                    move(x,y,tt,0)
                else:
                    move(x,y,tt,1)
 
    elif cnum==3:
        if num==1:
            for i in range(2):
                if i==0:
                    move(x,y,tt,0)
                else:
                    move(x,y,tt,2)
        elif num==2:
            for i in range(2):
                if i==0:
                    move(x,y,tt,0)
                else:
                    move(x,y,tt,3)
        elif num==3:
            for i in range(2):
                if i==0:
                    move(x,y,tt,1)
                else:
                    move(x,y,tt,2)
        else:
            for i in range(2):
                if i==0:
                    move(x,y,tt,1)
                else:
                    move(x,y,tt,3)
 
    elif cnum==4:
        if num==1:
            for i in range(3):
                if i==0:
                    move(x,y,tt,0)
                elif i==1:
                    move(x,y,tt,2)
                else:
                    move(x,y,tt,3)
        elif num==2:
            for i in range(3):
                if i==0:
                    move(x,y,tt,0)
                elif i==1:
                    move(x,y,tt,1)
                else:
                    move(x,y,tt,2)
        elif num==3:
            for i in range(3):
                if i==0:
                    move(x,y,tt,0)
                elif i==1:
                    move(x,y,tt,1)
                else:
                    move(x,y,tt,3)
        else:
            for i in range(3):
                if i==0:
                    move(x,y,tt,1)
                elif i==1:
                    move(x,y,tt,2)
                else:
                    move(x,y,tt,3)
 
    else:
        for i in range(4):
            if i==0:
                move(x,y,tt,0)
            elif i==1:
                move(x,y,tt,1)
            elif i==2:
                move(x,y,tt,2)
            else:
                move(x,y,tt,3)
 
def check(tttt):
    r = 0
    for i in range(n):
        for j in range(m):
            if tttt[i][j]==0:
                r += 1
    return r
 
def dfs(depth,t):
	global mins
 
	if depth==len(cctv):
		res = check(t)
		mins = min(mins,res)
	else:
		temp = copy.deepcopy(t)
		x, y, z = cctv[depth][1], cctv[depth][2], cctv[depth][0]
		for i in range(1,way[z]+1):
			fill(z,i,x,y,temp)
			dfs(depth+1,temp)
			temp = copy.deepcopy(t)
 
dfs(0,graph)
print(mins)