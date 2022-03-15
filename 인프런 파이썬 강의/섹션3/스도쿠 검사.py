#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/10. 스도쿠 검사/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/10. 스도쿠 검사/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#-----------------------------------------

#------------ 내 풀이 코드 ------------------

def is_right_big(matrix):
    for row in range(len(matrix)):
        row_test = set(matrix[row])
        if len(row_test) < len(matrix):
            return False
    c_matrix = []
    for i in range(len(matrix)):
        c_matrix.append([])
        for j in range(len(matrix)):
            c_matrix[i].append(matrix[j][i])

    for c in range(len(matrix)):
        c_test = set(c_matrix[c])
        if len(c_test) < len(matrix):
            return False
    return True

def is_right_div(matirx):
    test = set(x for x in range(1,10))
    target = set()
    for r in matirx:
        for i in r:
            target.add(i)

    if len(target) != len(test):
        return False
    return True

def solution():
    sdoku = []
    for _ in range(9):
        sdoku.append(list(map(int, input().split())))
    if is_right_big(sdoku):
        c_div = 0
        for _ in range(3):
            r_div = 0
            for _ in range(3):
                div_sdoku = []
                for j in range(3):
                    div_sdoku.append(sdoku[j+c_div][r_div:r_div+3])
                r_div+=3
                if not is_right_div(div_sdoku):
                    return "NO"
            c_div+=3
        return "YES"

    else:
        return "NO"

#-----------영상 풀이 코드 -------------------
def check(matrix):
    for i in range(9):
        row_check = [0] * 10
        col_check = [0] * 10
        for j in range(9):
            row_check[matrix[i][j]] = 1
            col_check[matrix[j][i]] = 1
        if sum(row_check) != 9 or sum(col_check) !=9:
            return False
    for i in range(3):
        for j in range(3):
            group_check = [0]*10
            for k in range(3):
                for s in range(3):
                    group_check[matrix[i*3+k][j*3+s]] = 1
            if sum(group_check) != 0:
                return False
    return True

sdoku = [list(map(int,input().split())) for _ in range(9)]

if check(sdoku):
    print("YES")
else:
    print("NO")