#---------- 정답 입력 코드 -----------------
import sys
NUM = 4
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/8. 곳감/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/8. 곳감/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#-----------------------------------------

#------------ 내 풀이 코드 ------------------
from collections import deque
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(deque(map(int,input().split())))
m = int(input())
orders = []
for _ in range(m):
    orders.append(list(map(int,input().split())))
for order in orders:
    if not order[1]:
        for r in range(order[2]):
            target = matrix[order[0]-1].popleft()
            matrix[order[0]-1].append(target)
    else:
        for r in range(order[2]):
            target = matrix[order[0]-1].pop()
            matrix[order[0]-1].appendleft(target)
change = False
cnt = 0
i = 0
j = n
for row in range(n):
    if not change:
        cnt+=sum(list(matrix[row])[i:j])
        i+=1
        j-=1
        if i==n//2:
            change = True
    else:
        cnt+=sum(list(matrix[row])[i:j])
        i-=1
        j+=1

print(cnt)
