# ---------- 정답 입력 코드 -----------------
import sys

NUM = 5
sys.stdin = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 8/13. 회장뽑기/in{NUM}.txt", "rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 8/13. 회장뽑기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-' * 50}")
# ----------------------------------------

import time
M = int(1e9)
# ------------ 내 풀이 코드 ----------------- => 실패
# start = time.time()
# n  = int(input())
# graph = [[M] * (n+1) for _ in range(n+1)]
# for a in range(1,n+1):
#     for b in range(1, n+1):
#         if a==b:
#             graph[a][b] = 0
#
# while True:
#     a,b = map(int, input().split())
#     if a < 0:
#         break
#     graph[a][b] = 1
#
# for k in range(1,n+1):
#     for a in range(1,n+1):
#         for b in range(1,n+1):
#             graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
#
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if graph[i][j] == M:
#             print("M", end=' ')
#         else:
#             print(graph[i][j], end=' ')
#     print()
# end = time.time()
# print(f"{end - start:.5f} sec")

# -----------영상 풀이 코드 -------------------

start = time.time()
n = int(input())
dis = [[100] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dis[i][i] = 0
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    dis[a][b] = 1
    dis[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])


res = [0]*(n+1)
score = 100
for i in range(1,n+1):
    for j in range(1,n+1):
        res[i] = max(res[i],dis[i][j])
    score = min(score,res[i])

out = []
for i in range(1,n+1):
    if res[i]==score:
        out.append(i)
print(score,len(out))
for i in out:
    print(i, end=" ")
print()
end = time.time()
print(f"{end - start:.5f} sec")