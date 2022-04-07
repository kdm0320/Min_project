#---------- 정답 입력 코드 -----------------
import datetime
import sys
NUM = 1
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/9. 수열 추측하기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/9. 수열 추측하기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------
from itertools import permutations
import time
def solution(): #permutations 이용
    start = time.time()
    n,f = map(int, input().split())
    lis = [i for i in range(1,n+1)]
    new = list(permutations(lis,n))
    for i in new:
        temp = list(i)
        for _ in range(n):
            for j in range(len(temp)-1):
                temp[j] = temp[j]+temp[j+1]
            if len(temp)>1:
                temp.pop()
            else:
                if temp[0] == f:
                    for k in i:
                        print(k,end=" ")
                    end = time.time()
                    print(f"{end - start:.5f} sec")
                    return
# solution()

#-----------영상 풀이 코드 -------------------
# def dfs(l,sum):
#     global end
#     global start
#     if l==n and sum==f:
#         for x in p:
#             print(x, end=" ")
#         end = time.time()
#         print(f"{end - start:.5f} sec")
#         sys.exit(0)
#     else:
#         for i in range(1,n+1):
#             if not ch[i]:
#                 ch[i] = 1
#                 p[l] = i
#                 dfs(l+1,sum+(p[l]*b[l]))
#                 ch[i] = 0
#
# start = time.time()
# n,f = map(int, input().split())
# p=[0]*n
# b=[1]*n
# ch=[0]*(n+1)
# for i in range(1,n):
#     b[i] = (b[i-1]*(n-i))//i #이항계수 구하는 방법
# dfs(0,0)

def library_solution():  #라이브러리 사용
    start = time.time()
    n, f = map(int, input().split())
    b=[1]*n
    for i in range(1,n):
        b[i] = (b[i-1]*(n-i))//i #이항계수 구하는 방법
    a = list(range(1,n+1))
    for tmp in permutations(a,n):
        check = 0
        for i,x in enumerate(tmp):
            check+=(x*b[i])
        if check == f:
            for k in tmp:
                print(k,end=" ")
            end = time.time()
            print(f"{end - start:.5f} sec")
            return
library_solution()