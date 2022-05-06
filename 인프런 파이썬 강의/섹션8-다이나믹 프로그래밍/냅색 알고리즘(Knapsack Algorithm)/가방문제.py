# ---------- 정답 입력 코드 -----------------
import sys

NUM = 5
sys.stdin = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 8/9. 가방문제/in{NUM}.txt", "rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 8/9. 가방문제/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-' * 50}")
# ----------------------------------------

import time

# ------------ 내 풀이 코드 ----------------- => 설명 듣고 품
# start = time.time()

# n,l = map(int, input().split())
# js = [list(map(int,input().split())) for _ in range(n)]
# dy = [0]*(l+1)
# for j in js:
#     for i in range(j[0],l+1):
#         dy[i] = max(dy[i-j[0]]+j[1],dy[i])
#
#
# print(dy[l])
#
# end = time.time()
# print(f"{end - start:.5f} sec")

# -----------영상 풀이 코드 -------------------

# start = time.time()
#
# n,m = map(int, input().split())
# dy = [0]*(m+1)
# for i in range(n):
#     w,v = map(int,input().split())
#     for j in range(w,m+1):
#         dy[j] = max(dy[j - w] + v, dy[j])
#
#
# print(dy[m])
#
# end = time.time()
# print(f"{end - start:.5f} sec")