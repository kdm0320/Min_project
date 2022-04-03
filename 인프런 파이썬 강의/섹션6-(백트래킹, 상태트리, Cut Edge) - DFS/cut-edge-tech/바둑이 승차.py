#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/5. 바둑이 승차/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/5. 바둑이 승차/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 ----------------- => 효율성 실패
# def dfs(l,sum):
#   if sum > c:
#       return
#   if l == n:
#     global m
#     m = max(sum,m)
#   else:
#       dfs(l+1,sum+a[l])
#       dfs(l+1,sum)
#
# c,n = map(int, input().split())
# a = [int(input()) for _ in range(n)]
# m =  0
# dfs(0,0)
# print(m)


#-----------영상 풀이 코드 -------------------
def dfs(l,sum,tsum):
  global result
  if sum+(total-tsum) < result:
    return
  if c < sum :
    return
  if l==n:
    if sum > result:
      result = sum
  else:
    dfs(l+1, sum+a[l],tsum+a[l])
    dfs(l+1, sum,tsum+a[l])


c,n = map(int, input().split())
a = [0]*n
result = -2147000
for i in range(n):
  a[i] = int(input())
total = sum(a)
dfs(0,0,0)
print(result)