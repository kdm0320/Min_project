#---------- 정답 입력 코드 -----------------
import datetime
import sys
NUM = 4
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/6. 중복순열 구하기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/6. 중복순열 구하기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 ----------------- => 라이브러리 사용
from itertools import product
import time,math
def solution():
    start = time.time()
    n,m = map(int, input().split())
    a = [i for i in range(1,n+1)]
    c = list(product(a,repeat=m))
    for i in c:
        for j in i:
            print(j, end=" ")
        print()
    print(len(c))
    end = time.time()
    print(f"{end - start:.5f} sec")

# solution()

#-----------영상 풀이 코드 -------------------
def dfs(L):
    if L==m:
        global cnt
        for i in res:
            print(i,end=" ")
        cnt+=1
        print()
        return
    else:
        for i in range(1,n+1):
            res[L] = i
            dfs(L+1)


start = time.time()
n,m = map(int, input().split())
res =[0]*m
cnt = 0
dfs(0)
print(cnt)
end = time.time()
print(f"{end - start:.5f} sec")