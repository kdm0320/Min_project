#---------- 정답 입력 코드 -----------------
import sys
NUM = 3
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/9. 아나그램(구글)/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/9. 아나그램(구글)/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 ----------------- => 리스트 해쉬 아님
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


#-----------영상 풀이 코드 ------------------- => 아스키 이용

a = input()
b = input()
str1 = [0]*52
str2 = [0]*52
#나중에
