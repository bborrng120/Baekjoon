import sys

n = int(sys.stdin.readline())

def check_if_1(s, e):
    while s<e:
        if mystr[s]==mystr[e]:
            s+=1
            e-=1
        else:
            return False
    return True

def check(s, e):
    c = False
    while s<e:
        if mystr[s]==mystr[e]:
            s+=1
            e-=1
        else:
            if check_if_1(s+1, e) or check_if_1(s, e-1):
                return 1
            else:
                return 2
    return 0
    

for _ in range(n):
    mystr = sys.stdin.readline().rstrip()
    s, e = 0, len(mystr)-1
    ans = check(s, e)
    print(ans)