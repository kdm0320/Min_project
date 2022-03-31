#---------- 정답 입력 코드 -----------------
import sys
NUM = 2
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/7. 교육과정 설계/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/7. 교육과정 설계/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------
from collections import  deque
def solution():
   es = input()
   n = int(input())
   lis = list(input() for _ in range(n))
   target = ""
   tmp = list(es)
   for index, i in enumerate(lis):
      q = deque(i)
      while q:
         if q[0] in tmp:
            target+=q.popleft()
         else:
            q.popleft()
      if len(target)>=len(es):
         for k in range(len(es)):
            if es[k]!=target[k]:
               print(f"#{index + 1} NO")
               break
         else:
            print(f"#{index + 1} YES")

      else:
         print(f"#{index+1} NO")
      target=""


# solution()


#-----------영상 풀이 코드 -------------------

need = input()
n =int(input())
for i in range(n):
   plan = input()
   dq = deque(need)
   for x in plan:
      if x in dq:
         if x != dq.popleft():
            print(f"#{i+1} NO")
            break
   else:
      if len(dq)==0:
         print(f"#{i+1} YES")
      else:
         print(f"#{i+1} NO")


