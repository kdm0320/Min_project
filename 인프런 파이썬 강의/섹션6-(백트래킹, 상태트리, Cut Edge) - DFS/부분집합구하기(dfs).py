#---------- 정답 입력 코드 -----------------
import sys
NUM = 1
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/3. 부분집합 구하기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/3. 부분집합 구하기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 ----------------- => 실패




def solution():
  n = int(input())



# solution()


#-----------영상 풀이 코드 -------------------

def dfs(v):
  if v==n+1:
    for i in range(1,n+1):
      if ch[i] == 1:
        print(i, end=" ")
    print()
    return
  else:
    ch[v] = 1
    dfs(v+1)
    ch[v] = 0
    dfs(v+1)


n = int(input())
ch = [0]*(n+1)
dfs(1)
