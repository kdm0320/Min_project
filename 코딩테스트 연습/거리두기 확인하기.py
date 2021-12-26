from collections import deque



D = ((-1,0),(1,0),(0,-1),(0,1))

def bfs(place, row, col):
    visited = [[False for _ in range(5)] for _ in range(5)]
    q = deque()
    visited[row][col] = True
    q.append((row,col,0))

    while not len(q) == 0:
        curr = q.popleft()

        if curr[2] > 2:
            continue
        if curr[2] != 0 and place[curr[0]][curr[1]] == 'P':
            return False

        for i in range(4):
            nr = curr[0] + D[i][0]
            nc = curr[1] + D[i][1]
            if nr < 0 or nr > 4 or nc < 0 or nc > 4:
                continue
            if visited[nr][nc]:
                continue
            if place[nr][nc] == 'X':
                continue
            visited[nr][nc] = True
            q.append((nr,nc,curr[2]+1))
    return True

def check(place):
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                if bfs(place,r,c) == False:
                    return False
    return True

def solution(places):
    answer = []

    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))