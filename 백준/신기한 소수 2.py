import sys

n = int(sys.stdin.readline())

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
    
def back(num):
    if len(str(num)) == n:
        print(num)
    
    else:
        for i in range(1, 10, 2):
            tmp = num*10 + i
            if is_prime(tmp):
                back(tmp)

back(2)
back(3)
back(5)
back(7)
