#---------- 정답 입력 코드 -----------------
import sys
NUM = 1
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/4. 동전바꿔주기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/4. 동전바꿔주기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------
#------------ 내 풀이 코드 ----------------- => 실패

def dfs(v,price):
    global cnt
    if price > t:
        return
    if v==k:
        if price==t:
            cnt+=1
    else:
        for j in range(n[v]+1):    #----> 2중 for문으로 돌렸었음
            dfs(v+1,price+p[v]*j)


t =int(input())
k = int(input())
p =[]
n =[]
for i in range(k):
    a,b = map(int,input().split())
    p.append(a)
    n.append(b)
cnt=0
dfs(0,0)
print(cnt)
#-----------영상 풀이 코드 -------------------

def dfs(v,price):
    global cnt
    if price > t:
        return
    if v==k:
        if price==t:
            cnt+=1
    else:
        for j in range(n[v]+1):
            dfs(v+1,price+p[v]*j)


t =int(input())
k = int(input())
p =[]
n =[]
for i in range(k):
    a,b = map(int,input().split())
    p.append(a)
    n.append(b)
cnt=0
dfs(0,0)
print(cnt)