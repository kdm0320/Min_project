
frame = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]

def dfs(x,y,n,m):
    if x <= -1 or x>=n or y <= -1 or y>=m:
        return False
    if frame[x][y] == 0:
        frame[x][y] = 1
        dfs(x-1,y,n,m)
        dfs(x,y-1,n,m)
        dfs(x+1,y,n,m)
        dfs(x-1,y+1,n,m)
        return True
    return False

def solution(frame):
    result = 0
    n = len(frame)
    m = len(frame[0])
    for i in range(n):
        for j in range(m):
            if dfs(i,j,n,m) == True:
                result +=1
    return result

print(solution(frame))
