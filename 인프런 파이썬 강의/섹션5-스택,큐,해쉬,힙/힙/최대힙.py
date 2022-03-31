#---------- 정답 입력 코드 -----------------
import sys
NUM = 2
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/11. 최대힙/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/11. 최대힙/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------
import heapq

def solution():
  h = []
  while True:
    a = int(input())
    if a == -1:
      break
    if not a:
      if len(h) == 0:
        print(-1)
      else:
        print(-heapq.heappop(h))
    else:
      heapq.heappush(h,-a)

solution()


#-----------영상 풀이 코드 -------------------


