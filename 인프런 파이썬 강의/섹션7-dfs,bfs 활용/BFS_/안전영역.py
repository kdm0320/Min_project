#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/14. 안전영역/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/14. 안전영역/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------
# import time
# from collections import  deque
# # sys.setrecursionlimit(10**2)
#
# import copy
# start = time.time()
# n = int(input())
# infos = [list(map(int, input().split())) for _ in range(n)]
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# # mi = 214700000
# # ma = -214700000
# # for i in range(n):
# #     info = list(map(int, input().split()))
# #     if max(info) > ma:
# #         ma = max(info)
# #     if min(info) < mi:
# #         mi = min(info)
# #     infos.append(info)
# q = deque()
# MAX = -2147000
# for k in range(100):
#     ch = [[0]*n for _ in range(n)]
#     cnt = 0
#     for i in range(n):
#         for j in range(n):
#             if infos[i][j] > k and ch[i][j]==0:
#                 q.append((i,j))
#                 ch[i][j]=1
#                 while q:
#                     tmp = q.popleft()
#                     for l in range(4):
#                         x = tmp[0]+dx[l]
#                         y = tmp[1]+dy[l]
#                         if 0<=x<n and 0<=y<n and infos[x][y] > k and ch[x][y]==0:
#                             ch[x][y] = 1
#                             q.append((x,y))
#                 cnt+=1
#     if cnt==0:
#         break
#     if cnt > MAX:
#         MAX = cnt
# print(MAX)
# end = time.time()
# print(f"{end - start:.5f} sec")
#-----------영상 풀이 코드 -------------------
# def dfs(x,y,h):
#     ch[x][y] = 1
#     for i in range(4):
#         xx = x+dx[i]
#         yy = y+dy[i]
#         if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy] > h:
#             dfs(xx,yy,h)
#
# start = time.time()
#
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# n = int(input())
# cnt=0
# res = 0
# board = [list(map(int, input().split())) for _ in range(n)]
# for h in range(100):
#     ch = [[0]*n for _ in range(n)]
#     cnt=0
#     for i in range(n):
#         for j in range(n):
#             if ch[i][j]==0 and board[i][j] > h:
#                 cnt+=1
#                 dfs(i,j,h)
#     res=max(res,cnt)
#     if cnt == 0:
#         break
# print(res)
# end = time.time()
# print(f"{end - start:.5f} sec")