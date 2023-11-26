import sys

n = int(sys.stdin.readline())
cookie = [sys.stdin.readline().strip() for _ in range(n)]
head = True
body=[0,0,0,0,0]

for i in range(n):
    for j in range(n):
        if cookie[i][j]=='*':
            if head:
                xhead,yhead = i,j
                head = False
                
            else:
                if xhead+1==i:
                    if yhead>j:
                        body[0]+=1
                    elif yhead==j:
                        xheart,yheart = i+1,j+1
                    else:
                        body[1]+=1
                        
                elif yheart-1==j:
                    body[2]+=1
                    
                else:
                    if yheart-2==j:
                        body[3]+=1
                    elif yheart==j:
                        body[4]+=1
                        
print(xheart,yheart)
print(*body)