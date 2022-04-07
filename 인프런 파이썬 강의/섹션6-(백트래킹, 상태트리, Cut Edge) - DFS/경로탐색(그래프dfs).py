#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/15. 경로탐색/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/15. 경로탐색/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 ----------------- => 4,5 효율성 싱패
# def dfs(s):
#     global cnt
#     global ch
#     global root
#     if s==n-1:
#         cnt+=1
#         return
#     else:
#         if 1 not in matrix[s]:
#             return
#         ch[s] = 1  -----------------------------------> 실수
#         for i in range(n):
#             if not ch[i] and matrix[s][i]:
#                       ---------------------------------> 여기에 와야 함
#                 dfs(i)
#                 ch[s] = 0
#
#
# n, m = map(int, input().split())
# infos = [list(map(int, input().split())) for _ in range(m)]
# matrix = [[0] * n for _ in range(n)]
# for info in infos:
#     matrix[info[0]-1][info[1]-1] = 1
# # for i in range(n):
# #     matrix[i][i] = 1
# # for c in matrix:
# #     for i in c:
# #         print(i, end=" ")
# #     print()
# ch = [0] * (n + 1)
# cnt =0
# ch[0] = 1
# dfs(0)
# print(cnt)

#-----------영상 풀이 코드 -------------------

def DFS(v):
    global cnt
    if v==n:
        cnt+=1
    else:
        for i in range(1,n+1):
            if matrix[v][i] and not ch[i]:
                ch[i] = 1
                DFS(i)
                ch[v] = 0

n, m = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n+1)]
ch = [0]*(n+1)
for i in range(m):
    a,b = map(int,input().split())
    matrix[a][b] =1
ch[1] = 1
cnt = 0
DFS(1)
print(cnt)