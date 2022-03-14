#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/3. 카드 역배치/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/3. 카드 역배치/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#-----------------------------------------

#------------ 내 풀이 코드 -----------------

origin = [x for x in range(1,21)]
for _ in range(10):
    a,b = map(int, input().split())
    left = origin[:a-1]
    target = origin[a-1:b]
    right = origin[b:]
    origin  = left + [x for x in reversed(target)] + right

for i in origin:
    print(i, end=" ")