#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/15. 토마토/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/15. 토마토/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

import time
#------------ 내 풀이 코드 -----------------
# from collections import deque
#
# def change(c):
#     check = False
#     for i in range(n):
#         for j in range(m):
#             if ts[i][j] == c-1 and ch[i][j]==0:
#                 ch[i][j] = 1
#                 for k in range(4):
#                     x = i+dx[k]
#                     y = j+dy[k]
#                     if 0<=x<n and 0<=y<m and ts[x][y] == 0 and ch[x][y]==0:
#                         ts[x][y] = c
#                         if not check:
#                             check=True
#
#     return check # 1이 안바뀌었다 => 익을 수 있는 토마토가 없거나 다익었다.
# start = time.time()
# cnt = 0
# m,n = map(int, input().split())
# ts = [list(map(int, input().split())) for _ in range(n)]
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# q = deque()
# ch = [[0]*m for _ in range(n)]
# c=2
# while True:
#     a = change(c)
#     if a:
#         cnt+=1
#         c+=1
#     else:
#         if c == 2:
#             print(0)
#             break
#         for i in range(n):
#             if 0 in ts[i]:
#                 print(-1)
#                 end = time.time()
#                 print(f"{end - start:.5f} sec")
#                 sys.exit(0)
#         else:
#             print(cnt)
#             break
# end = time.time()
# print(f"{end - start:.5f} sec")
#-----------영상 풀이 코드 -------------------

from collections import deque
start = time.time()

cnt = 0
m,n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
q=deque()
dis = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            q.append((i,j))

while q:
    tmp = q.popleft()
    for i in range(4):
        xx = tmp[0]+dx[i]
        yy = tmp[1]+dy[i]
        if 0<=xx< n and 0<= yy < m and board[xx][yy] == 0:
            board[xx][yy] = 1
            dis[xx][yy] = dis[tmp[0]][tmp[1]]+1
            q.append((xx,yy))
flag = 1
for i in range(n):
    for j in range(m):
        if board[i][j]==0:
            flag = 0
result = 0
if flag==1:
    for i in range(n):
        for j in range(m):
            if dis[i][j] > result:
                result=dis[i][j]
    print(result)
else:
    print(-1)
end = time.time()
print(f"{end - start:.5f} sec")