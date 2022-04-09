#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/7. 송아지 찾기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/7. 송아지 찾기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------
#------------ 내 풀이 코드 ----------------- => 몇개만 됨
from collections import  deque

#
# s,e =map(int,input().split())
# jump = [0]*10000
# ch = [False]*10000
# q = deque([s])
# ch[s] = True
# cnt = 0
# change = 0
# while q:
#     for _ in range(3):
#         targets = [q[0]-1,q[0]+1,q[0]+5]
#         for i in targets:
#             if not ch[i]:
#                 q.append(i)
#                 ch[i] = True
#                 if i == e:
#                     print(cnt)
#                     sys.exit(0)
#         q.popleft()
#     else:
#         cnt+=1



#-----------영상 풀이 코드 -------------------

MAX = 10000
ch = [0]*(MAX+1)
dis = [0]*(MAX+1)
n,m = map(int, input().split())
ch[n] = 1
dis[n] = 0
dq = deque()
dq.append(n)
while dq:
    now = dq.popleft()
    if now == m:
        break
    for next in (now-1,now+1,now+5):
        if 0 < next <= MAX:
            if not ch[next]:
                dq.append(next)
                ch[next] = 1
                dis[next] = dis[now]+1
                if next ==m:
                    break
print(dis[m])