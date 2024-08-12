import sys

n, m = map(int,sys.stdin.readline().split())
room = []

for i in range(n):
    l, k = sys.stdin.readline().split()
    l = int(l)
    go_in = False
    
    for j in range(len(room)):
        if len(room[j])==m:
            go_in = False
        elif l > room[j][0][1]+10 or l < room[j][0][1]-10:
            go_in = False
        else:
            go_in = True
            room[j].append((k,l))
            break
            
    if not go_in:
        room.append([(k,l)])
        
for i in room:
    i.sort()
    if len(i)==m:
        print("Started!")
    else:
        print("Waiting!")
    for j in i:
        print(j[1],j[0])