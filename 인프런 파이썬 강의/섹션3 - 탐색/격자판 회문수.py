#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/11. 격자판 회문수/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/11. 격자판 회문수/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#-----------------------------------------

#------------ 내 풀이 코드 ------------------

def is_palindrome(row):
    check = 0
    for i in range(3):
        finish = i+4
        for j in range(2):
            if row[i+j] != row[finish-j]:
                break
        else:
            check+=1
    return check

def solution():
    matrix = []
    for _ in range(7):
        matrix.append(list(map(int, input().split())))
    answer = 0
    #행검사
    for r in range(7):
        answer+=is_palindrome(matrix[r])
    #열검사
    c_matirx = []
    for i in range(7):
        c_matirx.append([])
        for j in range(7):
            c_matirx[i].append(matrix[j][i])
    for c in range(7):
        answer += is_palindrome(c_matirx[c])
    print(answer)
#-----------영상 풀이 코드 -------------------
matrix = [list(map(int,input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = matrix[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt+=1
        for k in range(2):
            if matrix[i+k][j] != matrix[i+5-k-1][j]:
                break
        else:
            cnt+=1
print(cnt)
