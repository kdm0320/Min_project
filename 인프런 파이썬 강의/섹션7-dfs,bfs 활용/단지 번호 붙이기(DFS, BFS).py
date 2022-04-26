#---------- 정답 입력 코드 -----------------
import sys
NUM = 1
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/12. 단지번호붙이기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/12. 단지번호붙이기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------
# def dfs(x,y):
#     global cnt
#     for i in range(4):
#         tx = x+dx[i]
#         ty = y+dy[i]
#         if 0 <= tx < n and 0 <= ty < n and houses[tx][ty] == "1":
#             cnt+=1
#             houses[tx][ty] = "0"
#             dfs(tx,ty)
#
#
#
# n = int(input())
# houses = [list(input()) for _ in range(n)]
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# cnt = 0
# res = []
# for i in range(n):
#     for j in range(n):
#         if houses[i][j] == "1":
#             dfs(i,j)
#             res.append(cnt)
#             cnt=0
# print(len(res))
# for i in sorted(res):
#     print(i)
#-----------영상 풀이 코드 -------------------

def dfs(x,y):
    global cnt
    cnt+=1
    board[x][y] = 0
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<= xx < n and 0<= yy < n and board[xx][yy]==1:
            dfs(xx,yy)


n = int(input())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
board = [list(map(int, input())) for _ in range(n)]
res = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt=0
            dfs(i,j)
            res.append(cnt)
print(len(res))
for i in sorted(res):
    print(i)