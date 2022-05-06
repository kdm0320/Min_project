# ---------- 정답 입력 코드 -----------------
import sys

NUM = 5
sys.stdin = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 8/12. 플로이드 워샬 알고리즘/in{NUM}.txt", "rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 8/12. 플로이드 워샬 알고리즘/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-' * 50}")
# ----------------------------------------

import time
M = int(1e9)
# ------------ 내 풀이 코드 -----------------
start = time.time()
n,m  = map(int, input().split())
graph = [[M] * (n+1) for _ in range(n+1)]
root = [[M]*(n+1) for _ in range(n+1)]
for a in range(1,n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0
            root[a][b] = [a,b]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c
    root[a][b] = [a,b]
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if graph[a][b] > graph[a][k]+graph[k][b]:
                root[a][b] = [a,k,b]
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == M:
            print("M", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
print()
for a in range(1,n+1):
    for b in range(1,n+1):
        if root[a][b] == M:
            print("M", end=" ")
        else:
            print(root[a][b], end=" ")
    print()
end = time.time()
print(f"{end - start:.5f} sec")

# -----------영상 풀이 코드 -------------------

# start = time.time()
# n, m = map(int, input().split())
# dis = [[5000] * (n + 1) for _ in range(n + 1)]
# for i in range(1, n + 1):
#     dis[i][i] = 0
# for i in range(m):
#     a, b, c = map(int, input().split())
#     dis[a][b] = c
# for k in range(1, n + 1):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if dis[i][j] == 5000:
#             print("M", end=' ')
#         else:
#             print(dis[i][j], end=' ')
#     print()
#
# end = time.time()
# print(f"{end - start:.5f} sec")