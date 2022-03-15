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
def solution():
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
#-----------영상 풀이 코드 -------------------
n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
matrix.insert(0,[0]*n)
matrix.append([0]*n)
for row in matrix:
    row.insert(0,0)
    row.append(0)

dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if all(matrix[i][j]>matrix[i+dx[k]][j+dy[k]] for k in range(4)): #all 알아두기
            cnt+=1
print(cnt)