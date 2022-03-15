#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/9. 봉우리/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/9. 봉우리/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#-----------------------------------------

#------------ 내 풀이 코드 ------------------
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        target = matrix[i][j]
        for k in range(4):
            nx = dx[k]+i
            ny = dy[k]+j
            if nx < 0 or ny < 0 or nx >= len(matrix) or ny >= len(matrix):
                continue
            if target <= matrix[nx][ny]:
                break
        else:
            answer+=1

print(answer)
