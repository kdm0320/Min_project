
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]


from collections import deque

def solution(board, moves):  
    answer = 0
    q =deque([0])
    new_board = list(map(list,zip(*board)))
    for i in moves:
            for index,doll in enumerate(new_board[i-1]):
                if doll !=0:
                    q.append(doll)
                    new_board[i-1][index] = 0
                    break
            if q[-2]==q[-1]:
                for _ in range(2):
                    q.pop()
                    answer+=1
    return answer
    
print(solution(board,moves))
