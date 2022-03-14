

#---------- 정답 입력 코드 -----------------
import sys
NUM = 1
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 2/10. 점수 계산/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 2/10. 점수 계산/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------
n = input()
scores = input().split()
check = []
answer = 0
for score in scores:
    if score == '0':
        check=[]
    else:
        check.append(score)
        answer+=len(check)
print(answer)