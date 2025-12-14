import sys

n = int(sys.stdin.readline())

def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
    
def back(num):
    if len(str(num)) == n:
        if is_prime(num):
            print(num)
        return
    
    if not is_prime(num):
        return
        
    for i in range(1, 10, 2):
        tmp = int(str(num) + str(i))
        back(tmp)

back(2)
back(3)
back(5)
back(7)