#---------- 정답 입력 코드 -----------------
import sys
NUM = 1
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/10. 조합 구하기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/10. 조합 구하기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------

#-----------영상 풀이 코드 -------------------
def dfs(l,s):
    if l==m:
        global cnt
        for i in range(m):
            print(res[i], end=" ")
        print()
        cnt+=1
        return
    else:
        for i in range(s,n+1):
            res[l] = i
            dfs(l+1,i+1)

n,m = map(int, input().split())
res = [0]*m
cnt = 0
dfs(0,1)
print(cnt)