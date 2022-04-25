#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/10. 미로탐색/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/10. 미로탐색/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------


# def dfs(x,y):
#     global cnt
#     if x==6 and y==6:
#         cnt+=1
#         return
#     if board[x][y] == 0 and dis[x][y] == 0:
#         dis[x][y] = 1
#         for i in range(4):
#             tx = x+dx[i]
#             ty = y + dy[i]
#             if 0<=tx<=6 and 0<=ty<=6:
#                 dfs(tx,ty)
#         dis[x][y] = 0
#
# board = [list(map(int, input().split())) for _ in range(7)]
# dis = [[0]*7 for _ in range(7)]
#
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
#
# cnt=0
# dfs(0,0)
# print(cnt)
#-----------영상 풀이 코드 -------------------

def dfs(x,y):
    global cnt
    if x==6 and y==6:
        cnt+=1
        return
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and board[xx][yy]==0:
                board[xx][yy] = 1
                dfs(xx,yy)
                board[xx][yy] = 0



board = [list(map(int, input().split())) for _ in range(7)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt=0
board[0][0] = 1
dfs(0,0)
print(cnt)
