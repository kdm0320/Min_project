# ---------- 정답 입력 코드 -----------------
import sys

NUM = 3
sys.stdin = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 8/10. 동전교환/in{NUM}.txt", "rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 8/10. 동전교환/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-' * 50}")
# ----------------------------------------

import time

# ------------ 내 풀이 코드 ----------------- => 실패
# start = time.time()
#
# n = int(input())
# coins = list(map(int, input().split()))
# m = int(input())
# dy = [2147000]*(m+1)
# dy[0] = 0
# for i in range(n):
#     for j in range(coins[i],m):
#         dy[j] = min(dy[j-coins[i]]+1,dy[j])
#
# print(dy[m])
# end = time.time()
# print(f"{end - start:.5f} sec")

# -----------영상 풀이 코드 -------------------

start = time.time()

n = int(input())
coin = list(map(int, input().split()))
m = int(input())
dy = [1000]*(m+1)
dy[0] = 0
for i in range(n):
    for j in range(coin[i],m+1):
        dy[j] = min(dy[j-coin[i]]+1,dy[j])

print(dy[m])
end = time.time()
print(f"{end - start:.5f} sec")