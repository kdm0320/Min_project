# ---------- 정답 입력 코드 -----------------
import sys

NUM = 5
sys.stdin = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 8/11. 최대점수 구하기(냅색알고리즘)/in{NUM}.txt", "rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 8/11. 최대점수 구하기(냅색알고리즘)/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-' * 50}")
# ----------------------------------------

import time

# ------------ 내 풀이 코드 ----------------- => 실패
#
# start = time.time()
#
# n,m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# dy = [0]*(m+1)
# ch = [0]*n
# arr.sort(key= lambda x : x[1])
# print(arr)
# for i in range(n):
#     s, t = arr[i]
#
#
# print(dy[m])
#
# end = time.time()
# print(f"{end - start:.5f} sec")

# -----------영상 풀이 코드 -------------------

start = time.time()
n,m = map(int, input().split())
dy=[0]*(m+1)
for i in range(n):
    ps,pt = map(int, input().split())
    for j in range(m,pt-1,-1):
        dy[j] = max(dy[j],dy[j-pt]+ps)

print(dy[m])

end = time.time()
print(f"{end - start:.5f} sec")