#---------- 정답 입력 코드 -----------------
import sys
NUM = 2
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/6. 응급실/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/6. 응급실/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------
from collections import  deque
def solution():
    n,m = map(int,input().split())
    lis = list(map(int, input().split()))
    q =deque()
    for index, i in enumerate(lis):
        q.append((i,index))

    cnt=0
    while q:
        tmp = [i[0] for i in q]
        if q[0][0] < max(tmp):
            q.append(q.popleft())
        else:
            cnt+=1
            if q[0][1]==m:
                return cnt
            else:
                q.popleft()

# print(solution())


#-----------영상 풀이 코드 -------------------
n,m = map(int,input().split())
Q = [(pos,val) for pos, val in enumerate(list(map(int, input().split())))]
q = deque(Q)
cnt=0
while True:
    cur = q.popleft()
    if any(cur[1]<x[1] for x in q):
        q.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            break
print(cnt)

