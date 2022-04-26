#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/13. 섬나라 아일랜드/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/13. 섬나라 아일랜드/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 ----------------- => DFS 방식
# def dfs(x,y):
#     global cnt
#     for i in range(8):
#         tx = x+dx[i]
#         ty = y+dy[i]
#         if 0 <= tx < n and 0 <= ty < n and boards[tx][ty] == 1:
#             cnt+=1
#             boards[tx][ty] = 0
#             dfs(tx,ty)
#
#
#
# n = int(input())
# boards = [list(map(int, input().split())) for _ in range(n)]
# dx = [-1,-1,0,1,1,1,0,-1]
# dy = [0,1,1,1,0,-1,-1,-1]
# cnt = 0
# res = []
# for i in range(n):
#     for j in range(n):
#         if boards[i][j] == 1:
#             dfs(i,j)
#             res.append(cnt)
#             cnt=0
# print(len(res))

#-----------영상 풀이 코드 -------------------

from collections import deque


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
cnt = 0
q = deque()
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j] = 0
            q.append((i,j))
            while q:
                tmp = q.popleft()
                for k in range(8):
                    x = tmp[0]+dx[k]
                    y = tmp[1] + dy[k]
                    if 0<=x<n and 0<=y<n and board[x][y]==1:
                        board[x][y] = 0
                        q.append((x,y))
            cnt+=1
print(cnt)