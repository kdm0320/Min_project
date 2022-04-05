#---------- 정답 입력 코드 -----------------
import datetime
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/7. 동전교환/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/7. 동전교환/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 ----------------- => 설명 듣고 품
def dfs(l,sum):
    global cnt
    if l >= cnt:
        return
    if sum > m:
        return
    elif sum==m:
        cnt=l
        return
    else:
        for i in coins:
            dfs(l+1,sum+i)

n = int(input())
coins = list(map(int, input().split()))
m = int(input())
coins.sort(reverse=True)
cnt=2146000
dfs(0,0)
print(cnt)



#-----------영상 풀이 코드 -------------------
# def DFS(l,sum):
#     global res
#     if l >= res:
#         return
#     if sum > m:
#         return
#     if sum==m:
#         if l < res:
#             res = l
#     else:
#         for i in range(n):
#             DFS(l+1,sum+coins[i])
#
# n = int(input())
# coins = list(map(int, input().split()))
# m = int(input())
# res = 214700000
# coins.sort(reverse=True)
# DFS(0,0)
# print(res)