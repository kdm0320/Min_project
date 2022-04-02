#---------- 정답 입력 코드 -----------------
import sys
NUM = 4
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/4. 합이 같은 부분집합/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/4. 합이 같은 부분집합/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 ----------------- => 실패


#-----------영상 풀이 코드 -------------------

def dfs(l,sum):
  if sum > total //2:
      return
  if l == n:
      if sum == (total-sum):
          print("YES")
          sys.exit(0)
  else:
      dfs(l+1,sum+a[l])
      dfs(l+1,sum)


n = int(input())
a = list(map(int, input().split()))
total = sum(a)
dfs(0,0)
print("NO")