import sys

plist = [True]*(1000001)
for i in range(3,int(1000000**0.5)+1,2):
    if plist[i]:
        for j in range(i+i,1000001,i):
            plist[j] = False

while True:
    n = int(sys.stdin.readline())
    if n==0:
        break
    
    a,b = 0,0
    for i in range(3,n+1,2):
        if plist[i] and plist[n-i]:
            a,b = i, n-i
            break
                
    if a==0 and b==0:
        print("Goldbach's conjecture is wrong.")
    else:
        print(f'{n} = {a} + {b}')