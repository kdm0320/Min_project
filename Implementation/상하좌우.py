n = int(input())
space = [1,1]

roots = list(input().split())

method = {"L":0,"R":1,"U":2,"D":3}
dx = [0,0,-1,1]
dy = [-1,1,0,0]
x=1
y=1
for i in roots:
    temp_x = x+dx[method[i]]
    temp_y = y+dy[method[i]]
    if temp_x > n or temp_x < 1 or temp_y < 1 or temp_y > n:
        pass
    else:
        x = temp_x
        y = temp_y
print(x,y)
