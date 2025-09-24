import sys

n = int(sys.stdin.readline())
time1, time2 = "00:00", "00:00"
score1, score2 = 0, 0
start = (0, "00:00")
end = "48:00"
last_winning = 0

def format_time(t):
    t1, t2 = t.split(":")
    
    if len(t1) == 1:
        t1 = "0" + t1
    if len(t2) == 1:
        t2 = "0" + t2
        
    return f"{t1}:{t2}"

def sub_time(s, e):
    t1, t2 = 0, 0
    s1, s2 = s.split(":")
    e1, e2 = e.split(":")
    
    t1 = int(e1) - int(s1)
    if int(e2) - int(s2) < 0:
        t2 = 60 - int(s2) + int(e2)
        t1 -= 1
    else:
        t2 = int(e2) - int(s2)
        
    t = format_time(f"{str(t1)}:{str(t2)}")
    
    return t
    
def add_time(s, e):
    t1, t2 = 0, 0
    s1, s2 = s.split(":")
    e1, e2 = e.split(":")
    
    t1 = int(s1) + int(e1)
    t2 = int(s2) + int(e2)
    if t2 >= 60:
        t2 -= 60
        t1 += 1
    
    t = format_time(f"{str(t1)}:{str(t2)}")
    
    return t

for _ in range(n):
    team, time = map(str, sys.stdin.readline().split())
    
    if team == "1":
        score1 += 1
    else:
        score2 += 1
        
    if score1 > score2:
        winning = 1
    elif score1 < score2:
        winning = 2
    else:
        winning = 0
        
    if not winning:
        if start[0] == 1:
            temp = sub_time(start[1], time)
            time1 = add_time(temp, time1)
        else:
            temp = sub_time(start[1], time)
            time2 = add_time(temp, time2)
            
    elif last_winning != winning:
        if winning == 1:
            start = (1, time)
        else:
            start = (2, time)
            
    last_winning = winning
    
if score1 > score2:
    temp = sub_time(start[1], end)
    time1 = add_time(temp, time1)
elif score1 < score2:
    temp = sub_time(start[1], end)
    time2 = add_time(temp, time2)
    
print(time1)
print(time2)
