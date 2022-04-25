#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/11. 등산경로/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/11. 등산경로/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------

# def dfs(x,y):
#     global cnt
#     if x==max[1] and y==max[2]:
#         cnt+=1
#         return
#     else:
#         for i in range(4):
#             xx=x+dx[i]
#             yy=y+dy[i]
#             if 0<=xx<=n-1 and 0<=yy<=n-1 and ch[xx][yy]==0 and board[xx][yy] > board[x][y]:
#                 ch[xx][yy] = 1
#                 dfs(xx,yy)
#                 ch[xx][yy] = 0
#
#
#
# n = int(input())
# board = []
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# cnt=0
# ch = [[0]*n for _ in range(n)]
# min = [21460000,0,0]
# max = [-2146000,0,0]
# for r in range(n):
#     row = list(map(int,input().split()))
#     for c,j in enumerate(row):
#         if min[0] > j:
#             min[0] = j
#             min[1] = r
#             min[2] = c
#             continue
#         if max[0] < j:
#             max[0] = j
#             max[1] = r
#             max[2] = c
#
#     board.append(row)
# dfs(min[1],min[2])
# print(cnt)
#-----------영상 풀이 코드 -------------------
def dfs(x,y):
    global cnt
    if x==ex and y==ey:
        cnt+=1
        return
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<=n-1 and 0<=yy<=n-1 and ch[xx][yy]==0 and board[xx][yy] > board[x][y]:
                ch[xx][yy] = 1
                dfs(xx,yy)
                ch[xx][yy] = 0

n = int(input())
ch = [[0]*n for _ in range(n)]
board = [[0]*n for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt=0
max = -2147000000
min = 2147000000
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        if tmp[j] <min:
            min = tmp[j]
            sx=i
            sy=j
        if tmp[j] > max:
            max = tmp[j]
            ex=i
            ey=j
        board[i][j] = tmp[j]
ch[sx][sy] = 1
dfs(sx,sy)
print(cnt)

