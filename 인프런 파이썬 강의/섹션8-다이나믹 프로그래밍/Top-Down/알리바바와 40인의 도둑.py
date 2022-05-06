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

# ------------ 내 풀이 코드 ----------------- => 실패

# def dfs(x,y):
#     for i in range(1, n):
#         for j in range(1, n):
#             up = i - 1
#             left = j - 1
#             dy[i][j] = min(dy[up][j], dy[i][left]) + boards[i][j]
#
# start = time.time()
#
# n = int(input())
# boards = [list(map(int,input().split())) for _ in range(n)]
# dy = [[0]*n for _ in range(n)]
# dy[0][0] = boards[0][0]
# for i in range(1,n):
#     dy[0][i] = dy[0][i-1]+boards[0][i]
#     dy[i][0] = dy[i-1][0]+boards[i][0]
#
# print(dy[n-1][n-1])
#
# end = time.time()
# print(f"{end - start:.5f} sec")

# -----------영상 풀이 코드 -------------------

def dfs(x,y):
    if dy[x][y] > 0:
        return dy[x][y]
    if x==0 and y==0:
        return arr[0][0]
    else:
        if y==0:
            dy[x][y] = dfs(x-1,y)+arr[x][y]
            return dfs(x-1,y)+arr[x][y]
        elif x==0:
            dy[x][y] = dfs(x,y-1)+arr[x][y]

        else:
            dy[x][y] = min(dfs(x-1,y),dfs(x,y-1))+arr[x][y]
        return dy[x][y]


start = time.time()
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)]
print(dfs(n-1,n-1))
end = time.time()
print(f"{end - start:.5f} sec")