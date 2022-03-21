#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 4/10. 역수열/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 4/10. 역수열/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------


#------------ 내 풀이 코드 ----------------- => 코드 전 설명 듣고 품
from collections import Counter
def solution():

    n = int(input())
    w = list(map(int,input().split()))
    c = [0]*n
    cnt = 0
    for k,i in enumerate(w):
        for ind,j in enumerate(c):
            if j==0:
                if cnt >=i:
                    c[ind] = k+1
                    cnt=0
                    break
                else:
                    cnt+=1
                    continue
    for i in c:
        print(i,end=" ")

# solution()


#-----------영상 풀이 코드 -------------------
n = int(input())
w = list(map(int, input().split()))
seq = [0]*n
for i in range(n):
    for j in range(n):
        if w[i] == 0 and seq[j] == 0:
            seq[j] = i+1
            break
        elif seq[j] == 0:
            w[i]-=1
for x in seq:
    print(x, end=" ")