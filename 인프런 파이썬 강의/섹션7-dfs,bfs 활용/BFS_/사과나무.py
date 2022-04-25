#---------- 정답 입력 코드 -----------------
import sys
NUM = 3
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/8. 사과나무/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/8. 사과나무/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------
#
# n = int(input())
# farm = [list(map(int, input().split())) for _ in range(n)]
# mid = len(farm)//2
# answer = 0
# start = 0
# last = n
# for i in range(mid,-1,-1):
#     answer+=sum(farm[i][start:last])
#     start+=1
#     last-=1
# start=0
# last=n
# for i in range(mid,n):
#     answer+=sum(farm[i][start:last])
#     start+=1
#     last-=1
# answer-=sum(farm[mid])
# print(answer)

#-----------영상 풀이 코드 -------------------
from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
sum=0
q = deque()
ch[n//2][n//2] = 1
sum+=a[n//2][n//2]
q.append((n//2,n//2))
l=0
while True:
    if l==n//2:
        break
    size = len(q)
    for i in range(size):
        tmp = q.popleft()
        for j in range(4):
            x = tmp[0]+dx[j]
            y = tmp[1]+dy[j]
            if ch[x][y] == 0:
                sum+=a[x][y]
                ch[x][y]=1
                q.append((x,y))
    l+=1

print(sum)