#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 4/8. 침몰하는 타이타닉/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 4/8. 침몰하는 타이타닉/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------
from collections import  deque
def solution():
    n,m = map(int,input().split())
    w = list(map(int,input().split()))
    cnt=0
    w.sort()
    q = deque(w)
    while True:
        try:
            if q[0]+q[-1] > m:
                cnt+=1
                q.pop()
            else:
                cnt+=1
                q.pop()
                q.popleft()
        except IndexError:
            return cnt


print(solution())


#-----------영상 풀이 코드 -------------------
#같음