#---------- 정답 입력 코드 -----------------
import sys
NUM = 1
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/16. 사다리타기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/16. 사다리타기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

import time
#------------ 내 풀이 코드 ----------------- ==> 도착지가 2인 행을 찾기 위해 0부터 처음부터 검사 - 비효율
# start = time.time()
#
# def dfs(x,y):
#     global ch
#     global two_ch
#     if two_ch or ch:
#         return
#     roots[x][y] = 1
#     if x==9:
#         if lads[x][y] == 2:
#             two_ch = True
#             return
#         else:
#             ch=True
#             return
#     for i in range(3):
#         tx = x+dx[i]
#         ty = y+dy[i]
#         if 0<=tx<10 and 0<=ty <10 and roots[tx][ty]==0 and lads[tx][ty] != 0:
#             roots[tx][ty]=1
#             dfs(tx,ty)
#
# lads = [list(map(int, input().split())) for _ in range(10)]
# two_ch = False
# dx = [0,0,1]
# dy = [1,-1,0]
# answer = 0
# for i in range(10):
#     roots = [[0] * 10 for _ in range(10)]
#     answer = i
#     if lads[0][i] != 0:
#         ch = False
#         dfs(0, i)
#         if two_ch:
#             print(i)
#             break
#     else:
#         continue
# end = time.time()
# print(f"{end - start:.5f} sec")
#-----------영상 풀이 코드 -------------------

def dfs(x,y):
    ch[x][y] = 1
    if x==0:
        print(y)
    else:
        if y-1 >= 0 and board[x][y-1]==1 and ch[x][y-1]==0:
            dfs(x,y-1)
        elif y+1 < 10 and board[x][y+1]==1 and ch[x][y+1]==0:
            dfs(x,y+1)
        else:
            dfs(x-1,y)


start = time.time()

board = [list(map(int, input().split())) for _ in range(10)]
ch = [[0]*10 for _ in range(10)]
for y in range(10):
    if board[9][y]==2:
        dfs(9,y)

end = time.time()
print(f"{end - start:.5f} sec")