import sys

num = int(sys.stdin.readline())
paper = [list(map(int,sys.stdin.readline().split())) for _ in range(num)]
b, w = 0, 0

def bin(x,y,n):
    global b, w
    white, blue = True, True
    
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j] == 0:
                blue = False
            if paper[i][j] == 1:
                white = False
                
    if blue:
        b += 1
        return
    if white:
        w += 1
        return
    
    bin(x,y,n//2)
    bin(x,y+(n//2),n//2)
    bin(x+(n//2),y,n//2)
    bin(x+(n//2),y+(n//2),n//2)
    
bin(0,0,num)
print(w)
print(b)