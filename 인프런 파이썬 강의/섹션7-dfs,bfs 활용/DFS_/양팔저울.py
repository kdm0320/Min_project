#---------- 정답 입력 코드 -----------------
import sys
NUM = 4
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/3. 양팔저울/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/3. 양팔저울/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------
from itertools import combinations
#------------ 내 풀이 코드 ----------------- => 실패
# def ch(w,li):
#     pass
#
# def solution():
#     k = int(input())
#     nums = list(map(int, input().split()))
#     w = [i for i in range(1,sum(nums)+1)]
#     coms = set()
#     for i in range(1,k+1):
#         a = list(combinations(nums,i))
#         for j in a:
#             coms.add(sum(j))
#     list(coms)
#     cnt=0
#     for i in w:
#         if i not in coms:
#             for j in nums:
#                 if i+j > sum(nums):
#                     cnt+=1
#                     break
#                 else:
#                     if i+j in coms:
#                         break
#                     else:
#                         continue
#             else:
#                 cnt+=1
#     print(cnt)
# solution()



#-----------영상 풀이 코드 -------------------
def DFS(L,sum):
    global res
    if L==k:
        if 0<sum<=s:
            res.add(sum)
    else:
        DFS(L+1,sum+G[L])
        DFS(L+1,sum-G[L])
        DFS(L+1,sum)



k  = int(input())
G = list(map(int, input().split()))
s = sum(G)
res = set()
DFS(0,0)
print(s-len(res))