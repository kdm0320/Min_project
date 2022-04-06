#---------- 정답 입력 코드 -----------------
import datetime
import sys
NUM = 4
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/8. 순열 구하기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/8. 순열 구하기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------
from itertools import permutations
import time
def solution(): # => 라이브러리 사용
    start = time.time()
    n,m = map(int, input().split())
    a = [i for i in range(1,n+1)]
    c = list(permutations(a,m))
    for i in c:
        for j in i:
            print(j, end=" ")
        print()
    print(len(c))
    end = time.time()
    print(f"{end - start:.5f} sec")

# solution()

def dfs(l):
    if l==m:
        global cnt
        for i in range(m):
            print(res[i], end=" ")
        print()
        cnt+=1
        return
    else:
        for i in range(1,n+1):
            if not check[i]:
                res[l] = i
                check[i] = 1
                dfs(l+1)
                check[i] = 0
start = time.time()
n,m = map(int, input().split())
res = [0]*m
check = [0]*(n+1)
cnt = 0
dfs(0)
print(cnt)
end = time.time()
print(f"{end - start:.5f} sec")
#-----------영상 풀이 코드 ------------------- => 위랑 같음
