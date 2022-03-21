#---------- 정답 입력 코드 -----------------
import sys
NUM = 1
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/8. 곳감/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/8. 곳감/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#-----------------------------------------

#------------ 내 풀이 코드 ------------------
from collections import deque
def solution():
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
#-----------영상 풀이 코드 -------------------
def answer():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())
    for i in range(m):
        r,d,k = map(int, input().split())
        if d==0:
            for _ in range(k):  #행렬 회전 시작
                matrix[r-1].append(matrix[r-1].pop(0)) # => 한줄로 가능
        else:
            for _ in range(k):  # 행렬 회전 시작
                matrix[r - 1].insert(0,matrix[r - 1].pop())  # => 한줄로 가능
    s=0
    e=n-1
    res = 0
    for i in range(n):
        for j in range(s,e+1):
            res+=matrix[i][j]
        if i < n//2:
            s+=1
            e-=1
        else:
            s-=1
            e+=1
    print(res)
#-----------------deque 이용 --------------------
def use_deque():
    n = int(input())
    matrix = [deque(map(int, input().split())) for _ in range(n)]
    m = int(input())
    for i in range(m):
        r, d, k = map(int, input().split())
        if d == 0:
            for _ in range(k):  # 행렬 회전 시작
                matrix[r - 1].append(matrix[r - 1].popleft())  # => 한줄로 가능
        else:
            for _ in range(k):  # 행렬 회전 시작
                matrix[r - 1].appendleft(matrix[r - 1].pop())  # => 한줄로 가능
    s = 0
    e = n - 1
    res = 0
    for i in range(n):
        for j in range(s, e + 1):
            res += matrix[i][j]
        if i < n // 2:
            s += 1
            e -= 1
        else:
            s -= 1
            e += 1
    print(res)

use_deque()