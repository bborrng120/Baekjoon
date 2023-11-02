import sys

while True:
    a, b, c = map(int,sys.stdin.readline().split())
    if a==0 and b ==0 and c == 0:
        break
    if a**2+b**2==c**2:
        print('right')
        continue
    if b**2+c**2==a**2:
        print('right')
        continue
    if a**2+c**2==b**2:
        print('right')
        continue
    print('wrong')