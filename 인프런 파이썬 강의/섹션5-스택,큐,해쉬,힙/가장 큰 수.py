#---------- 정답 입력 코드 -----------------
import sys
NUM = 3
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/1. 가장 큰 수/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/1. 가장 큰 수/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------  => 설명 들어도 실패

def solution():
    n,m = input().split()
    M = int(m)
    q = []
    cnt = 0
    for i in n:
        if M <=0:
            q.append(i)
            continue
        if len(q)==0:
            q.append(i)
            continue
        for j in q:
            if int(j) < int(i):
                cnt+=1
                M-=1

        for _ in range(cnt):
            q.pop()
        q.append(i)
        cnt=0
    return ''.join(q[:len(n)-int(m)])






# print(solutionlution())


#-----------영상 풀이 코드 -------------------
num,m =map(int, input().split())
num = list(map(int,str(num)))
stack = []
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack = stack[:-m]
res = ''.join(map(str,stack))
print(res)
