import sys

def get_num(s):
    x = 8-int(s[1])
    y = ord(s[0])-65
    
    return x,y

def get_alpha(x,y):
    s = ''
    s += chr(65+y)
    s += str(8-x)
    
    return s

def move(s):
    if s=='R':
        return 0,1
    elif s=='L':
        return 0,-1
    elif s=='B':
        return 1,0
    elif s=='T':
        return -1,0
    elif s=='RT':
        return -1,1
    elif s=='LT':
        return -1,-1
    elif s=='RB':
        return 1,1
    else:
        return 1,-1

my_list = sys.stdin.readline().split()
k,r = my_list[0],my_list[1]
t = int(my_list[2])
x1,y1 = get_num(k)
x2,y2 = get_num(r)

for _ in range(t):
    nx,ny = move(input().strip())
    dx,dy = nx+x1,ny+y1
    if 0<=dx<8 and 0<=dy<8:
        if dx==x2 and dy==y2:
            if not (0<=x2+nx<8 and 0<=y2+ny<8):
                continue
            x2+=nx
            y2+=ny
        x1,y1 = dx,dy
        
print(get_alpha(x1,y1))
print(get_alpha(x2,y2))