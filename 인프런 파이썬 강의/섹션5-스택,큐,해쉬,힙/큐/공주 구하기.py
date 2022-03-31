#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/5. 공주구하기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/5. 공주구하기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------  => 설명 듣고 품
from collections import  deque
def solution():
    n,k = map(int,input().split())
    q =deque(i for i in range(1,n+1))
    while len(q) > 1:
        for _ in range(k-1):
            q.append(q.popleft())
        q.popleft()

    return q[0]



print(solution())


#-----------영상 풀이 코드 -------------------


