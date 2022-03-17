#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/4. 두 리스트 합치기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/4. 두 리스트 합치기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#-----------------------------------------

#------------ 내 풀이 코드 ------------------

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    for i in sorted(a+b):
        print(i, end=" ")

#-----------영상 풀이 코드 -------------------
"""
이미 정렬되어있는 경우 아래와 같은 삽입 정렬이 오히려 더 효과적
"""
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
c = []
p1 = 0
p2 = 0
while p1<n and p2<m:
    if a[p1]<=b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
if p1 < n:
    c+=a[p1:]
if p2 < m:
    c+=b[p2:]

for i in c:
    print(i, end=" ")