#---------- 정답 입력 코드 -----------------
import sys
NUM = 1
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/14. 인접행렬/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 6/14. 인접행렬/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------
def solution():
    n,m = map(int, input().split())
    infos = [list(map(int,input().split())) for _ in range(m)]
    matrix = [[0]*n for _ in range(n)]
    for info in infos:
        matrix[info[0]-1][info[1]-1] = info[2]
    for c in matrix:
        for i in c:
            print(i,end=" ")
        print()
solution()

#-----------영상 풀이 코드 -------------------
