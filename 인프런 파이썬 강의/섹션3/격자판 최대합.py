#---------- 정답 입력 코드 -----------------
import sys
NUM = 4
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/6. 격자판 최대합/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/6. 격자판 최대합/out{NUM}.txt")
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

#행합
row_sum = 0
for row in matrix:
    if row_sum < sum(row):
        row_sum = sum(row)
#열합
column_sum = 0
for c in range(n):
    tmp = 0
    for r in range(n):
        tmp+=matrix[r][c]
    column_sum = max(column_sum,tmp)
#대각선합
diagonal_sum = 0
sec = 0
#왼쪽 위에서 오른쪽 아래로
for i in range(5):
    diagonal_sum += matrix[i][i]
#오른쪽 위에서 왼쪽 아래로
j = n-1
for i in range(n):
    sec+=matrix[i][j]
    j-=1

diagonal_sum = max(diagonal_sum,sec)
print(max(row_sum,diagonal_sum,column_sum))