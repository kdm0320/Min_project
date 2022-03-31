#---------- 정답 입력 코드 -----------------
import sys
NUM = 3
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/9. 아나그램(구글)/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/9. 아나그램(구글)/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------
from collections import Counter
def solution():
  f = input()
  s = input()
  f_c = Counter(f)
  s_c = Counter(s)
  try:
    for i in f_c:
      if f_c[i] != s_c[i]:
        print("NO")
        break
    else:
      print("YES")
  except KeyError:
    print("NO")

# solution()


#-----------영상 풀이 코드 -------------------

a = input()
b = input()
sh = dict()
for x in a:
  sh[x] = sh.get(x,0)+1
for x in b:
  sh[x] = sh.get(x, 0) - 1
for i in sh:
  if sh[i] > 0:
    print("NO")
    break
else:
  print("YES")

