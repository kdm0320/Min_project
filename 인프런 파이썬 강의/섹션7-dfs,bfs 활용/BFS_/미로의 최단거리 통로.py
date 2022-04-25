#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/9. 미로의 최단거리 통로/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 7/9. 미로의 최단거리 통로/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 ----------------- => 실패

# maze = [list(map(int, input().split())) for _ in range(7)]
# ch = [[0]*7 for _ in range(7)]
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# x=0
# y=0
# cnt = 0
#     for i in range(4):
#         tx = x+dx[i]
#         ty = y+dy[i]
#         if tx < 0 or ty < 0 or ch[tx][ty] == 1 or maze[tx][ty]==1:
#             continue
#         else:
#             if tx==6 and ty==6:
#
#             x = tx
#             y = ty
#             ch[x][y] = 1





#-----------영상 풀이 코드 -------------------
from collections import deque
board = [list(map(int, input().split())) for _ in range(7)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
dis = [[0]*7 for _ in range(7)]
q = deque()
q.append((0,0))
board[0][0] = 1
while q:
    tmp = q.popleft()
    for i in range(4):
        x = tmp[0]+dx[i]
        y = tmp[1]+dy[i]
        if 0 <= x <= 6 and 0<= y <= 6 and board[x][y] == 0:
            board[x][y] = 1
            dis[x][y] = dis[tmp[0]][tmp[1]]+1
            q.append((x,y))
if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])

