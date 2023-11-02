from collections import Counter
import sys

card = []
num = []
maxs = 0
color = True
cont = True
for _ in range(5):
    pair = sys.stdin.readline().split()
    card.append(pair)
    num.append(int(pair[1]))

for i in range(4):
    if card[i][0] != card[i+1][0]:
        color = False
        break

num.sort()
for i in range(4):
    if num[i+1]-num[i]!=1:
        cont = False
        break
        
count = Counter(num)
check = count.most_common()

if color or cont:
    if color and cont:
        maxs = max(maxs,num[-1]+900)
    if color:
        maxs = max(maxs,num[-1]+600)
    if cont:
        maxs = max(maxs,num[-1]+500)
    
if len(check)>1:
    if check[0][1]==4:
        maxs = max(maxs,check[0][0]+800)
    if check[0][1]==3:
        maxs = max(maxs,check[0][0]+400)
        if check[1][1]==2:
            maxs = max(maxs,check[0][0]*10+check[1][0]+700)
    if check[0][1]==2:
        maxs = max(maxs,check[0][0]+200)
        if check[1][1]==2:
            maxs = max(maxs,max(check[0][0],check[1][0])*10+min(check[0][0],check[1][0])+300)
maxs = max(maxs,num[-1]+100)
print(maxs)