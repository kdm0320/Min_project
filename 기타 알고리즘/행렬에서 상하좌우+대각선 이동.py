"""
행이나 열을 위아래로 혹은 좌우로 이동하는 것 => 큐를 쓸것
"""
from collections import deque

#행의 이동 - 좌:0, 우:1

#이동 오더 [행의번호, 좌/우 , 이동할 거리]
row_order = [1,0,3]

#행렬
n = 5 # n X n 행렬
matrix = []
e = 1
for r in range(n):
    matrix.append([])
    for c in range(n):
        matrix[r].append(e)
        e+=1
#좌우 이동만 있을땐 바로 deque로 추가
# for r in range(n):
#     matrix.append(deque([]))
#     for c in range(n):
#         matrix[r].append(c)

# 상하 이동도 있을땐 좌우(행) / 상하(렬) 따로 만들것

def lr_move(matrix,row_order):
    lr_matrix = []
    for r in range(n):
        lr_matrix.append(deque(matrix[r]))
    #좌
    if not row_order[1]:
        for r in range(row_order[2]):
            target = lr_matrix[row_order[0] - 1].popleft()
            lr_matrix[row_order[0] - 1].append(target)

    #우
    else:
        for r in range(row_order[2]):
            target = lr_matrix[row_order[0] - 1].pop()
            lr_matrix[row_order[0] - 1].appendleft(target)
    return lr_matrix
# #열의 이동 - 상:0, 하:1
# column_order = [1,0,3]
#
# #열의 이동 => 행렬의 재구성 필요
def ud_move(matrix, column_order):
    ud_matrix = []
    for r in range(n):
        ud_matrix.append(deque([]))
        for c in range(n):
            ud_matrix[r].append(matrix[c][r])
    #상
    if not column_order[1]:
        for r in range(column_order[2]):
            target = ud_matrix[column_order[0] - 1].popleft()
            ud_matrix[column_order[0] - 1].append(target)
    #하
    else:
        for r in range(column_order[2]):
            target = ud_matrix[column_order[0] - 1].pop()
            ud_matrix[column_order[0] - 1].appendleft(target)

    return ud_matrix

#행렬 동시 이동
# - 순서대로 실행 -> 좌우 이동 후 상하로 상하 이동후 좌우로 행렬 구성
# rl_order = [1,0,3]
# ud_order = [1,0,3]
# #좌우부터 실핼
# rl_matrix = lr_move(matrix,rl_order)
# #상하실행
# ud_matrix = ud_move(rl_matrix,ud_order)
# #원래 행렬로
# #좌우가 마지막일때
def add_lr_matrix(lr_matrix):
    new_matrix0 = []
    for i in lr_matrix:
        new_matrix0.append(list(i))
    return new_matrix0

#상하가 마지막일때
def add_up_matrix(ud_matrix):
    new_matrix1 = []
    for i in range(n):
        new_matrix1.append([])
        for j in range(n):
            new_matrix1[i].append(ud_matrix[j][i])
    return new_matrix1

#대각선 이동

diagonal_order = [1,3]

# 대각선 행렬 구성 -> 각각 한 행만 있으면 됨
#왼쪽 위 => 오른쪽 아래
def create_left_diagonal(matrix):
    left_diagonal = deque([])
    for i in range(n):
        left_diagonal.append(matrix[i][i])
    return left_diagonal
#오른쪽 위 => 왼쪽 아래
def create_right_diagonal(matrix):
    right_diagonal = deque([])
    j = n - 1
    for i in range(n):
        right_diagonal.append(matrix[i][j])
        j -= 1
    return right_diagonal

# ↙️↘️ = 하 = 우 = 1(임의) ↖ ↗ = 상 = 좌 = 0(임의)
def diagonal_move(diagonal,diagonal_order):
    # 상
    new_diagonal = diagonal
    if not diagonal_order[0]:
        for _ in range(diagonal_order[1]):
            target = new_diagonal.popleft()
            new_diagonal.append(target)
    # 하
    else:
        for _ in range(diagonal_order[1]):
            target = new_diagonal.pop()
            new_diagonal.appendleft(target)
    return new_diagonal

#왼-위 -> 오-아 대각선 집어넣기
def add_left_diagonal(left_diagonal,matrix):
    new_matrix = matrix
    for i in range(n):
        new_matrix[i][i] = left_diagonal[i]
    return new_matrix

#오-위 -> 왼-아 대각선 집어넣기
def add_right_diagonal(right_diagonal,matrix):
    new_matrix = matrix
    j = n - 1
    for i in range(n):
        new_matrix[i][j] = right_diagonal[i]
        j -= 1
    return new_matrix

print(matrix)
#상,좌,왼쪽에서 오른쪽 대각선,왼아->오위,오아->왼위 = 0
#하,우,오른쪽에서 왼쪽 대각선,왼위->오아,오위->왼아 = 1
lr_order = [1,0,3] #첫번째 행렬 왼쪽으로 3칸 이동
ud_order = [1,0,3] #첫번째 행렬 위로 3칸 이동
diagonal_order0 = [0,3] # 왼쪽에서 오른쪽 대각선,오아->왼위 3칸 이동
diagonal_order1 = [1,2] # 오른쪽에서 왼쪽 대각선,오위->왼아 2칸 이동
#좌우 이동
lr_matrix = lr_move(matrix,lr_order)
print(lr_matrix)
#상하이동
ud_matrix = ud_move(lr_matrix,ud_order)
print(ud_matrix)
tmp_matrix = add_up_matrix(ud_matrix)
print(tmp_matrix)
#왼쪽에서 오른쪽 대각선 이동
#1.왼쪽-오른쪽 대각선 생성
left_diago = create_left_diagonal(tmp_matrix)
#2.이동
moved_left_diag0 = diagonal_move(left_diago,diagonal_order0)
#3.합침
tmp_matrix = add_left_diagonal(moved_left_diag0,tmp_matrix)
#오른쪽에서 왼쪽 대각선 이동
#1.오른쪽-왼쪽 대각선 생성
right_diago = create_right_diagonal(tmp_matrix)
#2.이동
moved_right_diag0 = diagonal_move(right_diago,diagonal_order1)
#3.합침
tmp_matrix = add_right_diagonal(moved_right_diag0,tmp_matrix)
print(tmp_matrix)