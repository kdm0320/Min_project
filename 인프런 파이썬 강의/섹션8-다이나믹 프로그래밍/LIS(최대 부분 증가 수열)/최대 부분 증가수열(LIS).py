#---------- 정답 입력 코드 -----------------
import sys
NUM = 1
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 8/4. 최대부분증가수열/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 8/4. 최대부분증가수열/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

import time
#------------ 내 풀이 코드 ----------------- => 설명듣고 품

# start = time.time()
#
# n = int(input())
# se = list(map(int, input().split()))
# dy = [0]*n
# dy[0] = 1
# m = -21470000
# for i in range(1,n):
#     for j in range(i):
#         if se[j] < se[i]:
#             dy[i] = max(dy[i],dy[j]+1)
#     if m < dy[i]:
#         m = max(dy[i],m)
#     if dy[i] == 0:
#         dy[i] = 1
#
# print(m)
#
# end = time.time()
#
# print(f"{end - start:.5f} sec")

#-----------영상 풀이 코드 -------------------
start = time.time()

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)
dy = [0]*(n+1)
dy[1] = 1
res = 0
for i in range(2,n+1):
    max = 0
    for j in range(i-1,0,-1):
        if arr[j] < arr[i] and dy[j] > max:
            max = dy[j]

    dy[i] = max+1
    if dy[i] > res:
        res = dy[i]

print(res)


end = time.time()

print(f"{end - start:.5f} sec")