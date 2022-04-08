#---------- 정답 입력 코드 -----------------
import sys
NUM =5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/2. 휴가/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/2. 휴가/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------
# def DFS(L,sum):
#     global res
#     if L > n:
#         return
#     if L == n:
#         if sum > res:
#             res = sum
#     else:
#         DFS(L+pt[L],sum+pv[L])
#         DFS(L+1,sum)
#
# n = int(input())
# pv = []
# pt = []
# for i in range(n):
#     a,b = map(int,input().split())
#     pv.append(b)
#     pt.append(a)
# res = -21470000
# DFS(0,0)
# print(res)
#-----------영상 풀이 코드 -------------------


def DFS(L,sum):
    global res
    if L == n+1:
        if sum > res:
            res = sum
    else:
        if L+T[L] <= n+1:
            DFS(L+T[L],sum+P[L])
        DFS(L+1,sum)

n = int(input())
T = list()
P = list()
for i in range(n):
    a,b = map(int,input().split())
    T.append(a)
    P.append(b)
res = -21470000
T.insert(0,0)
P.insert(0,0)
DFS(1,0)
print(res)