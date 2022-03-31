#---------- 정답 입력 코드 -----------------
import sys
NUM = 3
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/8. 단어찾기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/8. 단어찾기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------
from collections import  deque
def solution():
    n = int(input())
    q = list(input() for _ in range(n))
    p = list(input() for _ in range(n-1))
    q.sort()
    p.sort()
    for i in range(n-1):
        if q[i] != p[i]:
            print(q[i])
            break
# solution()


#-----------영상 풀이 코드 -------------------
n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1
for i in range(n-1):
    word = input()
    p[word] = 0
for key,value in p.items():
    if value==1:
        print(key)
        break
