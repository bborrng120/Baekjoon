acm_str = int(input())

for _ in range(acm_str):
    h, w, n = map(int,input().split())
    if n <= h:
        rnum = n*100 + 1
    else:
        if n % h != 0:
            rnum = (n % h)*100 + (n // h + 1)        
        else:
            rnum = h*100 + n // h
            
    print(rnum)