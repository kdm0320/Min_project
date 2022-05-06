# ---------- 정답 입력 코드 -----------------
import sys

NUM = 1
sys.stdin = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 8/7, 8. 알리바바와 40인의 도둑/in{NUM}.txt", "rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 8/7, 8. 알리바바와 40인의 도둑/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-' * 50}")
# ----------------------------------------

import time

# ------------ 내 풀이 코드 -----------------

# start = time.time()
#
# n = int(input())
# boards = [list(map(int,input().split())) for _ in range(n)]
# dy = [[2147000]*n for _ in range(n)]
# dy[0][0] = boards[0][0]
# for i in range(n):
#     for j in range(n):
#         up = i-1
#         left = j-1
#         if up < 0:
#             dy[i][j] = min(dy[i][left]+boards[i][j],dy[i][j])
#         elif left < 0:
#             dy[i][j] = min(dy[up][j] + boards[i][j], dy[i][j])
#         else:
#             dy[i][j] = min(dy[up][j] + boards[i][j], dy[i][left] + boards[i][j])
#
# print(dy[n-1][n-1])
#
# end = time.time()
# print(f"{end - start:.5f} sec")

# -----------영상 풀이 코드 -------------------

start = time.time()
n = int(input())
boards = [list(map(int,input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)]
dy[0][0] = boards[0][0]
for i in range(1,n):
    dy[0][i] = dy[0][i-1]+boards[0][i]
    dy[i][0] = dy[i-1][0]+boards[i][0]
for i in range(1,n):
    for j in range(1,n):
        up = i - 1
        left = j-1
        dy[i][j] = min(dy[up][j] , dy[i][left])+ boards[i][j]
print(dy[n-1][n-1])
end = time.time()
print(f"{end - start:.5f} sec")