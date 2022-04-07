#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/11. 수들의 조합/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/11. 수들의 조합/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------
import time
#------------ 내 풀이 코드 -----------------
# def dfs(l,s):
#     global cnt
#     if l==k:
#         if sum(res)%m==0:
#             cnt+=1
#         return
#     else:
#         global nums
#         for i in range(s,n+1):
#             res[l] = nums[i-1]
#             dfs(l+1,i+1)
# start = time.time()
# n,k = map(int, input().split())
# nums = list(map(int,input().split()))
# m = int(input())
# res = [0]*k
# cnt=0
# dfs(0,1)
# print(cnt)
# end = time.time()
# print(f"{end - start:.5f} sec")
#-----------영상 풀이 코드 -------------------
def dfs(l,s,sum):
    global cnt
    if l==k:
        if sum%m==0:
            cnt+=1
        return
    else:
        global nums
        for i in range(s,n+1):
            res[l] = nums[i-1]
            dfs(l+1,i+1,sum+nums[i-1])
start =time.time()
n,k = map(int, input().split())
nums = list(map(int,input().split()))
m = int(input())
res = [0]*k
cnt=0
dfs(0,1,0)
print(cnt)
end = time.time()
print(f"{end - start:.5f} sec")