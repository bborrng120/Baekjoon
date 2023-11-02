num_str = int(input())

for i in range(num_str):
    ox_str = input()
    ox_list = ox_str.split("X")
    sum = 0
    for s in ox_list:
        if 'O' in s:
            count = len(s)
            while count != 0:
                sum+= count
                count-=1
    print(sum)