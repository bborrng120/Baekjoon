import sys

n = int(sys.stdin.readline())
paper = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
a, b, c = 0, 0, 0
 
def back(x,y,k):
    global a,b,c
    s = paper[x][y]
 
    for i in range(x,x+k):
        for j in range(y,y+k):
            if paper[i][j]!=s:
                back(x,y,k//3)
                back(x,y+(k//3),k//3)
                back(x,y+(k//3)*2,k//3)
                back(x+(k//3),y,k//3)
                back(x+(k//3),y+(k//3),k//3)
                back(x+(k//3),y+(k//3)*2,k//3)
                back(x+(k//3)*2,y,k//3)
                back(x+(k//3)*2,y+(k//3),k//3)
                back(x+(k//3)*2,y+(k//3)*2,k//3)
                return
 
    if s==-1:
        a+=1
        return
    elif s==0:
        b+=1
        return
    else:
        c+=1
        return
 
    
 
back(0,0,n)
print(a)
print(b)
print(c)