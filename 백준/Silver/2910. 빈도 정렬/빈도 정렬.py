import sys

n, c = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))

dic = {}
idx = 0
for i in my_list:
    if i in dic:
        dic[i][0]+=1
    else:
        dic[i] = [1,idx]
        idx += 1
        
ans = [[i,j] for i,j in dic.items()]
ans.sort(key=lambda x:(-x[1][0],x[1][1]))
for i,j in ans:
    for _ in range(j[0]):
        print(i,end=" ")