#---------- 정답 입력 코드 -----------------
import sys
NUM = 4
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 4/9. 증가수열 만들기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 4/9. 증가수열 만들기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------
from collections import  deque
def solution():
    n = int(input())
    w = list(map(int,input().split()))
    new = []
    answer = ""
    q = deque(w)
    if q[0] > q[-1]:
        new.append(q.pop())
        answer += "R"
    else:
        new.append(q.popleft())
        answer += "L"
    while len(q) > 0:
        ma = max(q[0],q[-1])
        mi  = min(q[0],q[-1])
        if ma <= new[-1]:
            break
        if len(q)==1:
            if q[0] > new[-1]:
                answer+="L"
                q.pop()
        else:
            if mi > new[-1]:
                if mi == q[0]:
                    new.append(q.popleft())
                    answer += "L"
                else:
                    new.append(q.pop())
                    answer += "R"
            else:
                if ma == q[0]:
                    new.append(q.popleft())
                    answer += "L"
                else:
                    new.append(q.pop())
                    answer += "R"

    print(len(answer))
    print(answer)




# solution()


#-----------영상 풀이 코드 -------------------
n = int(input())
w = list(map(int, input().split()))
lt=0
rt=n-1
last = 0
res = ""
tmp =[]
while lt <= rt:
    if w[lt] > last:
        tmp.append((w[lt],"L"))
    if w[rt] > last:
        tmp.append((w[rt],"R"))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res+=tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == "L":
            lt+=1
        else:
            rt-=1
    tmp.clear()

print(len(res))
print(res)
