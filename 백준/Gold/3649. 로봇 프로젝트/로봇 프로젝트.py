import sys

while True:
    try:
        n = int(sys.stdin.readline())
        n *= int(1e7)
        m = int(sys.stdin.readline())
        my_list = []
        for _ in range(m):
            my_list.append(int(sys.stdin.readline()))
    
        my_list.sort()
        left, right = 0, m-1
        check = False

        while left < right:
            sums = my_list[left] + my_list[right]
    
            if sums == n:
                check = True
                a = my_list[left]
                b = my_list[right]
                break
        
            elif sums < n:
                left += 1
        
            else:
                right -= 1
        
        if check:
            print('yes',a,b)
        else:
            print('danger')
            
    except:
        break