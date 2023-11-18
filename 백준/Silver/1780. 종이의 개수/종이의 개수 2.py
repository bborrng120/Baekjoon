import sys

n = int(sys.stdin.readline())
paper = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
a, b, c = 0, 0, 0
 
def back(x,y,k):
    global a,b,c
    a_check, b_check, c_check = True, True, True
 
    for i in range(x,x+k):
        for j in range(y,y+k):
            if paper[i][j]==-1:
                b_check, c_check = False, False
            elif paper[i][j]==0:
                a_check, c_check = False, False
            else:
                a_check, b_check = False, False
 
    if a_check:
        a+=1
        return
    if b_check:
        b+=1
        return
    if c_check:
        c+=1
        return
 
    back(x,y,k//3)
    back(x,y+(k//3),k//3)
    back(x,y+(k//3)*2,k//3)
    back(x+(k//3),y,k//3)
    back(x+(k//3),y+(k//3),k//3)
    back(x+(k//3),y+(k//3)*2,k//3)
    back(x+(k//3)*2,y,k//3)
    back(x+(k//3)*2,y+(k//3),k//3)
    back(x+(k//3)*2,y+(k//3)*2,k//3)
 
back(0,0,n)
print(a)
print(b)
print(c)
