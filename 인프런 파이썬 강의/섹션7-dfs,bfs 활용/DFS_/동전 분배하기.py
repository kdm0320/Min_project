#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/5. 동전분배하기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/5. 동전분배하기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------
#------------ 내 풀이 코드 ----------------- => 3,4,5실패

# def dfs(l):
#     global res
#     global a
#     c = res
#
#     # if max(a)-min(a) >= res: -----> 위치가 문제
#     #     return
#     # else:
#     if l==n:
#         #----------------------------> 이리로 와야함
#         c = set(a)
#         if len(c)==3:
#             res = max(a)-min(a)
#     else:
#         k = a
#         for i in range(3):
#                 a[i]+=coins[l]
#                 dfs(l+1)
#                 a[i] -= coins[l]
#
# n = int(input())
# coins = [int(input()) for _ in range(n)]
# a =[0]*3
# res = 21467000
# dfs(0)
# print(res)
#-----------영상 풀이 코드 -------------------

def DFS(l):
    global res
    if l==n:
        cha = max(money) - min(money)
        if cha < res:
            tmp = set(money)
            if len(tmp) < 3:
                return
            else:
                res = cha
    else:
        for i in range(3):
            money[i]+=coin[l]
            DFS(l+1)
            money[i]-=coin[l]


n = int(input())
coin = [int(input()) for _ in range(n)]
money = [0]*3
res = 214700000
DFS(0)
print(res)