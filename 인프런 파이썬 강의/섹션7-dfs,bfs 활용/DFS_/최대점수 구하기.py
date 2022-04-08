#---------- 정답 입력 코드 -----------------
import sys
NUM =2
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/1. 최대점수 구하기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/1. 최대점수 구하기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 ----------------- => 4,5 실패
# def dfs(v,sc,t):
#     global score
#     global k
#     global m
#     a = k
#     b = score
#     c = m
#     if t>m:
#         return
#     if t==m:
#         score = max(score, sc)
#         return
#     else:
#         for i in range(n):
#             if not ch[i]:
#                 dfs(i,sc+k[i][0],t+k[i][1])
#                 score = max(score,sc)
#             ch[v] = 1
#
#
#
#
# n, m = map(int, input().split())
# k = [tuple(map(int, input().split())) for _ in range(n)]
# k.sort(reverse=True)
# ch = [0]*n
# score = -21467000
# dfs(0,0,0)
# print(score)
#-----------영상 풀이 코드 -------------------

def DFS(L,sum,time):
    global res
    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L+1,sum+pv[L],time+pt[L])
        DFS(L+1,sum,time)

n, m = map(int, input().split())
pv = []
pt = []
for i in range(n):
    a,b = map(int,input().split())
    pv.append(a)
    pt.append(b)
res = -21470000
DFS(0,0,0)
print(res)
