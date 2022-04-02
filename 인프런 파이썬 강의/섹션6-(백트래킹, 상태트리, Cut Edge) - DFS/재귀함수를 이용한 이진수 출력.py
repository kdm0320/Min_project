#---------- 정답 입력 코드 -----------------
import sys
NUM = 1
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/1. 재귀함수란(이진수출력)/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/1. 재귀함수란(이진수출력)/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 ----------------- => 이진수를 어케 만들지

def dfs(n):
  if n == 0:
    return
  else:
    dfs(n//2)
    print(n%2, end="" )



def solution():
  n = int(input())
  dfs(n)


solution()


#-----------영상 풀이 코드 -------------------


