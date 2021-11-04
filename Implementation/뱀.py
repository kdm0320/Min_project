from collections import deque

n = int(input())
k = int(input())
#맵 정보 - 사과 있는 곳은 1로 표시
data = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
	a,b = map(int, input().split())
	data[a][b] = 1
#방향 회전 정보 입력
l = int(input())
info = []
for _ in range(l):
	x,c = input().split()
	info.append((int(x),c))
#처음에는 오른쪽을 보고 있으므로(동,남,서,북) -> 프로그래밍의 행렬에서의 x와 y / x = 행, y = 열
dx = [0,1,0,-1]
dy =[1,0,-1,0]

def turn(direction,c):
	if c=="L":
		direction = (direction - 1) % 4 #-> (0-1)%4 = 3 인 이유는 나머지는 원래수 - 몫*나누는 수 인데 파이썬은 몫은 내림을 한다.
	else:								#따라서 (0-1)//4 = -1 이고 -1 - 4*(-1) = 3이 나머지가 되는 것이다.
		direction = (direction + 1) % 4
	return direction
	
def simulate():
	x,y =1, 1 #뱀의 머리 위치 / 실제 좌표가 아닌 행렬의 좌표로 봐야한다.
	data[x][y] = 2 #뱀이 존재하는 위치는 2로 표시
	a = data
	direction = 0 #처음에는 동쪽을 보고 잇음
	time = 0 # 시작한 뒤에 지난 '초' 시간
	index = 0 # 다음에 회전할 정보
	q = deque([(x,y)]) # deque로 하면 pop()의 시간복잡도를 줄일 수 있다
	# q =[(x,y)] #뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
	while True:
		nx = x+dx[direction]
		ny = y + dy[direction]

		#맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
		if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
			if data[nx][ny] == 0:
				data[nx][ny] = 2
				q.append((nx,ny))
				px, py = q.popleft()
				# px,py = q.pop(0)
				data[px][py] = 0
			# 사과가 있다면 이동 후에 꼬리 그대로 두기
			if data[nx][ny] == 1:
				data[nx][ny] = 2
				q.append((nx,ny))
		#벽이나 뱀의 몸통과 부딪혔다면
		else:
			time+=1
			break
		x,y = nx,ny # 다음 위치로 머리를 이동
		time+=1
		if index <1 and time == info[index][0]: # 회전할 시간인 경우 회전
			direction = turn(direction,info[index][1])
			index+=1
	return time

print(simulate())

