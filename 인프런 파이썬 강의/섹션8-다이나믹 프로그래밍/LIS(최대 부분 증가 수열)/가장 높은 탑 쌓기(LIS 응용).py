#---------- 정답 입력 코드 -----------------
import sys
NUM = 1
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 8/6. 가장 높은 탑 쌓기(LIS 응용)/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 8/6. 가장 높은 탑 쌓기(LIS 응용)/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

import time
#------------ 내 풀이 코드 ----------------- => 실패

# start = time.time()
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# arr.sort(reverse=True)
# dy = [0]*n
# dy[1] = arr[0][1]
# res = 0
# for i in range(1,n):
#     max = 0
#     for j in range(i-1,0,-1):
#         if arr[j][2] > arr[i][2] and dy[j] > max:
#             max = dy[j]
#
#     dy[i] = max+arr[i][1]
#     if dy[i] > res:
#         res = dy[i]
#
# print(res)
#
# end = time.time()
#
# print(f"{end - start:.5f} sec")

#-----------영상 풀이 코드 -------------------
start = time.time()

n = int(input())
bricks = []
for i in range(n):
    a, b, c = map(int, input().split())
    bricks.append((a, b, c))
print(bricks)
bricks.sort(reverse=True)
print(bricks)
dy = [0] * n
dy[0] = bricks[0][1]
res = bricks[0][1]
for i in range(1, n):
    max_h = 0
    for j in range(i - 1, -1, -1):
        if bricks[j][2] > bricks[i][2] and dy[j] > max_h:
            max_h = dy[j]
    dy[i] = max_h + bricks[i][1]
    res = max(res, dy[i])
print(res)

end = time.time()

print(f"{end - start:.5f} sec")