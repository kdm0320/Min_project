#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/7. 사과나무/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/7. 사과나무/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#-----------------------------------------

#------------ 내 풀이 코드 ------------------
n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
cnt =0
mid = n//2
i =mid
j = mid+1
change = False
for row in range(n):
    if not change:
        cnt+=sum(matrix[row][i:j])
        i-=1
        j+=1
        if i==0:
            change = True
    else:
        cnt+=sum(matrix[row][i:j])
        i+=1
        j-=1
print(cnt)

