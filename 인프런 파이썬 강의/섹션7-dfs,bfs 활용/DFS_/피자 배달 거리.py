#---------- 정답 입력 코드 -----------------
import sys
NUM = 1
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/17. 피자 배달 거리/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/17. 피자 배달 거리/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

import time
#------------ 내 풀이 코드 -----------------  => combinations 사용
from itertools import combinations

# start = time.time()
# n,m = map(int, input().split())
# hs = []
# s = []
# dist = 21470000
# for i in range(n):
#     a = list(map(int, input().split()))
#     for j in range(n):
#         if a[j]==1:
#             hs.append((i,j))
#         elif a[j]==2:
#             s.append((i,j))
#
# choices = list(combinations(s,m))
# for cs in choices:
#     tmp = 0
#     for h in hs:
#         tmp1 = 214670000
#         for c in cs:
#             tmp2 = abs(h[0] - c[0]) + abs(h[1] - c[1])
#             if tmp2 < tmp1:
#                 tmp1 = tmp2
#         tmp+=tmp1
#     if tmp < dist:
#         dist = tmp
#
# print(dist)
#
# end = time.time()
# print(f"{end - start:.5f} sec")

#-----------영상 풀이 코드 -------------------  => 재귀 사용해 조합구함 -> for 문 한번 덜 돌음

def dfs(l,s):
    global res
    if l==m:
        sum = 0
        for j in range(len(hs)):
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 2147000000
            for x in cb:
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis,abs(x1-x2)+abs(y1-y2))
            sum+=dis
        if sum < res:
            res = sum
    else:
        for i in range(s, len(pz)):
            cb[l]=i
            dfs(l+1,i+1)


start = time.time()

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
hs = []
pz = []
cb = [0]*m #=> 조합의 경우의 수를 저장하는 리스트
res = 214700000
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            hs.append((i,j))
        elif board[i][j]==2:
            pz.append((i,j))

dfs(0,0) #=> 조합재귀
print(res)
end = time.time()
print(f"{end - start:.5f} sec")