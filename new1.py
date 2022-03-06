


def dfs(x,y,n,m,board,check,k):
    if x <= -1 or x>=n or y <= -1 or y>=m:
        return False
    if check>=k:
        return True
    else:
        check+=1
    if board[x][y] == 1:
        dfs(x-1,y,n,m,board,check,k)
        dfs(x,y-1,n,m,board,check,k)
        dfs(x+1,y,n,m,board,check,k)
        dfs(x-1,y+1,n,m,board,check,k)
        return True
    return False



def solution(h,w,n,board):
    new_board = [[] for _ in range(h)]
    for index,rows in enumerate(board):
        for r in rows:
            new_board[index].append(int(r))
    result = 0
    check = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j, h, w,new_board,check,n) == True:
                result += 1
                check=0
    return result

grid =[[1,1,1,1],[2,1,2,2],[2,2,2,1],[1,1,2,2]]
board = ["11111","11111","11111","11111","11111"]
h = 5
w = 5
n = 5
print(solution(h,w,n,board))