#---------- 정답 입력 코드 -----------------
import sys
NUM = 1
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/3. 카드 역배치/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/3. 카드 역배치/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#-----------------------------------------

#------------ 내 풀이 코드 -----------------

origin = [x for x in range(1,21)]
def solution(matrix):
    for _ in range(10):
        a,b = map(int, input().split())
        left = matrix[:a-1]
        target = matrix[a-1:b]
        right = matrix[b:]
        matrix = left + [x for x in reversed(target)] + right
    return matrix

# for i in solution(origin):
#    print(i, end=" ")
#------------ 영상 풀이 코드 -----------------

a = list(range(21))

for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]

for i in a[1:]:
    print(i,end=" ")


